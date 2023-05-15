#!/usr/bin
import os, requests
from backend import web, crypto

# métodos de teste da aplicação
# sem curses

user = os.environ.get("USER")

def getRoomName():
    os.system('clear')
    print(":: DontChat alpha0.1 :: [ sala: --- ]", end="\n\n")
    return input("Digite o nome da sala> ")

def protoMenu(session, room, roomAlias):
    while True:
        os.system('clear')
        print(f":: DontChat alpha0.1 :: [ sala: {roomAlias} ]\ndica: digite /quit para sair!", end="\n\n")

        # Recebe as mensagens no corpo do chat
        # e exibe na tela
        print(web.getMsg(session, room), end="\n\n")

        # Campo de input para envio de mensagens
        web.postMsg(session, room, roomAlias, input(f"{user}> "))

def startApp():
    roomAlias = getRoomName()
    room = crypto.encryptRoom(roomAlias)
    session = requests.Session()

    # Envia a mensagem de conexão de usuário
    web.postMsg(session, room, roomAlias, ".defaultJoinMessage")

    protoMenu(session, room, roomAlias)
