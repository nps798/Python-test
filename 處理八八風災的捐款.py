import csv

file = open("C:\\Users\\CHICHI\\Desktop\\88_input.txt", "r")
i=1
data = []
for line in file:
	print("第" ,i ,"行:", end="")
	if("元" in line):
		loca = line.find("元")
		print(line[loca-10:loca+1])
		data.append([line[loca-10:loca+1],line])
	else: 
		print()
		data.append(["",line])
	i=i+1

f = open("C:\\Users\\CHICHI\\Desktop\\88_output.csv","a")  
w = csv.writer(f)  
w.writerows(data)  
f.close()  