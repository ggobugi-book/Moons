from konlpy.tag import Komoran
tagger = Komoran()  # 형태소 분석기
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import requests
import lxml.html
import codecs

#미술관옆동물원시나리오 읽어오기
articles = []
fp = codecs.open("2CJ00052.txt", "r")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("body")
text = body.getText()
articles = text.split("\n")
len(articles)
fp.close()

from sklearn.feature_extraction.text import TfidfVectorizer

def get_noun(text):
    nouns = tagger.nouns(text)
    return [n for n in nouns if len(n) > 1]  # 2글자 이상인 명사만 추출

#TF-IDF 행렬구하기
cv = TfidfVectorizer(tokenizer=get_noun, max_features=100)
tdm = cv.fit_transform(articles)

#print(tdm.toarray())
#print(tdm) 

import numpy
import operator
words = cv.get_feature_names()
count_mat = tdm.sum(axis=0)
count = numpy.squeeze(numpy.asarray(count_mat))
word_count = list(zip(words, count))
word_count = sorted(word_count, key=operator.itemgetter(1), reverse=True)
word_count

hot_key = list(dict(word_count[:50]).keys())
hot_key

#word cloud
#%matplotlib inline
from matplotlib import pyplot
from wordcloud import WordCloud
wc = WordCloud(font_path='C:\\Windows\\Fonts\\NGULIM.ttf', background_color='white', width=400, height=300)
cloud = wc.fit_words(dict(word_count))
pyplot.figure(figsize=(12, 9))
pyplot.imshow(cloud)
pyplot.axis("off")
pyplot.show()

import codecs
from konlpy.tag import Twitter
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

def sigmoid(x):
    return 1 / (1 + math.e ** -x)

# 텍스트를 처리하기
twitter = Twitter()
results = []
lines = articles
words_all = []

for line in lines:
    # 형태소 분석하기
    malist = twitter.pos(line, norm=True, stem=True)
    r = []
    for word in malist:
        # 명사/동사/부사만 걸러내기 
        if word[1] in ['Noun','Verb','Adjective']:
            r.append(word[0])
            words_all.append(word[0])
    rl = (" ".join(r)).strip()
    results.append(rl)
    #print(rl)
    
# 파일로 저장하기
from gensim.models import word2vec
yang_file = 'yang.model'
with open(yang_file, 'w', encoding='utf-8') as fp2:
    fp2.write("\n".join(results))
    
fp2.close() 

# Word2Vec 모델
data = word2vec.LineSentence(yang_file)
model = word2vec.Word2Vec(data,size=200, window=10, hs=1, min_count=2, sg=1)
model.save("yang_w2v.model")

################ 테스트 #######
model.most_similar(positive=["춘희"])
model.most_similar(positive=["철수"])
model["결혼"]
model["사람"]
model.most_similar(positive=["미술관","여자"] , negative=["여자"])

from IPython.display import Image
from sklearn.decomposition import PCA

#차원을 줄여주기(그래프를 그려주기 위함) 
words = list(model.wv.vocab)
X = model[model.wv.vocab]
pca = PCA(n_components=2)
result = pca.fit_transform(X)

result2 = StandardScaler().fit_transform(result)
db = DBSCAN(eps=0.3, min_samples=10).fit(result2)
labels = db.labels_

import collections
import math
import numpy as np 

myCounter = collections.Counter(words_all)
#print('myCounter:', myCounter)

radiuds = np.array([i for i in list(myCounter.values())])
area = np.pi * (radiuds)**2  
table_words = list(myCounter.keys()) 
table_counts = list(list(myCounter.values()))

import matplotlib.pyplot as plt
import matplotlib
from matplotlib.font_manager import FontProperties
import matplotlib.font_manager as fm 

#top50의 단어를 선별하여 word2vec을 계산하고 좌표로 찍어준다. 
font_location = "C:\\Windows\\Fonts\\NGULIM.TTF"
font_name = fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

valid_words = [hot_key[i] for i in range(0,50) if hot_key[i] in words]
valid_index = [words.index(str_temp) for str_temp in valid_words]   
valid_labels = [labels[i]+1 for i in valid_index]
valid_area = area[[table_words.index(str_temp) for str_temp in valid_words]]   
zip_index = zip(valid_index,valid_words)

plt.figure(figsize=(16, 8))
plt.scatter(result[valid_index, 0], result[valid_index, 1] , c = valid_labels , s = area , alpha=0.3)
for i, word in zip_index:
    plt.annotate(word, xy=(result[i, 0], result[i, 1]))
    
plt.show()

#캐릭터 관계테스트 
model.similarity('춘희', '철수')
model.similarity('춘희', '인공')
print(model.most_similar(positive=["인공"], topn=100))


