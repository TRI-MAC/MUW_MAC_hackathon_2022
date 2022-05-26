import asyncio
import websockets

async def test():
    async with websockets.connect("ws://192.168.75.51/websocket", subprotocols=["g3api"]) as websocket:
        await websocket.send("{'path':'rudimentary:gaze','id':12,'method':'POST','body':null}")
        while True:
            try:
                message = await websocket.recv()
                print('Received: ' + str(message))
            except websockets.exceptions.ConnectionClosed:
                print('Connection with server closed')
                break

asyncio.run(test())
