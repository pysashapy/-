from bot import write_msg, parser_slow, pogoda, uploadMP3onSERVER,keyboard_
from sating import primer,lang,lang1

def help_(vk, primer, id, keyboard):
    write_msg(session=vk, id=id, text=primer, keyboard=keyboard)

def pogoda_(vk, text, id, keyboard,peer):
    z = pogoda(text[peer+1:])  # погода
    write_msg(session=vk, id=id, text=z, keyboard=keyboard)

def perevod_(vk, text, id, keyboard,peer):
    a = None
    t = ""
    try:
        t+="1"
        if text[peer+1].lower() == "audio":
            t+="3"
            z = parser_slow(text[peer+2:], text[peer].lower())
            a = uploadMP3onSERVER(vk=vk, id=id, text=z, LANG=text[peer].lower())
            write_msg(session=vk, id=id, text="Перевод: " + z, keyboard=keyboard, document=a)
        else:
            t+="2"
            z = parser_slow(text[peer+1:], text[peer].lower())
            write_msg(session=vk, id=id,
                      text="Перевод: " + z, keyboard=keyboard,
                      document=a)
    except:
        z = parser_slow(text[1:], text[peer].lower())
        write_msg(session=vk, id=id,
                  text="Перевод: " + z + "\nЕщё не могу говорить на этом  языке", keyboard=keyboard, document=a)

def lang_(vk, lang, id, keyboard):
    write_msg(session=vk, id=id, text=lang, keyboard=keyboard)

def main(vk, event,peer,qw=0):

    obj = event.object
    text = event.object.text.split()
    id = obj.peer_id

    if text[peer].lower() == "помощь" :
        help_(vk, primer, id, keyboard_())
    elif text[peer].lower() == "погода":
        pogoda_(vk, text, id, keyboard_(),peer)
    elif len(text[peer]) == 3 or len(text[peer]) == 2:  # переводчик
        for i in range(len(lang1)):
            if lang1[i] == text[peer].lower():
                perevod_(vk, text, id, keyboard_(),peer)

    elif text[peer].lower() == "доступные":
        lang_(vk, lang, id, keyboard_())
