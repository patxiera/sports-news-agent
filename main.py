# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:28:55 2026

@author: Patxi
"""


import feedparser
import requests
import os
from datetime import datetime, timezone, timedelta

TOKEN = "8601460374:AAHJ-kTRmz3nnF2_Y0Q1rMc9nY3KtebyD90"
CHAT_ID = "8943577359"

rss_urls = [
    "https://e00-marca.uecdn.es/rss/futbol.xml",
    "https://feeds.elpais.com/mrss-s/pages/ep/site/as.com/section/futbol/portada"
]

ARCHIVO = "enviadas.txt"

# Cargar enviadas
if os.path.exists(ARCHIVO):
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        enviadas = set(f.read().splitlines())
else:
    enviadas = set()

nuevas = []

ahora = datetime.now(timezone.utc)

for rss in rss_urls:

    feed = feedparser.parse(rss)

    print("Leyendo:", rss)

    for n in feed.entries[:15]:

        link = n.link
        titulo = n.title

        # Evitar repetidos
        if link in enviadas:
            continue

        # Comprobar fecha
        if hasattr(n, "published_parsed"):

            fecha = datetime(*n.published_parsed[:6], tzinfo=timezone.utc)

            # Solo noticias últimas 12 horas
            if ahora - fecha > timedelta(hours=12):
                print("Antigua:", titulo)
                continue

        mensaje = f"{titulo}\n{link}"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

        requests.post(url, data={
            "chat_id": CHAT_ID,
            "text": mensaje
        })

        print("Enviado:", titulo)

        enviadas.add(link)
        nuevas.append(link)

# Guardar nuevas
with open(ARCHIVO, "a", encoding="utf-8") as f:
    for link in nuevas:
        f.write(link + "\n")
