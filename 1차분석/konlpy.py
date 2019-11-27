from konlpy.tag import Komoran
import numpy
import scipy

komoran=Komoran() 

text_file=open("C:/Users/student/Documents/GitHub/Moons/1차분석/test1.txt",'r',encoding='utf-8')
data=text_file.readlines()
noun_data = komoran.nouns(data)
print(noun_data)