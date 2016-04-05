import re



pat = '*千*百'
'''Special Character
  . 代表任何字，except a newline，
                例如 text = 'id,c\n5' 
				     re.findall(pat, text)
					 #resule: ['i', 'd', ',', 'c', '5']
  ^ 代表以什麼開頭，例如 pat = '^id'
                         text = 'id,c\n5'
                         re.findall(pat, text)
                         # result: ['nd']
  $ 代表以什麼結尾，例如 pat = 'c5$'
                         text = 'id,c5'
						 # resulr: ['c5']
  * 代表*前面的字元可以重複0次~多次，例如	'6百*'	可找到 '6' '6百' '6百百'	 	
  + 代表+前面的字元可以重複1次~多次
  
						 
'''
text = '5千600萬'
text = '8千3百萬元'
#Byte String只能包含ASCII (不能有中文)


print(re.findall(pat, text))
print(text)


#以下為金額偵測程式
def tellmoney(str):
	foreign = ['日幣','日圓','日元','美元','美金']
	str
	#先排除外幣
	#再來分析本國金幣
