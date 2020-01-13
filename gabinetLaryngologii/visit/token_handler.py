from fernet import Fernet
import base64
import logging
from time import time
import traceback
from django.conf import settings


def encrypt(txt):
    txt = str(txt)
    cipher_suite = Fernet(settings.ENCRYPT_KEY)  # key should be byte
    encrypted_text = cipher_suite.encrypt(txt.encode('ascii'))
    encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii")
    return encrypted_text


def decrypt(txt):

    txt = base64.urlsafe_b64decode(txt)
    cipher_suite = Fernet(settings.ENCRYPT_KEY)
    decoded_text = cipher_suite.decrypt(txt).decode("ascii")
    return decoded_text


def token_generator(email):
    token = encrypt(email + 'SEPARATOR' + str(time()))
    return token
