from konlpy.tag import Komoran
from pprint import pprint
import numpy
import scipy

komorean=Komoran() 
text_file=open("C:/Users/user/Documents/Moons/1차분석/test2.txt",encoding='utf-8')

text = text_file.read().replace
pprint(list(komorean.pos(text)))


# print(text)

# while True:
#     text=text_file.readline()
#     if not text: break
#     print(text)
#     # Text_list=[]
#     # for page in 

    



#print(komorean.pos(u'text_file'))

#참고: 다음기사 크롤링 https://leegijun.tistory.com/5
#참고: TF-IDF 라이브러리 - Scikit-Learn : https://blog.naver.com/shrntg/220655244241  /https://scikit-learn.org/dev/developers/advanced_installation.html