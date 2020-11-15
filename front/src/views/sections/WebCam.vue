<template>
  <div class="container">
      <div><br>
          <base-section-heading title="화상회의" />
      </div>
      
      <div class="video-list" >
            <div v-for="item in videoList"
                v-bind:video="item"
                v-bind:key="item.id"
                class="video-item">
                <video controls autoplay playsinline ref="videos" v-if="localVideo.id === item.id" height="500" :muted="item.muted" :id="item.id" @click="printer(item)"></video>
                <video controls autoplay playsinline ref="videos" v-else :height="cameraHeight" :muted="item.muted" :id="item.id" @click="printer(item)"></video>
                <p>{{ item.id }}</p>
            </div>
        </div>
        <div class="row d-flex justify-center">
            <div class="my-3">
                <!-- 여기 나중에 버튼 컴포넌트 호출 -->
                <v-btn @click="invite">초대하기</v-btn>
                <v-btn @click="leave">종료</v-btn>
                <v-btn @click="shareScreen">화면공유</v-btn>
            </div>
        </div>
        <!-- <v-button @click="changeUserId">닉네임변경</v-button> -->
  </div>
</template>

<script>
import RTCMultiConnection from 'rtcmulticonnection';
import { uuid } from 'vue-uuid';
import axios from 'axios'
import constants from '@/api/constants.js'
require('adapterjs');

export default {
    name: "WebCam",
    components: {
    },
    data () {
        return {
            rtcmConnection: null,
            localVideo: null,
            videoList: [],
            canvas: null,
            roomId: 'public-room',
            constants,
        }
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
    created() {
        // this.roomId = this.$route.query.uuid
        // console.log(this.roomId)
    },
     mounted() {
        // console.log('webcam1')
        this.rtcmConnection = new RTCMultiConnection();
        // console.log('webcam2')
        this.rtcmConnection.socketURL = this.socketURL;
        this.rtcmConnection.autoCreateMediaElement = false;
        this.rtcmConnection.enableLogs = this.enableLogs;
        this.rtcmConnection.session = {
            audio: this.enableAudio,
            video: this.enableVideo
        };

        // // 닉네임 변경 실험
        // let today = new Date()
        // var tempUserId = today.getSeconds();
        // console.log(tempUserId)
        // this.rtcmConnection.changeUserId(tempUserId, function() {
        //     alert('닉변됨' + rtcmConnection.userid)
        // })

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
        
        // 난수생성
        if ($cookies.isKey('roomID')) {
            this.roomId = $cookies.get('roomID')
        } else {
            const newUuid = this.$uuid.v4()
            this.roomId = newUuid
            $cookies.set('roomID', this.roomId )
            // const data = {
            //     'program_id': 1, // 나중에 program의 id를 받아와서 넣어주면 돼
            //     webRtcroomId : this.roomId
            // }
            // axios.post(`${constants.API_URL}api/trainer/program/online/`, data)
            // .then((res)=>{
            //     this.roomId = res.data.data
            //     $cookies.set('roomID', this.roomId )
            // })
        }
        // if ($cookies.isKey('roomID') === false) {
        //     $cookies.set('roomID', newUuid)
        // }
        // join code
        var that = this;
        this.rtcmConnection.openOrJoin(this.roomId, function (isRoomExist, roomid) {
            if (isRoomExist === false && that.rtcmConnection.isInitiator === true) {
                that.$emit('opened-room', roomid);
            }
        })
    },
    methods: {
        invite() {
        },
        leave() {
            $cookies.remove('roomID')
            alert('수업이 종료되었습니다.')
            this.$router.push({ name: 'Home' })
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
                    // console.log('Media error: ' + JSON.stringify(error));
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
        },
        printer(item) {
            // console.log(item)
        },
        changeUserId() {
            
        }
    },
    destroyed(){
        // console.log('사라졌어요')
        this.rtcmConnection.attachStreams.forEach(function (localStream) {
        localStream.stop();
        });
    }
}
</script>

<style>

</style>