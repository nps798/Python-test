
arr=[]
num = int(input("請問您要比較幾個值？"))
for i in range(0,num,1):
	inp = float(input("請輸入第" + str(i+1) +  "個值？"))
	arr.append(inp)

for m in range(len(arr)-1,0,-1):
	for n in range(0,m,1):
		if(arr[n]<arr[n+1]):
			temp = arr[n]
			arr[n] = arr[n+1]
			arr[n+1] = temp
print(arr)
'''	
print("最大值:" ,max ,"  最小值:" ,min)
mean = (max + min)/2
print(arr)

# extend() 括號內要填入List資料 ex. [2] but not 2
arr.extend([arr[min_index]])
del arr[min_index]

print(arr)

arr.insert(0,arr[max_index])
del arr[max_index+1]

print(arr)
print(mean)


temp = arr
for j in range(1,len(arr),1):
	if(temp[j]>mean):
		temp.insert(1,j)
		print("比較大")
		
	elif(j<mean):
		arr.extend([j])
		print("小")
print(arr)


'''

		
			
			
			