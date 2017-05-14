import datetime
from datetime import date
import math

#date & time
print("datetime:")
print(datetime.datetime.now())
print("--------------------------")

#area of circle
radius = float(input("enter the radius:"))
area = math.pi * pow(radius, 2)
print("area of circle is:",area )
print("--------------------------")

#create list & tuple
input_seq = input("enter the number sequence: ")
split_seq = input_seq.split(",")
list = []
for seq in split_seq:
	list.extend(seq)	
print("list : ",list)
print("tuple : ",tuple(list))	
print("--------------------------")

#returning file extention
filename = input("enter the file name : ")
ext = filename.split(".")
print("extention of file is: ",ext[1])
print("--------------------------")

#input = n;output = n+nn+nnn
number = int(input("enter a number : "))
count = 1
result =0
while(count <= number):
	temp = number ** count
	result = result + temp
	count = count + 1;
print("output : ",result)
print("--------------------------")

#return the difference of date
def diff_dates(d1,d2):
	diff = d1-d2
	print("number of days:",diff.days)
	return
print("difference between (1995,5,5) and (1995,1,7)")
diff_dates(date(1995,5,5),date(1995,1,7))
print("--------------------------") 
		


	

