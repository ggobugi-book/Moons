from collections import Counter
from konlpy.utils import pprint
from konlpy.tag import Twitter
from konlpy.tag import Komoran
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

import re

#파일 읽어오기
file = open('C:/Users/student/Documents/GitHub/Moons/분석/test3.txt','r',encoding='utf-8')
line = file.read()

#장(chapter)마다 나눔
sentences = re.split('(?<=[2-9]\n)|(?<=[0-9][0-9]\n)|(?<=[0-9][0-9][0-9]\n)', line)

#Komoran 형태소 분석을 위한 전처리
sent=[]
for stuff in sentences:
#         stuff = stuff.replace("'","").replace("?","").replace(".","").replace("'","").replace('"'
# ,"").replace("!","").replace("-","").replace('"',"").replace("\n","")
        # stuff = re.sub("\n","", line).strip()
        sent.append(stuff)