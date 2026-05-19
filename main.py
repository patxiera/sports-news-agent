# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:28:55 2026

@author: Patxi
"""

import feedparser

rss_urls = [
    "https://e00-marca.uecdn.es/rss/futbol.xml",
    "https://feeds.elpais.com/mrss-s/pages/ep/site/as.com/portada"
]

for rss_url in rss_urls:

    feed = feedparser.parse(rss_url)

    print("\n====================")
    print("NUEVA FUENTE")
    print("====================\n")

    for noticia in feed.entries[:10]:

        titulo = noticia.title.lower()

        # filtro fútbol
        palabras_futbol = [
            "fútbol",
            "football",
            "liga",
            "champions",
            "real madrid",
            "barça",
            "barcelona",
            "atlético"
        ]

        if any(p in titulo for p in palabras_futbol):

            print(noticia.title)
            print(noticia.link)
            print()
