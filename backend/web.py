#!/usr/bin/python3
from datetime import datetime
from backend import crypto
import os

def getMsg(session, room):
    url = f"https://api.dontpad.com/{room}.body.json?lastModified=0"
    r = session.get(url).json()
    text = r["body"].encode("iso-8859-1").decode("utf-8")

    return text

def update_text(session, room):
    url = f"https://api.dontpad.com/{room}.body.json?lastModified=0"
    r = session.get(url).json()
    text = r["body"].encode("iso-8859-1").decode("utf-8")

    return text

# Transformar room em classe e remover roomAlias dos parâmetros
def postMsg(session, room, roomAlias, message):
    # data['text'] precisa ser todo o texto anterior + o texto novo
    # portanto, chame update() antes de cada post(), isso é um append

    # Utiliza o usuário do ambiente Linux
    user = os.environ.get("USER")

    time = datetime.now().replace(microsecond=0)
    stamp = datetime.timestamp(time) * 1000

    url = f"https://api.dontpad.com/{room}"

    # Comandos de debug e padrões de mensagem
    ###########################################
    # Estruturar melhor e separar deste arquivo

    if message.startswith("."):
        # Exibe a mensagem de conexão
        if message == ".defaultJoinMessage":
            txt = f"{update_text(session, room)}\n[{time}] {user} entrou na conversa."
        # Limpa as mensagens
        elif message == ".clearMessages":
            txt = ""
        # Exibe o hash MD5 da sala
        elif message == ".getRoomAddress":
            txt = f"{update_text(session, room)}\n(DEBUG) Sala: {roomAlias} - {room}"

        # (REVISAR) Teste de mensagem criptografada
        #elif message == ".sendEncMsg":
        #    key = crypto.loadKeys()
        #    txt = f"{update_text(session, room)}\n{crypto.encryptMsg('teste123', key)}"
        #elif message == ".enableEncryption":
        #    txt = f"{update_text(session, room)}\n[{time}] (DEBUG) modo criptografado ativado."

    # Formato de mensagem padrão
    else:
        txt = f"{update_text(session, room)}\n[{time}] <{user}> {message}"

    data = {
            "text":f"{txt}",
            "captcha-token-v2":"",
            "lastModified":f"{int(stamp)}",
            "force":"false"
            }

    if message == "/quit":
        txt = f"{update_text(session, room)}\n[{time}] {user} saiu da conversa."
        data = {"text":f"{txt}","captcha-token-v2":"","lastModified":f"{int(stamp)}","force":"false"}
        r = session.post(url, data=data)
        quit()
    else:
        r = session.post(url, data=data)
