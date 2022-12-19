# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 14:55:17 2022

@author: GerardGallardo
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import sqlite3

# Paràmetres de configuració:
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-cookie-encryption")
options.add_argument(r"user-data-dir=/bin/crawler/test")
browser = webdriver.Chrome(executable_path=r'/bin/crawler/chromedriver', options=options)

# Creació del procés d'automatització:
browser.get('https://developer.mozilla.org/de/')
browser.implicitly_wait(2)

# Creació de la DB:
con = sqlite3.connect(r'/bin/crawler/test/Default/Cookies')
cur = con.cursor()
cur.execute("SELECT * FROM cookies")
rows = cur.fetchall()

for row in rows:
    print(row)