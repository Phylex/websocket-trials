#!/usr/bin/python3

# WS client example

import asyncio
import sys
import websockets

async def hallo():
    uri = f"ws://192.168.205.140:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What is your name?")
        await websocket.send(name)
        print(f"> {name}")
        greeting = await websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hallo())
