#!/usr/bin/python3

# WS client example

import asyncio
import websockets

async def hallo(ip, port):
    uri = f"ws://{ip}:{port}"
    async with websockets.connect(uri) as websocket:
        name = input("What is your name?")
        await websocket.send(name)
        print(f"> {name}")
        greeting = await.websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hallo())
