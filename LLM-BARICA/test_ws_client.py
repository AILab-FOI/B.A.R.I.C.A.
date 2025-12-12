import asyncio
import websockets

async def main():
    uri = "ws://localhost:8766"
    async with websockets.connect(uri) as websocket:
        msg = "Ovo je dummy tekst za TTS."
        print("Sending:", msg)
        await websocket.send(msg)

asyncio.run(main())
