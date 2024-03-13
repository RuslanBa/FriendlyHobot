# from aiogram import types
# from loader import bot
#
#
# msg_id = []     # message for deleting when new message come
#
#
# async def delete_dialog(message: types.Message):
#     if msg_id:
#         for id_messages in msg_id:
#             await bot.delete_message(message.from_user.id, message_id=int(id_messages))
#         msg_id.clear()
#         print('msg_id cleaned and now is - ', msg_id)
#     else:
#         print("can't clean msg_id - it is clean")
