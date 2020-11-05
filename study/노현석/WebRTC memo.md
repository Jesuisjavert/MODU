# WebRTC



> webrtc란 한개의 화면을 재생하고  RTCPeerconnection을 통해서 같은 화면을 다른 사람에게 보여주는 형식



### step-02

- 







npm i vue-webrtc

npm i plugin



- 난수발생은
  - uuid 라이브러리 사용하기





```javascript
<template>
<v-app>
        <h1> 
            여기는 WebMeeting.vue
        </h1>
      <div >
      
      <v-btn
        class="ma-2"
        color="secondary"
        id="cameraBtn" @click="openUserMedia"
      >
        비디오 시작
      </v-btn>

      <v-btn
        color="blue-grey"
        class="ma-2 white--text"
         id="createBtn" @click="createRoom"
      >
        방 생성
        <v-icon
          right
          dark
        >
          mdi-cloud-upload
        </v-icon>
      </v-btn>

      <!-- //////////////////////////-->
        <v-dialog
          v-model="dialog"
          persistent
          max-width="290"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              dark
              v-bind="attrs"
              v-on="on"
            >
              <!-- id="joinBtn" @click="joinRoom" -->
              방 들어가기

            </v-btn>
          </template>
          <v-card>
            <v-card-title class="headline">
              Room ID를 입력해주세요
            </v-card-title>

            <v-text-field
            v-model="room_id"
            label="Room ID"
            required
            outlined
            dense
          ></v-text-field>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="green darken-1"
                text
                @click="dialog = false"
              >
                취소
              </v-btn>
              <v-btn
                color="green darken-1"
                text
                id="confirmJoinBtn"
                @click="joinRoomById"
              >
                입장
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

      

      <v-btn
        class="ma-2"
        color="info"
        id="hangupBtn" @click="hangUp"
      >
        Hang Up
        
      </v-btn>

</div>
<div>
    <span id="currentRoom"></span>
</div>
<div id="videos">
    <video id="localVideo" muted autoplay playsinline></video>
    <video id="remoteVideo" autoplay playsinline></video>
</div>

        <!-- <video id="gum-local" autoplay playsinline></video> -->
        <!-- <v-btn id="showVideo" color="info" @click="getUserMedia">카메라</v-btn> -->
        <!-- <v-btn id="startButton" color="info" @click="shareScreen">화면공유</v-btn> -->

</v-app>
</template>

<script>
import adapter from 'webrtc-adapter'
import db from '../../firebaseInit'

if (adapter.browserDetails.browser == 'firefox') {
  adapter.browserShim.shimGetDisplayMedia(window, 'screen');
}

// mdc.ripple.MDCRipple.attachTo(document.querySelector('.mdc-button'));


const configuration = {
  iceServers: [
    {
      urls: [
        'stun:stun1.l.google.com:19302',
        'stun:stun2.l.google.com:19302',
      ],
    },
  ],
  iceCandidatePoolSize: 10,
};


let peerConnection = null;
let localStream = null;
let remoteStream = null;
// let roomDialog = null;
let roomId = null;

// roomDialog = new mdc.dialog.MDCDialog(document.querySelector('#room-dialog'));




function registerPeerConnectionListeners() {
  peerConnection.addEventListener('icegatheringstatechange', () => {
    console.log(
        `ICE gathering state changed: ${peerConnection.iceGatheringState}`);
  });

  peerConnection.addEventListener('connectionstatechange', () => {
    console.log(`Connection state change: ${peerConnection.connectionState}`);
  });

  peerConnection.addEventListener('signalingstatechange', () => {
    console.log(`Signaling state change: ${peerConnection.signalingState}`);
  });

  peerConnection.addEventListener('iceconnectionstatechange ', () => {
    console.log(
        `ICE connection state change: ${peerConnection.iceConnectionState}`);
  });
}


export default {
    name : "",
    data(){
      return{
        dialog: false,
        room_id : "",
        isCameraBtnDisabled : false,
        isCreateBtnDisabled : false,
      }
    },
    methods :{
        

        // async shareScreen(){
        //   navigator.mediaDevices.getDisplayMedia({video: true})
        //   .then(handleSuccess, handleError);
        // },

        async createRoom() {
          document.querySelector('#createBtn').disabled = true;
          const roomRef = await db.collection('rooms').doc();

          console.log('Create PeerConnection with configuration: ', configuration);
          peerConnection = new RTCPeerConnection(configuration);

          registerPeerConnectionListeners();

          localStream.getTracks().forEach(track => {
            peerConnection.addTrack(track, localStream);
          });

          // Code for collecting ICE candidates below
          const callerCandidatesCollection = roomRef.collection('callerCandidates');

          peerConnection.addEventListener('icecandidate', event => {
            if (!event.candidate) {
              console.log('Got final candidate!');
              return;
            }
            console.log('Got candidate: ', event.candidate);
            callerCandidatesCollection.add(event.candidate.toJSON());
          });
          // Code for collecting ICE candidates above

          // Code for creating a room below
          const offer = await peerConnection.createOffer();
          await peerConnection.setLocalDescription(offer);
          console.log('Created offer:', offer);

          const roomWithOffer = {
            'offer': {
              type: offer.type,
              sdp: offer.sdp,
            },
          };
          await roomRef.set(roomWithOffer);
          roomId = roomRef.id;
          console.log(`New room created with SDP offer. Room ID: ${roomRef.id}`);
          document.querySelector(
              '#currentRoom').innerText = `Current room is ${roomRef.id} - You are the caller!`;
          // Code for creating a room above

          peerConnection.addEventListener('track', event => {
            console.log('Got remote track:', event.streams[0]);
            event.streams[0].getTracks().forEach(track => {
              console.log('Add a track to the remoteStream:', track);
              remoteStream.addTrack(track);
            });
          });

          // Listening for remote session description below
          roomRef.onSnapshot(async snapshot => {
            const data = snapshot.data();
            if (!peerConnection.currentRemoteDescription && data && data.answer) {
              console.log('Got remote description: ', data.answer);
              const rtcSessionDescription = new RTCSessionDescription(data.answer);
              await peerConnection.setRemoteDescription(rtcSessionDescription);
            }
          });
          // Listening for remote session description above

          // Listen for remote ICE candidates below
          roomRef.collection('calleeCandidates').onSnapshot(snapshot => {
            snapshot.docChanges().forEach(async change => {
              if (change.type === 'added') {
                let data = change.doc.data();
                console.log(`Got new remote ICE candidate: ${JSON.stringify(data)}`);
                await peerConnection.addIceCandidate(new RTCIceCandidate(data));
              }
            });
          });
        },


        async  joinRoomById(){
          const roomRef = db.collection('rooms').doc(this.room_id);
          const roomSnapshot = await roomRef.get();
          console.log(this.room_id)
          console.log(roomRef)

          if (roomSnapshot.exists) {
            console.log('Create PeerConnection with configuration: ', configuration);
            peerConnection = new RTCPeerConnection(configuration);
            registerPeerConnectionListeners();
            localStream.getTracks().forEach(track => {
              peerConnection.addTrack(track, localStream);
            });

            // Code for collecting ICE candidates below
            const calleeCandidatesCollection = roomRef.collection('calleeCandidates');
            peerConnection.addEventListener('icecandidate', event => {
              if (!event.candidate) {
                console.log('Got final candidate!');
                return;
              }
              console.log('Got candidate: ', event.candidate);
              calleeCandidatesCollection.add(event.candidate.toJSON());
            });
            // Code for collecting ICE candidates above

            peerConnection.addEventListener('track', event => {
              console.log('Got remote track:', event.streams[0]);
              event.streams[0].getTracks().forEach(track => {
                console.log('Add a track to the remoteStream:', track);
                remoteStream.addTrack(track);
              });
            });

            // Code for creating SDP answer below
            const offer = roomSnapshot.data().offer;
            console.log('Got offer:', offer);
            await peerConnection.setRemoteDescription(new RTCSessionDescription(offer));
            const answer = await peerConnection.createAnswer();
            console.log('Created answer:', answer);
            await peerConnection.setLocalDescription(answer);

            const roomWithAnswer = {
              answer: {
                type: answer.type,
                sdp: answer.sdp,
              },
            };
            await roomRef.update(roomWithAnswer);
            // Code for creating SDP answer above

            // Listening for remote ICE candidates below
            roomRef.collection('callerCandidates').onSnapshot(snapshot => {
              snapshot.docChanges().forEach(async change => {
                if (change.type === 'added') {
                  let data = change.doc.data();
                  console.log(`Got new remote ICE candidate: ${JSON.stringify(data)}`);
                  await peerConnection.addIceCandidate(new RTCIceCandidate(data));
                }
              });
            });
            // Listening for remote ICE candidates above
          }
          this.dialog=false;

        },
        

        async openUserMedia(){
          const stream = await navigator.mediaDevices.getUserMedia(
            {
              video : true,
              audio : true
            }
          );

          document.querySelector('#localVideo').srcObject = stream;
          localStream = stream;
          remoteStream = new MediaStream();
          document.querySelector('#remoteVideo').srcObject = remoteStream;

          // document.querySelector('#cameraBtn').disabled = true;
          // document.querySelector('#joinBtn').disabled = false;
          // document.querySelector('#createBtn').disabled = false;
          // document.querySelector('#hangupBtn').disabled = false;
        },

        async hangUp(){
          const tracks = document.querySelector('#localVideo').srcObject.getTracks();
          tracks.forEach(track=>{
            track.stop();
          });

          if(remoteStream){
            remoteStream.getTracks().forEach(track => track.stop());
          }

          if(peerConnection){
            peerConnection.close();
          }

          document.querySelector('#localVideo').srcObject = null;
          document.querySelector('#remoteVideo').srcObject = null;
          // document.querySelector('#cameraBtn').disabled = false;
          // document.querySelector('#joinBtn').disabled = true;
          // document.querySelector('#createBtn').disabled = true;
          // document.querySelector('#hangupBtn').disabled = true;
          document.querySelector('#currentRoom').innerText = '';

          if(roomId){
            const roomRef = db.collection('rooms').doc(roomId);
            const calleeCandidates = await roomRef.collection('calleeCandidates').get();
            calleeCandidates.forEach(async candidate => {
              await candidate.delete();
            });

            const callerCandidates = await roomRef.collection('callerCandidates').get();
            callerCandidates.forEach(async candidate =>{
              await candidate.delete();
            });
            await roomRef.delete();
          }

          document.location.reload(true);
        },
        
    }

}
</script>

<style scoped>


</style>
```





- WebCam.vue

```javascript
<template>
    <div class="container">
        <div>
            <h1>RoomID</h1>
            <v-text-field
                v-model="roomId"
                label="RoomID"
                placeholder="public-room"
                required
                outlined
                dense
            ></v-text-field>
        </div>
        <div class="row">
          <div class="col-md-12 my-3">
            <button type="button" class="btn btn-primary" @click="join">Join</button>
            <button type="button" class="btn btn-primary" @click="leave">Leave</button>
            <button type="button" class="btn btn-primary" @click="leave" v-if="this.inviteButtonFlag">Invite</button>
            
            <!-- <button type="button" class="btn btn-primary" @click="capture">Capture Photo</button> -->
            <button type="button" class="btn btn-primary" @click="shareScreen">Share Screen</button>
            <!-- <button type="button" class="btn btn-primary" @click="getCanvas">Get Canvas</button> -->
            <!-- <button type="button" class="btn btn-primary" @click="stopVideo">Stop Video</button> -->
          </div>
        </div>
        <div class="video-list" >
            <div v-for="item in videoList"
                v-bind:video="item"
                v-bind:key="item.id"
                class="video-item">
                <video controls autoplay playsinline ref="videos" v-if="localVideo.id === item.id" height="100" :muted="item.muted" :id="item.id" @click="printer(item)"></video>
                <video controls autoplay playsinline ref="videos" v-else :height="cameraHeight" :muted="item.muted" :id="item.id" @click="printer(item)"></video>
            </div>
        </div>
        <WebCreateBtn>시작하기</WebCreateBtn>
    </div>
</template>

<script>
  import RTCMultiConnection from 'rtcmulticonnection';
  import { uuid } from 'vue-uuid';
  require('adapterjs');
  export default {
    name: 'vue-webrtc',
    components: {
      WebCreateBtn: () => import('@/components/base/WebCreateBtn'),
    },
    data() {
      return {
        rtcmConnection: null,
        localVideo: null,
        videoList: [],
        canvas: null,
        roomId: 'public-room',
        uuid: '',
        inviteButtonFlag: false,
      };
    },
    props: {
    //   roomId: {
    //     type: String,
    //     default: 'public-room'
    //   },
      socketURL: {
        type: String,
        default: 'https://rtcmulticonnection.herokuapp.com:443/'
      },
      cameraHeight: {
        type: [Number, String],
        default: 500
      },
      autoplay: {
        type: Boolean,
        default: true
      },
      screenshotFormat: {
        type: String,
        default: 'image/jpeg'
      },
      enableAudio: {
        type: Boolean,
        default: true
      },
      enableVideo: {
        type: Boolean,
        default: true
      },
      enableLogs: {
        type: Boolean,
        default: false
      },
      stunServer: {
        type: String,
        default: null
      },
      turnServer: {
        type: String,
        default: null
      }
    },
    watch: {
    },
    mounted() {
      var that = this;
      this.rtcmConnection = new RTCMultiConnection();
      this.rtcmConnection.socketURL = this.socketURL;
      this.rtcmConnection.autoCreateMediaElement = false;
      this.rtcmConnection.enableLogs = this.enableLogs;
      this.rtcmConnection.session = {
        audio: this.enableAudio,
        video: this.enableVideo
      };
      this.rtcmConnection.sdpConstraints.mandatory = {
        OfferToReceiveAudio: this.enableAudio,
        OfferToReceiveVideo: this.enableVideo
      };
      if ((this.stunServer !== null) || (this.turnServer !== null)) {
        this.rtcmConnection.iceServers = []; // clear all defaults
      }
      if (this.stunServer !== null) {
        this.rtcmConnection.iceServers.push({
          urls: this.stunServer
        });
      }
      if (this.turnServer !== null) {
        var parse = this.turnServer.split('%');
        var username = parse[0].split('@')[0];
        var password = parse[0].split('@')[1];
        var turn = parse[1];
        this.rtcmConnection.iceServers.push({
          urls: turn,
          credential: password,
          username: username
        });
      }
      this.rtcmConnection.onstream = function (stream) {
        let found = that.videoList.find(video => {
          return video.id === stream.streamid
        })
        if (found === undefined) {
          let video = {
            id: stream.streamid,
            muted: stream.type === 'local'
          };
          that.videoList.push(video);
          if (stream.type === 'local') {
            that.localVideo = video;
          }
        }
        setTimeout(function(){ 
          for (var i = 0, len = that.$refs.videos.length; i < len; i++) {
            if (that.$refs.videos[i].id === stream.streamid)
            {
              that.$refs.videos[i].srcObject = stream.stream;
              break;
            }
          }
        }, 1000);
        
        that.$emit('joined-room', stream.streamid);
      };
      this.rtcmConnection.onstreamended = function (stream) {
        var newList = [];
        that.videoList.forEach(function (item) {
          if (item.id !== stream.streamid) {
            newList.push(item);
          }
        });
        that.videoList = newList;
        that.$emit('left-room', stream.streamid);
      };
      console.log(this.videoList)
    },
    methods: {
      stopVideo() {
          this.enableVideo = false
      },
      printer(item) {
        console.log(item)
      },
      join() {
        // 난수생성
         const newUuid = this.$uuid.v4()
         this.uuid = newUuid
         console.log(this.uuid)

         // 초대버튼 활성
         this.inviteButtonFlag = true

         var that = this;
         this.rtcmConnection.openOrJoin(this.roomId, function (isRoomExist, roomid) {
             console.log(roomid)
             console.log(isRoomExist,'----')
          if (isRoomExist === false && that.rtcmConnection.isInitiator === true) {
            that.$emit('opened-room', roomid);
          }
        });
      },
      leave() {
        // 초대버튼 비활성화
        this.inviteButtonFlag = false

        this.rtcmConnection.attachStreams.forEach(function (localStream) {
          localStream.stop();
        });
        this.videoList = [];
      },
      capture() {
        return this.getCanvas().toDataURL(this.screenshotFormat);
      },
      getCanvas() {
        let video = this.getCurrentVideo();
        if (video !== null && !this.ctx) {
          let canvas = document.createElement('canvas');
          canvas.height = video.clientHeight;
          canvas.width = video.clientWidth;
          this.canvas = canvas;
          this.ctx = canvas.getContext('2d');
        }
        const { ctx, canvas } = this;
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        return canvas;
      },
      getCurrentVideo() {
        if (this.localVideo === null) {
          return null;
        }
        for (var i = 0, len = this.$refs.videos.length; i < len; i++) {
          if (this.$refs.videos[i].id === this.localVideo.id)
            return this.$refs.videos[i];
        }
        return null;
      },
      shareScreen() {
        var that = this;
        if (navigator.getDisplayMedia || navigator.mediaDevices.getDisplayMedia) {
          function addStreamStopListener(stream, callback) {
            var streamEndedEvent = 'ended';
            if ('oninactive' in stream) {
                streamEndedEvent = 'inactive';
            }
            stream.addEventListener(streamEndedEvent, function() {
                callback();
                callback = function() {};
            }, false);
          }
          function onGettingSteam(stream) {
            that.rtcmConnection.addStream(stream);
            that.$emit('share-started', stream.streamid);
            addStreamStopListener(stream, function() {
              that.rtcmConnection.removeStream(stream.streamid);
              that.$emit('share-stopped', stream.streamid);
            });
          }
          function getDisplayMediaError(error) {
            console.log('Media error: ' + JSON.stringify(error));
          }
          if (navigator.mediaDevices.getDisplayMedia) {
            navigator.mediaDevices.getDisplayMedia({video: true, audio: false}).then(stream => {
              onGettingSteam(stream);
            }, getDisplayMediaError).catch(getDisplayMediaError);
          }
          else if (navigator.getDisplayMedia) {
            navigator.getDisplayMedia({video: true}).then(stream => {
              onGettingSteam(stream);
            }, getDisplayMediaError).catch(getDisplayMediaError);
          }
        }
      }
    }
  };
</script>
<style scoped>
  .video-list {
    background: whitesmoke;
    height: auto;
  }
    .video-list div {
      padding: 0px;
    }
  .video-item {
    background: #c5c4c4;
    display: inline-block;
  }
</style>

```





- WebCam2.vue

```javascript
<template>
  <div class="container">
    <div class="row">
      <div class="col-md-12 my-3">
        <h2>Room</h2>
        <input v-model="roomId">
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <div class="">
          <vue-webrtc ref="webrtc"
                      width="100%"
                      :roomId="roomId"
                      v-on:joined-room="logEvent"
                      v-on:left-room="logEvent"
                      v-on:opened-room="logEvent"
                      v-on:share-started="logEvent"
                      v-on:share-stopped="logEvent"
                      @error="onError" />
        </div>
        <div class="row">
          <div class="col-md-12 my-3">
            <button type="button" class="btn btn-primary" @click="onJoin">Join</button>
            <button type="button" class="btn btn-primary" @click="onLeave">Leave</button>
            <button type="button" class="btn btn-primary" @click="onCapture">Capture Photo</button>
            <button type="button" class="btn btn-primary" @click="onShareScreen">Share Screen</button>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <h2>Captured Image</h2>
        <figure class="figure">
          <img :src="img" class="img-responsive" />
        </figure>
      </div>
    </div>
  </div>
</template>

<script>
  import Vue from 'vue'
  import { WebRTC } from 'plugin';
  import { find, head } from 'lodash';
//   Vue.component(WebRTC.name, WebRTC);
  export default {
    name: 'WebRTC',
    components: {
    },
    data() {
      return {
        img: null,
        roomId: "public-room"
      };
    },
    computed: {
    },
    watch: {
    },
    methods: {
      onCapture() {
        this.img = this.$refs.webrtc.capture();
      },
      onJoin() {
        this.$refs.webrtc.join();
      },
      onLeave() {
        this.$refs.webrtc.leave();
      },
      onShareScreen() {
        this.img = this.$refs.webrtc.shareScreen();
      },
      onError(error, stream) {
        console.log('On Error Event', error, stream);
      },
      logEvent(event) {
        console.log('Event : ', event);
      },
    }
  };
</script>
```





- WebCam3.vue

```javascript
<template>
    <div class="container">
        <div class="row">
          <div class="col-md-12 my-3">
            <button type="button" class="btn btn-primary" @click="join">Join</button>
            <button type="button" class="btn btn-primary" @click="leave">Leave</button>
            <button type="button" class="btn btn-primary" @click="capture">Capture Photo</button>
            <button type="button" class="btn btn-primary" @click="shareScreen">Share Screen</button>
            <!-- <button type="button" class="btn btn-primary" @click="getCanvas">Get Canvas</button> -->
            <button type="button" class="btn btn-primary" @click="stopVideo">Stop Video</button>
          </div>
        </div>
        <div class="video-list" >
            <div v-for="item in videoList"
                v-bind:video="item"
                v-bind:key="item.id"
                class="video-item">
                <video controls autoplay playsinline ref="videos" :height="cameraHeight" :muted="item.muted" :id="item.id"></video>
            </div>
        </div>
    </div>
</template>

<script>
  import RTCMultiConnection from 'rtcmulticonnection';
  require('adapterjs');
  export default {
    name: 'vue-webrtc',
    components: {
      RTCMultiConnection
    },
    data() {
      return {
        rtcmConnection: null,
        localVideo: null,
        videoList: [],
        canvas: null,
      };
    },
    props: {
      roomId: {
        type: String,
        default: 'public-room'
      },
      socketURL: {
        type: String,
        default: 'https://rtcmulticonnection.herokuapp.com:443/'
      },
      cameraHeight: {
        type: [Number, String],
        default: 160
      },
      autoplay: {
        type: Boolean,
        default: true
      },
      screenshotFormat: {
        type: String,
        default: 'image/jpeg'
      },
      enableAudio: {
        type: Boolean,
        default: true
      },
      enableVideo: {
        type: Boolean,
        default: true
      },
      enableLogs: {
        type: Boolean,
        default: false
      },
      stunServer: {
        type: String,
        default: null
      },
      turnServer: {
        type: String,
        default: null
      }
    },
    watch: {
    },
    mounted() {
      var that = this;
      this.rtcmConnection = new RTCMultiConnection();
      this.rtcmConnection.socketURL = this.socketURL;
      this.rtcmConnection.autoCreateMediaElement = false;
      this.rtcmConnection.enableLogs = this.enableLogs;
      this.rtcmConnection.session = {
        audio: this.enableAudio,
        video: this.enableVideo
      };
      this.rtcmConnection.sdpConstraints.mandatory = {
        OfferToReceiveAudio: this.enableAudio,
        OfferToReceiveVideo: this.enableVideo
      };
      if ((this.stunServer !== null) || (this.turnServer !== null)) {
        this.rtcmConnection.iceServers = []; // clear all defaults
      }
      if (this.stunServer !== null) {
        this.rtcmConnection.iceServers.push({
          urls: this.stunServer
        });
      }
      if (this.turnServer !== null) {
        var parse = this.turnServer.split('%');
        var username = parse[0].split('@')[0];
        var password = parse[0].split('@')[1];
        var turn = parse[1];
        this.rtcmConnection.iceServers.push({
          urls: turn,
          credential: password,
          username: username
        });
      }
      this.rtcmConnection.onstream = function (stream) {
        let found = that.videoList.find(video => {
          return video.id === stream.streamid
        })
        if (found === undefined) {
          let video = {
            id: stream.streamid,
            muted: stream.type === 'local'
          };
          that.videoList.push(video);
          if (stream.type === 'local') {
            that.localVideo = video;
          }
        }
        setTimeout(function(){ 
          for (var i = 0, len = that.$refs.videos.length; i < len; i++) {
            if (that.$refs.videos[i].id === stream.streamid)
            {
              that.$refs.videos[i].srcObject = stream.stream;
              break;
            }
          }
        }, 1000);
        
        that.$emit('joined-room', stream.streamid);
      };
      this.rtcmConnection.onstreamended = function (stream) {
        var newList = [];
        that.videoList.forEach(function (item) {
          if (item.id !== stream.streamid) {
            newList.push(item);
          }
        });
        that.videoList = newList;
        that.$emit('left-room', stream.streamid);
      };
    },
    methods: {
      stopVideo() {
          this.enableVideo = false
      },
      join() {
         var that = this;
         this.rtcmConnection.openOrJoin(this.roomId, function (isRoomExist, roomid) {
          if (isRoomExist === false && that.rtcmConnection.isInitiator === true) {
            that.$emit('opened-room', roomid);
          }
        });
      },
      leave() {
        this.rtcmConnection.attachStreams.forEach(function (localStream) {
          localStream.stop();
        });
        this.videoList = [];
      },
      capture() {
        return this.getCanvas().toDataURL(this.screenshotFormat);
      },
      getCanvas() {
        let video = this.getCurrentVideo();
        if (video !== null && !this.ctx) {
          let canvas = document.createElement('canvas');
          canvas.height = video.clientHeight;
          canvas.width = video.clientWidth;
          this.canvas = canvas;
          this.ctx = canvas.getContext('2d');
        }
        const { ctx, canvas } = this;
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        return canvas;
      },
      getCurrentVideo() {
        if (this.localVideo === null) {
          return null;
        }
        for (var i = 0, len = this.$refs.videos.length; i < len; i++) {
          if (this.$refs.videos[i].id === this.localVideo.id)
            return this.$refs.videos[i];
        }
        return null;
      },
      shareScreen() {
        var that = this;
        if (navigator.getDisplayMedia || navigator.mediaDevices.getDisplayMedia) {
          function addStreamStopListener(stream, callback) {
            var streamEndedEvent = 'ended';
            if ('oninactive' in stream) {
                streamEndedEvent = 'inactive';
            }
            stream.addEventListener(streamEndedEvent, function() {
                callback();
                callback = function() {};
            }, false);
          }
          function onGettingSteam(stream) {
            that.rtcmConnection.addStream(stream);
            that.$emit('share-started', stream.streamid);
            addStreamStopListener(stream, function() {
              that.rtcmConnection.removeStream(stream.streamid);
              that.$emit('share-stopped', stream.streamid);
            });
          }
          function getDisplayMediaError(error) {
            console.log('Media error: ' + JSON.stringify(error));
          }
          if (navigator.mediaDevices.getDisplayMedia) {
            navigator.mediaDevices.getDisplayMedia({video: true, audio: false}).then(stream => {
              onGettingSteam(stream);
            }, getDisplayMediaError).catch(getDisplayMediaError);
          }
          else if (navigator.getDisplayMedia) {
            navigator.getDisplayMedia({video: true}).then(stream => {
              onGettingSteam(stream);
            }, getDisplayMediaError).catch(getDisplayMediaError);
          }
        }
      }
    }
  };
</script>
<style scoped>
  .video-list {
    background: whitesmoke;
    height: auto;
  }
    .video-list div {
      padding: 0px;
    }
  .video-item {
    background: #c5c4c4;
    display: inline-block;
  }
</style>

```

