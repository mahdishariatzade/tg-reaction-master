from pyrogram import Client
from config import API_ID, API_HASH
import os


api_id = API_ID
api_hash = API_HASH
proxy = {
     "scheme": "socks5",  # "socks4", "socks5" and "http" are supported
     "hostname": "127.0.0.1",
     "port": 10808,
 }


if not (api_id or api_hash):
    raise Exception('You have to pass both API_ID and API_HASH env variables')

app = Client("auto-reaction",
             api_id,
             api_hash,
             proxy=proxy)
