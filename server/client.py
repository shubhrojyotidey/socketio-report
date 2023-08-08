import asyncio

import socketio

sio_client = socketio.AsyncClient()


@sio_client.event
async def connect():
    print('Connected!')


@sio_client.event
async def disconnect():
    print('Disconnected!')


async def main():
    await sio_client.connect(url='http://localhost:8000', socketio_path='sockets')
    await sio_client.disconnect()

asyncio.run(main())