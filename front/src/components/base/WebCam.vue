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
        <!-- 초기설정 -->
        <!-- <div class="video-list" >
            <div v-for="item in videoList"
                v-bind:video="item"
                v-bind:key="item.id"
                class="video-item">
                <video controls autoplay playsinline ref="videos" :height="cameraHeight" :muted="item.muted" :id="item.id" @click="printer(item)"></video>
            </div>
        </div> -->
        <!-- 나만 작은화면 -->
        <!-- <div class="video-list" >
            <div v-for="item in videoList"
                v-bind:video="item"
                v-bind:key="item.id"
                class="video-item">
                <video controls autoplay playsinline ref="videos" v-if="localVideo.id === item.id" height="100" :muted="item.muted" :id="item.id" @click="printer(item)"></video>
                <video controls autoplay playsinline ref="videos" v-else :height="cameraHeight" :muted="item.muted" :id="item.id" @click="printer(item)"></video>
            </div>
        </div> -->
        <!-- 선택하면 캐로젤실험 전 값 -->
        <!-- <div class="video-list" >
            <div v-for="item in videoList"
                v-bind:video="item"
                v-bind:key="item.id"
                class="video-item">
                <video controls autoplay playsinline ref="videos" v-if="localVideo.id === item.id" height="100" :muted="item.muted" :id="item.id" @click="printer(item)"></video>
            </div>
        </div>
        <div class="select-video">
            <div v-for="item in videoList"
                v-bind:video="item"
                v-bind:key="item.id"
                class="video-item">
                <video controls autoplay playsinline ref="videos" v-if="localVideo.id !== item.id" height="100" :muted="item.muted" :id="item.id" @click="printer(item)"></video>
            </div>
        </div> -->
        <!-- 캐로젤 실험 -->
        <!-- <div class="video-list" >
            <div v-for="item in videoList"
                v-bind:video="item"
                v-bind:key="item.id"
                class="video-item">
                <video controls autoplay playsinline ref="videos" v-if="selectCam === item.id" height="500" :muted="item.muted" :id="item.id" @click="printer(item)"></video>
            </div>
        </div>
        <div class="select-video">
            <div v-for="item in videoList"
                v-bind:video="item"
                v-bind:key="item.id"
                class="video-item">
                <video controls autoplay playsinline ref="videos" v-if="selectCam !== item.id" height="100" :muted="item.muted" :id="item.id" @click="printer(item)"></video>
            </div>
        </div> -->
        <!-- 케로젤 실험2 -->
        <div class="video-list" >
            <div v-for="item in videoList"
                v-bind:video="item"
                v-bind:key="item.id"
                class="video-item">
                <video controls autoplay playsinline ref="videos" v-if="selectCam === item.id" height="500" :muted="item.muted" :id="item.id" @click="printer(item)"></video>
                <video controls autoplay playsinline ref="videos" v-else height="100" :muted="item.muted" :id="item.id" @click="printer(item)"></video>
            </div>
        </div>
        <WebCreateBtn>시작하기</WebCreateBtn>
        <WebJoinBtn>입장하기</WebJoinBtn>
        <CamSlider></CamSlider>
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
      WebJoinBtn: () => import('@/components/base/WebJoinBtn'),
      CamSlider: () => import('@/components/base/CamSlider'),
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
        selectCam: null,
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
      if (this.videoList.length > 0) {
        this.selectCam = this.videoList[0].id
        console.log(this.selectCam)
      }
    },
    watch: {
      videoList: function() {
        if (this.selectCam === null) {
          this.selectCam = this.videoList[0].id
          // console.log('비디오리스트1번', this.selectCam)
        }
      }
    },
    methods: {
      stopVideo() {
          this.enableVideo = false
      },
      printer(item) {
        this.selectCam = item.id
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
