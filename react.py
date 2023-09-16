import random

from client import app
from config import victim_ids, group_ids, REACT_EMOJI, max_reaction
from alive_progress import alive_bar
from time import sleep
import warnings

warnings.filterwarnings("ignore")

app.start()
if not (victim_ids or group_ids):
    raise Exception('You have to pass both VICTIM_USER_IDS and VICTIM_GROUP_IDS env variables')

number = 0
with alive_bar(max_reaction, force_tty=True, dual_line=False) as bar:
    for msg in app.get_chat_history(group_ids):
        if msg.from_user is None:
            pass
        elif msg.from_user.id in victim_ids:
            try:
                msg.react(REACT_EMOJI, True)
                bar.text = 'WORKING'
                bar()
            except:
                print('error')
            sleep(random.uniform(0, 2))
            number += 1
            if number >= max_reaction:
                break

# @app.on_message(
#     filters.chat(list(map(int, group_ids.split(',')))) &
#     filters.user(list(map(int, victim_ids.split(','))))
# )
# async def react(_, message):
#     try:
#         await message.react(emoji=REACT_EMOJI)
#     except Exception as e:
#         print(e)

# app.run()
