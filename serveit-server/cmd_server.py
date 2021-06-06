import base64
from pathlib import Path

import cv2
# import serial
from fastapi import FastAPI, WebSocket

# ACCEPTED_COMMANDS = {
#     "w": "f",
#     "s": "b",
#     "a": "l",
#     "d": "r"
# }
# ser = serial.Serial('/dev/ttyACM0', 9600) # Establish the connection on a specific port

app = FastAPI()


@app.websocket("/ws/cmd")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(data)
        # if data in ACCEPTED_COMMANDS:
        #     await websocket.send_text("Received.")
        #     # ser.write(data.encode())
        # else:
        #     await websocket.send_text("Invalid command,")