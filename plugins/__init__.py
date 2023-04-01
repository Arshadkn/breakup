from aiohttp import web
from .route import routes
from pyrogram import Client
import pyromod.listen
from info import API_ID, API_HASH, BOT_TOKEN
from os import getcwd


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

Client = Client(
    name='Web Streamer',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    sleep_threshold=5,
    workers=50
)

multi_clients = {}
work_loads = {}
