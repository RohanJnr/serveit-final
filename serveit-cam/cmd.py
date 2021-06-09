import websocket
import _thread as thread


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print("error")

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        ws.send("cam_cmd_password")
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