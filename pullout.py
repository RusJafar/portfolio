# -*- coding: utf-8 -*-
import re


class Pull(object):
    def __init__(self, txt):
        self.txt = ' '.join(txt)

#######################################################################################################################

    def finde_href(self,txt_in_tags):
        '''
        Метод заключает содержимое "<a href=" в квадратные скобки
        '''
        text_str = re.sub(r'<a.*?href=\"(.*?)','s3r',txt_in_tags).replace('\"','s3e')
        text_str = re.sub(r's3r(.*?)','[',text_str).replace('s3e','] <a')
        return self.remove_html(text_str)

#######################################################################################################################

    def remove_html(self,s):
        '''
        Метод удаляет все теги из данных
        '''

        tag = False
        quote = False
        out = ""

        for c in s:
                if c == '<' and not quote:
                    tag = True
                elif c == '>' and not quote:
                    tag = False
                elif (c == '"' or c == "'") and tag:
                    quote = not quote
                elif not tag:
                    out = out + c + ''

        return self.splitter(out)

#######################################################################################################################     
  
    def scan(self):
        '''
        Метод списывает теги <h1>,<h2>,<p> вместе с содержимым
        '''
        data = self.txt[self.txt.find('<h1')-3  :self.txt.find('<footer')]
        count = 1 
        st_new = ''
        runner = 0
        triger = 0
        while runner != len(data):
            
            
            if data[runner] == '<':
                if data[runner + 1] == 'p':
                    index_start = runner
                    
                    triger = 1
                elif data[runner + 1] == 'h' and (data[runner + 2] == '2' or data[runner + 2] == '1'):  
                    index_start = runner
                    triger = 1
                   
                    
            
            if data[runner] == '<':
                if data[runner + 1] == '/' and triger == 1 and data[runner + 2] == 'p':
                    index_p = runner
                    
                    triger = 0
                    st_new += '\t\t\t' + data[index_start:index_p] + '\n'
                    index_start = 0
                    index_p = 0
                elif data[runner + 1] == '/' and triger == 1 and data[runner + 2] == 'h':
                    index_p = runner
                    
                    triger = 0
                    st_new += data[index_start:index_p] + '\n\n'
                    index_start = 0
                    index_p = 0
            
            runner += 1
        return self.finde_href(st_new)

#######################################################################################################################

    def splitter(self,must_split):
        '''
        Метод разбивает текст на строки > 80 символов
        '''
        split_txt = ''
        len_line = 0
        for word in must_split.split(' '):
            len_word = len(word)
            len_line += len_word
            #print('len_word',len_word)
            if len_line + len_word >= 90:
                #print('len_line',len_line)
                split_txt +=  '\n\n' + word +' ' 
                len_line = 0
            elif len_line >= 90:
                #split_txt += '\n\n'
                len_line = 0
            else:
                split_txt += ' ' + word + ' ' 
                len_line += len_word
        return split_txt


if __name__ == "__main__":
    line_lst = []
    
