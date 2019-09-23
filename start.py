from sating import *
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import vk_api, people, time
time_ = time.time()
def loop(vk_session, longpoll):
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            obj = event.object
            id = obj.peer_id
            text = event.object.text.split()
            if id >= 2000000000:             #беседа
                if text[1][0] == "/":
                    pass
                else:
                    people.main(vk_session, event, 1)
            else:
                people.main(vk_session, event, 2)
if __name__ == '__main__':
    vk = vk_api.VkApi(token=token)
    print("""--------------------------\n««««««<Start bot...»»»»»»>\n--------------------------""")
    try: loop(vk, VkBotLongPoll(vk, group_id))
    except KeyboardInterrupt:
        print("""--------------------------\n««««««<Break bot...»»»»»»>\n--------------------------""")
    except: loop(vk, VkBotLongPoll(vk, group_id))