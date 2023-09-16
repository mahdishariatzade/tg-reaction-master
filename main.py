import threading

from pyrogram import filters, idle
from pyrogram.enums import ChatType

from client import app
from config import REACT_EMOJI
from functions.react_in_history import react_in_chat_history

app.start()
dialogs = []
for dialog in app.get_dialogs(100):
    if dialog.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        print(f"{len(dialogs) + 1}-", dialog.chat.first_name or dialog.chat.title)
        dialogs.append(dialog.chat.id)

selected_group = int(input('select a group:')) - 1
selected_group_id = dialogs[selected_group]

members = list(app.get_chat_members(selected_group_id))
for count, member in enumerate(members, 1):
    name = f"{member.user.first_name} {member.user.last_name}" if member.user.last_name else f"{member.user.first_name}"
    print(f"{count}- {name}")

selected_member = int(input('select a member:')) - 1
selected_member_id = members[selected_member].user.id

# scheduler = BackgroundScheduler()
# scheduler.add_job(react_in_chat_history, args=(selected_group_id, [selected_member_id], REACT_EMOJI, app),
#                   trigger='cron', hour=datetime.datetime.now().hour, second=datetime.datetime.now().second + 2)

history = threading.Thread(target=react_in_chat_history,
                           args=(selected_group_id, [selected_member_id], REACT_EMOJI, app))


@app.on_message(
    filters.chat(selected_group_id) &
    filters.user(selected_member_id)
)
async def react(_, message):
    try:
        await message.react(emoji=REACT_EMOJI)
    except Exception as e:
        print(e)


history.start()
idle()
