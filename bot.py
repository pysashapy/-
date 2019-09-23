from sating import *
from bs4 import BeautifulSoup
from gtts import gTTS
import requests,json, os, time
from random import randint

def write_msg(session, id, text= None, keyboard= None, document= None):
    randint1 = randint(0, 99999999)
    return session.method("messages.send", {"peer_id": id, "message": text, 'attachment': document, "random_id": randint1, "keyboard": keyboard})

def write_post(session, id, text="1"):
    return session.method("wall.post", {"owner_id": id, "message": text})

def get_album(session,id,ids=None):
    return session.method("photos.getAlbums",{"owner_id":id,"album_ids":ids})

def pogoda(city):
    cit = ""
    for i in city:
        cit+=i+"-"
    s = requests.get('https://sinoptik.com.ru/погода-' + cit[:-1])
    b = BeautifulSoup(s.text, "html.parser")
    p3 = b.select('.temperature .p3')
    pogoda1 = p3[0].getText()
    p4 = b.select('.temperature .p4')
    pogoda2 = p4[0].getText()
    p5 = b.select('.temperature .p5')
    pogoda3 = p5[0].getText()
    p6 = b.select('.temperature .p6')
    pogoda4 = p6[0].getText()
    p = b.select('.rSide .description')
    pogoda = p[0].getText().strip()
    z = str('Утром :' + pogoda1 + ' ' + pogoda2 + "\n" + \
            'Днём :' + pogoda3 + ' ' + pogoda4 + "\n\n" + \
            pogoda)
    return z

def fail1(text):
    r = ""
    for i in text:
        r+=i+" "
    return r

def parser_slow(text,ru):
    text = fail1(text)
    url = "https://translate.yandex.net/api/v1.5/tr.json/translate?key={0}&text={1}&lang={2}".format(token1,text,ru)
    response = requests.get(url).json()["text"]
    return fail1(response)[:-1]

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

def uploadMP3onSERVER(vk, id, text, LANG):
    url = vk.method('docs.getMessagesUploadServer', {'type': 'audio_message', "peer_id": id})['upload_url']  # получаем ссылку для загрузки файла
    tts = gTTS(text=text, lang=LANG)
    name = str(int(time.time())) + ".mp3"
    tts.save(name)
    file = open(name, 'rb')
    files = [('file', (name, file))]
    url_2 = requests.post(url , files=files).text
    file.close()
    os.remove(name)
    RESPONSE = json.loads(url_2)['file']
    RESPONSE2 = vk.method('docs.save',{'file': RESPONSE })
    id = RESPONSE2["audio_message"]["id"]
    owner_id = RESPONSE2["audio_message"]["owner_id"]
    document = 'doc%s_%s' % (str(owner_id), str(id))
    return document

def keyboard_():
    keyboard = {
        "one_time": False,
        "buttons": [
            [get_button(label="Доступные языки", color="positive")],
            [get_button(label="Помощь", color="positive")],
        ]
    }

    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard1 = str(keyboard.decode('utf-8'))
    return keyboard1
