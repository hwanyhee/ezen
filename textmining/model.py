from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import re
import nltk

class SamsungReport:
    def __init__(self):
        self.okt=Okt()


    def read_file(self):

        self.okt.pos("삼성전자 글로벌센터 전자사업부",stem=True)
        filename='./text/kr-Report_2018.txt'

        with open(filename,'r',encoding='utf-8') as f:
            texts = f.read()
        return texts

    @staticmethod
    def extract_hangul(texts):
        temp = texts.replace('\n',' ')
        tokenizer = re.compile(r'[^ ㄱ-힣]+')
        temp = tokenizer.sub('',temp)
        return temp
    @staticmethod
    def change_token(texts):
        tokens = word_tokenize(texts)
        print(tokens[:7])
        return tokens

    def extract_noun(self):
        #삼성전자의 스마트폰은 ->삼성전자 스마트폰
        noun_tokens =[]
        tokens = self.change_token(self.extract_hangul(self.read_file()))

        for token in tokens:
            token_pos = self.okt.pos(token)
            temp = [txt_tag[0] for txt_tag in token_pos if txt_tag[1]=='Noun']
            if len(' '.join(temp)) > 1:
                noun_tokens.append(' '.join(temp))

        texts = ' '.join(noun_tokens)
        print('----------- 추출된 명사 300-----------')
        print(texts[:300])

    @staticmethod
    def download():
        nltk.download()