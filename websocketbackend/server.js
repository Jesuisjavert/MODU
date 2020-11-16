
var fs = require('fs'); 
var app = require('express')(); 
var https  = require('https');
const path = require('path'); 
var server = https.createServer({ 
    ca: fs.readFileSync('/etc/letsencrypt/live/k3c202.p.ssafy.io/fullchain.pem'),
    key: fs.readFileSync(path.resolve(process.cwd(), '/etc/letsencrypt/live/k3c202.p.ssafy.io/privkey.pem'), 'utf8').toString(),
    cert: fs.readFileSync(path.resolve(process.cwd(), '/etc/letsencrypt/live/k3c202.p.ssafy.io/cert.pem'), 'utf8').toString(),
    requestCert: false, 
    rejectUnauthorized: false 
},app);

// var app = require('express')()
// var server = require('http').createServer(app)



var io = require('socket.io')(server,{
    pingTimeout: 1000,
});


app.all('/*', function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
    next();
});

// localhost:3000서버에 접속하면 클라이언트로 메세지을 전송한다
app.get('/', function(req, res) {
    res.sendFile('Hellow Chating App Server');
});

//connection event handler
io.on('connection' , function(socket) {
    console.log('Connect from Client: '+socket)
    console.log(Object.keys(socket))

    socket.on('hello', function(data){
        console.log('hello from Client: '+data)
    });
    socket.on('join',(roomId,username)=>{
        socket.join(roomId,()=>{
            io.to(roomId).emit('join')
        })
    })
    socket.on('chat', (roomId,username,message,time)=>{
        console.log(roomId,username,message)
        console.log(socket.rooms)
        socket.broadcast.to(roomId).emit('chat',{
            username: username,
            message : message,
            time : time
        })

    });


})

server.listen(3000, function() {
    console.log('socket io server listening on port 3000')
})
