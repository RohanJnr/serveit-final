import asyncio
import base64
from pathlib import Path

import cv2
import websockets

loop = asyncio.get_event_loop()


async def send_frame(websocket):
    p = Path("resources", "sample.mp4")
    capture = cv2.VideoCapture(0)

    while capture.isOpened():
        _, frame = capture.read()
        _, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = base64.b64encode(buffer).decode()
        try:
            await websocket.send(jpg_as_text)
            await asyncio.sleep(0.1)
        except websockets.exceptions.ConnectionClosedError:
            print("Closed")
            break

        if cv2.waitKey(100)==ord('q'):
            cv2.destroyAllWindows()        
            break

    capture.release()

async def handle_messages(websocket):
    try:
        async for message in websocket:
            print(message)
            await websocket.send("Hello")

    except websockets.exceptions.ConnectionClosedError:
        print("Closed")

async def echo(websocket, path):
    await send_frame(websocket)
    

loop.run_until_complete(
    websockets.serve(echo, 'localhost', 9000))
loop.run_forever()
