from konlpy.tag import Komoran
from pprint import pprint
import numpy
import scipy
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
from IPython import embed
import re

komoran=Komoran() 

path=open("C:/Users/student/Documents/GitHub/Moons/분석/test4.txt",'r',encoding='utf-8')
line=path.read()

words = []

while True:
    if not line:
        break
    elif line =="\n":
        continue
    elif line =="" :
        continue

    line = line.replace("'","").replace("?","").replace(".","").replace("'","").replace('"'
    ,"").replace("!","").replace("-","").replace('"',"").replace("\n\n","")
    words = komoran.nouns(line)

    print(words)

#//////////////////////////////////////////

# noun_data = komoran.nouns(data)
# print(noun_data)
cv = CountVectorizer()
word_count_vector = cv.fit_transform(words)

tfidf=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf.fit(word_count_vector)

df = pd.DataFrame(tfidf.idf_,index=cv.get_feature_names(),columns=["idf_weight"])
print(df)

# #행렬형식으로 문서의 단어 개수를 가지고오는 코드
count_vector =cv.transform(words)
print(count_vector)

# print(count_vector.shape())
# #tf-idf score

# tfidf_vector = tfidf.transform(count_vector)
# noun_names = cv.get_feature_names()
# first_document_vec = tfidf_vector[2100]
# df = pd.DataFrame(first_document_vec.T.todense(), index=noun_names, columns=["tfidf"])
# df.sort_values(by=["tfidf"],ascending=True)

#////////////////////////////////////

#print(df)
#print(tfidf_vector)

# text_noun=[]
# for tx in text_file:
#     text_noun.append(tx)




    
    


#text = text_file.readlines()
#text_nouns=komoran.pos(text_file)
#embed()
#print(text_nouns)

#pprint(text)
#text_list = list(text)
#pprint(text)

# cv=CountVectorizer()
# word_count_vector=cv.fit_transform(text)
# #print(word_count_vector)

# tfidf_tranformer=TfidfTransformer(smooth_idf=True,use_idf=True)
# tfidf_tranformer.fit(word_count_vector)

# df_idf=pd.DataFrame(tfidf_tranformer.idf_,index=cv.get_feature_names(),columns=['idf_weight'])
# df_idf.sort_values(by=['idf_weight'])

# count_vector=cv.transform(text)
# tf_idf_vector=tfidf_tranformer.transform(count_vector)

# feature_names = cv.get_feature_names()
# frist_document_vector=tf_idf_vector[0]


# tfidf_vectorizer = TfidfVectorizer(use_idf=True)
# tfidf_vectorizer_vectors = tfidf_vectorizer.fit_transform(text_nouns)
#print(tfidf_vectorizer_vectors)

# first_vector_tfidfvectorizer=tfidf_vectorizer_vectors[0]
#print(first_vector_tfidfvectorizer)

# df=pd.DataFrame(first_vector_tfidfvectorizer.T.todense(),index=tfidf_vectorizer.get_feature_names(),columns=["tf-idf"])
# df.sort_values(by=["tf-idf"],ascending=True)
# print(df)
# print(df)

#ㅡㅡㅡㅡㅡㅡㅡㅡ<여러 시도>ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# komorean.pos(text)
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