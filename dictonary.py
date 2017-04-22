#acending and decending order
import operator
d = {1:2,9:4,2:6,5:8}
sorted_d = sorted(d.items(),key=operator.itemgetter(0))
print("in decending : ",sorted_d )
sorted_a = sorted(d.items(),key=operator.itemgetter(0),reverse = True)
print("in acending : ",sorted_a )
print("-----------------")

#update
input_dict = {0:10,1:20}
add_dict = {2:30}
print("input_dict :%s" % input_dict)
print("add_dict :%s" % add_dict)
input_dict.update(add_dict)
print("updated input_dict :%s" % input_dict)
print("-----------------")
dict1 = {0:10,1:20}
dict2 = {2:20,3:30}
dict3 = {4:40,5:50}
dict4 = {}
print(dict1)
print(dict2)
print(dict3)
for d in (dict1,dict2,dict3):
	dict4.update(d)
print("new one: %s" % dict4 )
print("-----------------")

#check key availability
dict_sample = {'fruit':'grapes','vegetable':'tomato'}
key = input("enter the key to check : ")
result = key in dict_sample
if result is True:
	print("given key is available")
else:
	print("given key is not available")
print("-----------------")

#list keys & values
dict_sample = {'fruit':'grapes','vegetable':'tomato'}
print("key -> values")
print("---    ------")
for dict_key,dict_values in dict_sample.items():
	print(dict_key,'->',dict_values)
print("-----------------")

#compare dictionary
ages1 = {'arjun':4,'brindha':3}
ages2 = {'aarthi':5,'babu':4}
print("length of a dict ages1 : %d" % len(ages1))
ages1.clear()
print("length of a dict ages1 after using clear() command : %d" % len(ages1))
ages1 = ages2.copy()
print("ages1 after copying from ages2: %s" % ages1)
print("type of a dict ages2 : %s" % type(ages2))
print("-----------------")

#
