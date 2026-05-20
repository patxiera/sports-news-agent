# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:28:55 2026

@author: Patxi
"""

import feedparser
import requests

TOKEN = "8601460374:AAHMK1KGQqB3T3EWOBo68kJTzNo8k5ihL80"
CHAT_ID = "8943577359"

rss_urls = [
    "https://e00-marca.uecdn.es/rss/futbol.xml",
    "https://feeds.elpais.com/mrss-s/pages/ep/site/as.com/portada"
]

palabras = ["fútbol", "liga", "champions", "real madrid", "barça"]

for rss in rss_urls:
    feed = feedparser.parse(rss)

    for n in feed.entries[:10]:
        titulo = n.title.lower()

        if any(p in titulo for p in palabras):

            mensaje = f"{n.title}\n{n.link}"

            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

            requests.post(url, data={
                "chat_id": CHAT_ID,
                "text": mensaje
            })

            print("Enviado:", n.title)
