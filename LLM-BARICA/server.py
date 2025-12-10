from dotenv import load_dotenv
import os
import asyncio
import websockets
from llmHelper import ask_foi_llm, dummy_foi_response


load_dotenv()


WS_HOST = os.getenv("WS_HOST")
WS_PORT = int(os.getenv("WS_PORT"))


# WS_HOST = os.getenv("WS_HOST", "localhost")
# WS_PORT = int(os.getenv("WS_PORT", 8766))

async def handle_client(websocket):
    async for message in websocket:
        print(f": {message}")

        try:
            answer = ask_foi_llm(message)
            print(f"LLM response: {answer}") 
        except Exception as e:
            print(dummy_foi_response())
            print(f"Error in LLM: {e}")

async def main():
    async with websockets.serve(handle_client, WS_HOST, WS_PORT):
        print(f"LLM server running on ws://{WS_HOST}:{WS_PORT}")
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())