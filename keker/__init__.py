# -*- coding: utf-8 -*-

import requests
from re import findall, search
from random import shuffle, choice
from threading import Thread
from time import sleep
from datetime import datetime
from os import mkdir, name, system

about = lambda: print("Made For You By: @Tufaah\n\
> github.com/Tufaah\n> cracked.io/Tufaah\n> t.me/Tufaah")

# Made For You By: @Tufaah
# > github.com/Tufaah
# > cracked.io/Tufaah
# > t.me/Tufaah
#
# > Keker lib made to make making checkers much easier

try: mkdir('results')
except FileExistsError: pass
time = datetime.now();date = f'{time.month}_{time.day}_{time.hour}_{time.minute}_{time.second}'
mkdir(f'results/{date}')

class Combo:
    def __init__(self, combo: list): self.combo = combo
    def from_file(self, fileName: str):
        file = open(fileName, 'r', encoding='utf8', errors='ignore')
        self.combo[:] = file.read().splitlines()
        file.close()

    def from_api(self, url: str):
        response = requests.get(url).text
        self.combo[:] = response.splitlines()

    def pop(poped):
        try:
            if ':' in poped:
                new = str(poped).split(":", 1)
                return (new[0], new[1])
            else: return False
        except: return False

    class remove:
        def __init__(self, combo: list): self.combo = combo
        @property
        def duplicates(self): self.combo[:] = (list(set(self.combo)))
        
        @property
        def users(self):
            self.duplicates
            for c in self.combo[:]:
                if '@' not in str(c.split(':')[0]): self.combo.remove(c)

        @property
        def emails(self):
            self.duplicates
            for c in self.combo[:]:
                if '@' in str(c.split(':')[0]): self.combo.remove(c)

    class extract():
        def __init__(self, combo: list): self.combo = combo
        @property
        def passwords(self):
            result = []
            for c in self.combo:
                if ':' in c: result.append(str(c.split(':')[1]))
            return result

        @property
        def emails(self):
            result = []
            for c in self.combo:
                if ':' in c:
                    if '@' in str(c.split(':')[0]): result.append(str(c.split(':')[0]))
            return result

        @property
        def users(self):
            result = []
            for c in self.combo:
                if ':' in c:
                    if '@' not in str(c.split(':')[0]): result.append(str(c.split(':')[0]))
            return result

    class edit:
        def __init__(self, combo: list): self.combo = combo
        @property
        def swap(self): self.combo[:] = self.combo[::-1]
        @property
        def shake(self): shuffle(self.combo)


class Proxy:
    updates = 0
    def __init__(self, proxy: list): self.proxy = proxy
    def from_file(self, fileName: str):
        file = open(fileName, 'r', encoding='utf8', errors='ignore')
        self.proxy[:] = file.read().splitlines()
        file.close()

    def from_api(self, url: str):
        response = requests.get(url).text
        self.proxy[:] = response.splitlines()

    def auto_update(self, url: str, minutes: int):
        def update():
            while True:
                Proxy.updates += 1
                Proxy(self.proxy).from_api(url)
                sleep(minutes*60)
        Thread(target=update).start()

    def proxies(proxy_type, proxy): return {'http': f'{proxy_type}://{proxy}', 'https': f'{proxy_type}://{proxy}'}

    @property
    def random(self): return choice(self.proxy)
        
    @property
    def auth(self):
        for p in self.proxy[:]:
            if str(p).count(':') == 3:
                x = str(p).split(":")
                self.proxy[self.proxy.index(p)] = f'{x[2]}:{x[3]}:{x[0]}:{x[1]}'
    
    class edit:
        def __init__(self, proxy: list): self.proxy = proxy
        @property
        def swap(self): self.proxy[:] = self.proxy[::-1]
        @property
        def shake(self): shuffle(self.proxy)


class Main:
    def save(fileName: str, data):
        with open(rf'results/{date}/{fileName}', "a+") as save_file:
            save_file.write(str(data)+'\n')
    
    def clear(): 
        system('cls' if name=='nt' else 'clear')

    def title(info): system("title " + info)

    class input:
        def combo(msg=' [Input] Drag your COMBO here: '): return input(msg).replace('"', '').replace("'", "").strip()
        def proxy(msg=' [Input] Drag your PROXIES here: '): return input(msg).replace('"', '').replace("'", "").strip()
        def threads(msg=' [Input] How many THREADS [ 10 - 1000 ]: '): return int(input(msg))
        def proxy_type(msg=' [Select] (1): HTTP/S (2): SOCKS4 (3): SOCKS5\n [Input] Choise: '): 
            proxy_type_input = str(input(msg))
            if proxy_type_input == "2": return "socks4"
            elif proxy_type_input == "3": return"socks5"
            return "http"

    def multi_threading(threads_value, target):
        threads = []
        for i in range(threads_value):
            th = Thread(target=target)
            threads.append(th)
            th.start()

        for thread in threads:
            thread.join()


class Scrap:
    class value:
        def search(text: str, html: str):
            to_find = lambda s: search(text.replace(f'<>{text.strip()[-1]}', f'([^{text.strip()[-1]}]+)'), s)
            if to_find(html): return to_find(html).group(1)
            return None

        def find(text: str, html: str):
            to_find = text.replace(f'<>{text.strip()[-1]}', f'([^{text.strip()[-1]}]+)')
            return findall(to_find, html)

    class javaScript:
        def javaScript(html): return findall('<script>[^>]+>', html)

        def search(text, html):
            to_find = lambda s: search(text.replace(f'<>{text.strip()[-1]}', f'([^{text.strip()[-1]}]+)'), s)
            for i in Scrap.javaScript.javaScript(html):
                if to_find(i): return to_find(i).group(1)

        def find(text, html):
            to_find = text.replace(f'<>{text.strip()[-1]}', f'([^{text.strip()[-1]}]+)')
            return findall(to_find, " ".join(Scrap.javaScript.javaScript(html)).replace('\n', ' '))