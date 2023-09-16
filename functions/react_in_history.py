import math
import random
from time import sleep

from pyrogram.errors import FloodWait


def react_in_chat_history(chat_id, user_id: list, react_emoji, app, limit=math.inf):
    reacted_messages = 0
    for msg in app.get_chat_history(chat_id):
        if reacted_messages >= limit:
            print('job ended')
            break
        # if msg.chat.type in [ChatType.CHANNEL, ChatType.GROUP, ChatType.SUPERGROUP]:
        #     continue
        if msg.sender_chat:
            continue
        if msg.from_user.id not in user_id:
            continue
        try:
            msg.react(react_emoji, True)
            sleep(random.uniform(0, 2))
            reacted_messages += 1
        except FloodWait as e:
            sleep(e.value)
        except Exception as e:
            print(e)
