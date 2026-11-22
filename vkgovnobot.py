import vk_api
import  random
from vk_api.longpoll import VkLongPoll, VkEventType
import os
from dotenv import load_dotenv

TOKEN = os.getenv("TOKEN")
vk_session = vk_api.VkApi(token=TOKEN)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.from_user:
            vk.messages.send(user_id=event.user_id, message=event.text, random_id=random.randint(1,10000))