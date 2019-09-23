from bot import write_msg, parser_slow, pogoda, uploadMP3onSERVER,keyboard_
from sating import primer,lang


def name(vk, event, text):
    vk.method("messages.editChat", {"peer_id": event.object.peer_id, "title": text})

def ban(vk, event):
    vk.method("", {"peer_id": event.object.peer_id})

def unban(vk, event,id_):
    vk.method("messages.addChatUser", {"peer_id": event.object.peer_id, "user_id": id_})

def delete(vk, event):
    vk.method("", {"peer_id": event.object.peer_id})

def Members(vk, event):
    vk.method("", {"peer_id": event.object.peer_id})
