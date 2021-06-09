const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8080 });


const connections = {
    cam_stream: null,
    cam_cmd: null,
    client: null
}


wss.on('connection', function connection(ws) {

  ws.on('message', function incoming(message) {
    console.log("a new message")
    if (!connections.client || !connections.cam_stream){

        if (message === "cam_stream_password"){
            connections.cam_stream = ws   
            console.log("cam_stream_password")     
        } else if (message === "cam_cmd_password") {
            connections.cam_cmd = ws
            console.log("cam_cmd_password")
        } else if (message === "client_password") {
            console.log("CLIENT_CONNECTED")
            connections.client = ws
            connections.cam_stream.send("CLIENT_CONNECTED")
        }
    }
    else{
        message = JSON.parse(message)

        const method = message.method
        console.log(method)
        if (method === "stream"){
            connections.client.send(message.frame)
        }
    
        else if (method === "command") {
            console.log(message.cmd)
            if (connections.cam_cmd){
                connections.cam_cmd.send(message.cmd)
            }
        }
    }
   
    });

});