#!/usr/bin/env python3

import asyncio
from websockets import serve


async def connection_handler(websocket):
    while True:
        message = await websocket.recv()
        await websocket.send(message)


async def main():
    async with serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
