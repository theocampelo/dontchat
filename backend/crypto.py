#!/usr/bin/python3
import hashlib
import rsa

# Gera par de chaves RSA
def generateKeys():
    (publicKey, privateKey) = rsa.newkeys(1024)
    with open('keys/publicKey.pem', 'wb+') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('keys/privateKey.pem', 'wb+') as p:
        p.write(publicKey.save_pkcs1('PEM'))

# Carrega o par de chaves RSA
def loadKeys():
    with open('keys/publicKey.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read().decode('ascii'))
    with open('keys/privateKey.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read().decode('ascii'))

    return privateKey, publicKey

# Transforma o nome da sala em sua hash md5
def encryptRoom(roomName):
    encrypted = hashlib.md5(roomName.encode("utf-8"))
    return encrypted.hexdigest()

# Criptografa a mensagem usando as chaves RSA
def encryptMsg(message, key):
    return rsa.encrypt(message.encode('ascii'), key)

# Descriptografa a mensagem usando as chaves RSA
def decryptMsg(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False
