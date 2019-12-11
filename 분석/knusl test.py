import json


class KnuSL():

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
							
		print('극성 : ' + s_word)		
		
		
		return s_word

if __name__ == "__main__":
	
	ksl = KnuSL

	for i in match_char[0:]:
		i = i.strip(" ")
		point = ksl.data_list(i)
		for total in point[0:]:
			total += i
