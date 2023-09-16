from pyrogram.enums import ChatType

from client import app

app.start()
for count, dialog in enumerate(app.get_dialogs(20)):
    if dialog.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        print(count + 1, dialog.chat.first_name or dialog.chat.title, dialog.chat.id)

# for member in app.get_chat_members("-1001678716086"):
#     print(f'name: {member.user.first_name} {member.user.last_name} id: {member.user.id}')
# @app.on_message()
# async def react(_, message:Message):
#     print(f'title: {message.chat.title}\n',
#           f'chat_id: {message.chat.id}\n',
#           f'name: {message.from_user.first_name if message.from_user.first_name else None}',
#           f'id: {message.from_user.id if message.from_user.id else None}')


# app.run()
