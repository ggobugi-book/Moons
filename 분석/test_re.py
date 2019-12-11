import re

###########감정 분석############
sentifile = open('C:/Users/student/Documents/GitHub/Moons/분석/test3.txt','r',encoding='utf-8')
senti_line = sentifile.readlines() #한 문장씩 받기

str_senti_line = ' '
for i in senti_line:
    str_senti_line += i
##### 함수 모음 #######



#### 입력받은 사람이 들어간 문장 차기위한 변수 생성 #####
character_senti = [['형식'],['영채'],['병욱'],['선형']] 

result = []
for i in character_senti[0:]:
    B=character_senti.pop(0)
    result += ([B+a for a in character_senti])
#print(result)

##### 한 문장에 캐릭터 2명이 들어간 것을 찾는다 #####

match_char=[]
for i in result:
    #print(i)
    i = str(i) 
    # print(i) 
    # print(type(i))
    for sents in senti_line[0:]:
        #print(type(sents))
        m = re.match(i,sents,re.MULTILINE) 
        print(m)
        
##########################################################################################

class KnuSL()
    def data_list(wordname):	
            with open('C:/Users/student/Documents/GitHub/Moons/분석/data/SentiWord_info.json', encoding='utf-8-sig', mode='r') as f:
                data = json.load(f)
            result = ['None']	
            for i in range(0, len(data)):
                if data[i]['word'] == wordname:
                    result.pop()
                    result.pop()
                    result.append(data[i]['polarity'])	
            
        
            s_word = result[1]
            return s_word

if __name__ == "__main__":
	
	ksl = KnuSL

    for word in match_char[0:]:
    while(True):
		wordname = input("word : ")
		wordname = wordname.strip(" ")		
		if wordname != "#":
			print(ksl.data_list(wordname))
			print("\n")	
				

		elif wordname == "#":
			print("\n이용해주셔서 감사합니다~ :)")
			break