# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:28:55 2026

@author: Patxi
"""

import feedparser

rss_url = "https://www.espn.com/espn/rss/news"

feed = feedparser.parse(rss_url)

print("ÚLTIMAS NOTICIAS:\n")

for noticia in feed.entries[:5]:
    print(noticia.title)
    print(noticia.link)
    print()