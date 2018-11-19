from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api

login, password = 'login', 'password'
vk_session = vk_api.VkApi(login, password)
try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)


def write_msg(user_id, s):
    vk_session.method('messages.send', {'user_id': user_id, 'message': s})


longpoll = VkLongPoll(vk_session)
user_id = #integer id

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.from_chat and event.chat_id == 72:
        write_msg(user_id, event.text)
