import websocket
import json
import base64
import _thread as thread
import cv2

def send_frame(ws):
    capture = cv2.VideoCapture(0)

    while capture.isOpened():
        _, frame = capture.read()
        _, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = base64.b64encode(buffer).decode()
        res = {
            "method": "stream",
            "frame": jpg_as_text
        }

        ws.send(json.dumps(res))

        if cv2.waitKey(100)==ord('q'):
            cv2.destroyAllWindows()        
            break

    capture.release()

def on_message(ws, message):
    print("A new message")
    if message == "CLIENT_CONNECTED":
        send_frame(ws)


def on_error(ws, error):
    print("error")

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        ws.send("cam_stream_password")
    thread.start_new_thread(run, ())

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "ws://localhost:8080",
        on_open = on_open,
        on_message = on_message,
        on_error = on_error,
        on_close = on_close
)

    ws.run_forever()