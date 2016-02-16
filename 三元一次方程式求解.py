#x + y +z=100
#6*x + 3*y + 0.1*z =100
# 求正整數解

import time, itertools
num = 2
print(float(num).is_integer())
print("歡迎來到數學題！")
print("     x + y +z=100")
print("     6*x + 3*y + 0.1*z =100")
print("     求正整數解")



def cal_time(info , tStart=0):
	if(info=="start"):
		tStart = time.time()
		return tStart
	if(info=="end"):
		tEnd = time.time()
		alltime = tEnd-tStart
		return alltime

ju = input("請問你要執行暴力版(1)，修正版(2)，任意方程式版(3)？")
if(ju=="1"):
	hu2 = input("會執行很久喔！你確定 (Y/N)？")
	if(hu2=="N"):
		print("請重新執行程式！")
	elif(hu2 =="Y"):
		tStart_outside = cal_time("start")
	
		for x in range(1,101,1):
			for y in range(1,101,1):
				for z in range(1,101,1):
					if(x+y+z ==100):
						if(6*x + 3*y + 0.1*z == 100):
							i=x
							j=y
							k=z
						else:
							print("x = " , x,	"y = "	,y	, "z = ",z , "不是答案"	)
					else:
						print("x = " , x,	"y = "	,y	, "z = ",z , "不是答案"	)

		print("------------------------------------------")				
		print("答案是:" , "x =", i, "y = " , j, "z = " , k )
		
		print("總執行時間為:",end='')
		print(cal_time("end" , tStart_outside))
				
elif(ju=="2"):				
	tStart_outside=cal_time("start")
	for x in range(1,101,1):
		# 當x=1
		# y + z = 99 = 100-x
		#    3y + 3z = 300-3x
		# 3y + 0.1z = 100-6x
		#     2.9z = 200+3x
		#     z = (200+3x)/2.9
		
		z = (200+ 3*x) / 2.9	
		y = 100-x-z
		if(z.is_integer()):
			if(y.is_integer()):
				if(z>0):
					if(y>0):
						print("x = " , x,	"y = "	,y	, "z = ",z , "----------------------------是答案"	)
						
						print("總執行時間為:",end='')
						print(cal_time("end", tStart_outside))
						

		
elif(ju=="3"):
	
	print("請輸入方程式？")
	print("a*x + b*y + c*z = d")
	print("e*x + f*y + g*z = h")
	arr = []


	for i in range(0,8,1):
		arr.append(float(input("請輸入" + chr(97+i) + "的值？")))
		
	a = arr[0]
	b = arr[1]
	c = arr[2]
	d = arr[3]
	
	e = arr[4] 
	f = arr[5]
	g = arr[6]
	h = arr[7]
	
	print("您所指定的方程式為：")
	print(a  ,"x + ", b ,"y + ",c, "z = " , d)
	print(e  ,"x + ", f ,"y + ",g, "z = " , h)
	
	# a*x + b*y + c*z = d
    #    b*y + c*z = d - a*x 
	#    bf*y + cf*z = df - af*x
	
	# e*x + f*y + g*z = h
	#    f*y + g*z = h - e*x
	#    bf*y + bg*z = bh - be*x	
	

	tStart_outside=cal_time("start")
	ggg = 0
	for x in range(1,10000,1):
		#貌似不能用中括號 ex. [ (c*e-a*g)*x + (d*g-c*h) ] / (b*g - c*f)
		y = (c*e-a*g)*x/(b*g - c*f) + (d*g-c*h)/(b*g - c*f)
		z = (b*e-a*f)*x/(c*f - b*g) + (d*f - b*h)/(c*f - b*g)
		if(z.is_integer()):
			if(y.is_integer()):
				if(z>0):
					if(y>0):
						print("x = " , x,	",y = "	,y	, ",z = ",z , "----------------------------是答案"	)
						ggg = 1
						
		if(x==100):
			if(ggg!=1):
				print("此方程式並無正整數解")
		

	print("總執行時間為:",end='')
	print(cal_time("end", tStart_outside))
		
			
			
			