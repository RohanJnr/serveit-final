const WebSocket = require('ws');

const ws_fetch_stream = new WebSocket('http://127.0.0.1:8000/ws/fetch_stream');
const ws_cmd = new WebSocket('http://127.0.0.1:8000/ws/cmd');

ws_cmd.on('open', function open() {
  ws_cmd.send('something');
});

ws_cmd.on('message', function incoming(data) {
  console.log("here")
});


setInterval(() => {
  ws_cmd.send("hello, a message again")
  }, 2000
)