# -*- coding: utf-8 -*-
import requests
from pullout import Pull
import os
import re

class Parser(object):
    '''
    Скачивает содержимое URL-адреса в фаил, после чего читает его,
    передает даные в модуль "pullout" для обработки и сохраняет обработанные
    данные в фаил с именем файла URL-адреса(с заменой "/" на "_")
    '''
    def __init__(self, url):
        self.url = url

    def pars(self):
        r = requests.get(self.url)
        with open('test.txt','w',encoding='utf8') as f:
            f.write(r.text)
        return self.sv_text()
        

    def sv_text(self):
        line_str = ''
        with open('test.txt','rU', encoding='utf8') as self.output_file:
            for line in self.output_file:
                st = self.output_file.readlines()
                pl = Pull(st)
                line_str += pl.scan()
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test.txt') 
        os.remove(path)
        file_name = ''.join(re.findall(r'htt\w.*?:/(.*)', self.url))
        file_name = re.sub(r'\?.*?','',file_name).replace('','') + ''
        file_name = 'saved articles' + '/' +  re.sub(r'/.*?','_',file_name).replace('','') + '.txt'
        with open(file_name, 'w', encoding='utf8') as output_file:
            output_file.write(line_str)
            print('Документ готов!\n Адрес файла:\n', file_name)
        

   

if __name__ == "__main__":

    p = Parser('https://habr.com/ru/post/349860/')
    p.pars()
    

