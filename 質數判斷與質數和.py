import math
import time

while(1):
	sum=0
	num = input("請問你要1~多少的質數總和？")


	# 記錄開始時間 Record start time
	tStart = time.time()

	
	#新二版 29.64秒
	for i in range(2,int(num)+1,1): 
		for j in range(2,i+1,1):
			if(j*j>i):
				print(i,"是質數")
				sum+=i
				break
			elif(i % j == 0):
				print(i,"是合數")
				break
					
	
	'''
	#新版 29.39秒
	for i in range(2,int(num)+1,1):
		for j in range(2,i+1,1):
			if(i % j == 0):
				if(i != j):
					print(i,"是合數")
					break
				else:
					if(i==j):
						print(i,"是質數")
						sum+=i
	
	#原版 25.077秒
	for i in range(2,int(num)+1,1):
		if(i==2):
			print(i,"是質數")
			sum+=i	
		else:
			for j in range(2,i,1):
				if(i % j == 0):
					print(i,"是合數")
					break
				else: 
					if(j==i-1):
						print(i,"是質數")
						sum+=i
						break
	'''		
	print("---------------")
	print("總和:", sum)


	# 記錄結束時間 Record stop time
	tStop = time.time()
	print("Code執行時間 = ",end = '')
	print(tStop - tStart,end = '')
	print("秒")
