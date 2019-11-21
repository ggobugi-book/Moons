from konlpy.tag import Komoran
from pprint import pprint
import numpy
import scipy
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd

komorean=Komoran() 
text_file=open("C:/Users/student/Documents/GitHub/Moons/1차분석/test3.txt",encoding='utf-8')

text = text_file.readlines()
#text_list = list(text)
#pprint(text)

cv=CountVectorizer()
word_count_vector=cv.fit_transform(text)
#print(word_count_vector)

tfidf_tranformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_tranformer.fit(word_count_vector)

df_idf=pd.DataFrame(tfidf_tranformer.idf_,index=cv.get_feature_names(),columns=['idf_weight'])
df_idf.sort_values(by=['idf_weight'])

count_vector=cv.transform(text)
tf_idf_vector=tfidf_tranformer.transform(count_vector)

feature_names = cv.get_feature_names()
frist_document_vector=tf_idf_vector[0]

df=pd.DataFrame(frist_document_vector.T.todense(),index=feature_names,columns=["tf-idf"])
df.sort_values(by=["tf-idf"],ascending=True)

print(df)

#ㅡㅡㅡㅡㅡㅡㅡㅡ<여러 시도>ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# pprint((komorean.pos(text)))
# text_file.close()
# vec_file=CountVectorizer(text_list)
# vec_file.fit(text_list)
# vec_file.vocabulary_
# print(vec_file)

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