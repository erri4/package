import requests
import tkinter.messagebox
from scapy.layers.http import HTTPRequest
from scapy.all import *


blacklist = ['https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'https://www.youtube.com/watch?v=xvFZjo5PgG0']


def openwin():
    tkinter.messagebox.showwarning(title='Warning', message="This is a rickroll")


def process_packet(pkt: Packet):
    if pkt.haslayer(HTTPRequest):
        method = pkt[HTTPRequest].Method.decode()
        host = pkt[HTTPRequest].Host.decode()
        path = pkt[HTTPRequest].Path.decode()
        
        if method == 'GET':
            url = f'http://{host}{path}'
            if isrick(url):
                openwin()


def isrick(url: str):
    res = requests.get(url)

    page = str(res.text)

    if 'never gonna' in page or 'rick' in page or url in blacklist:
        return True
    return False
