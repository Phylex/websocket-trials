#!/usr/bin/python3
# WebSocket Server example
import asyncio
import websockets

async def hallo(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")
    greeting = f"< Hello {name}"
    await websocket.send(greeting)
    print(f"> {greeting}")

server = websockets.serve(hello, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
