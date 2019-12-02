from konlpy.tag import Komoran
import numpy
import scipy
import re



# text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
# regex = re.compile("아하")
# mo = regex.search(text)
# if mo != None:
#     print(mo.group()) 

# text = "사과 딸기 포도 벨 사과 딸기 포도벨"
# re.split(" ",text)
# print(re.split(" ",text))
# text="""사과
# 딸기
# 포도
# 벨
# 사과
# 포도벨
# 와와아
# 마셔라 마셔라 마셔라 ~
# 술이들어간다
# 쭉
# 쭉쭉쭉 ~
# 언제까지 어께춤을 추게 할거야
# 내어께를 봐
# 탈골됬자나
# 탈골탈골
# """

# print(re.split(" ",text))



# r=re.compile("a.c")
# r.search("kkk")

# print(r.search("abc"))


komoran=Komoran() 

text_file=open("C:/Users/student/Documents/GitHub/Moons/1차분석/test1.txt",'r',encoding='utf-8')
data=text_file.read()
# print(type(data))
print(data)
noun_data = komoran.nouns(data)
print(noun_data)