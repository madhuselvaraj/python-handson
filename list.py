#basic list operation
list_sample = [1,2,3,4,5,6,7,8,9,0]
print("sample list :",list_sample)
print("list_sample : ",list_sample[2:5])
list_sample[3] = 0
print("updating 4 to 0 :",list_sample[2:5])
del list_sample[3]
print("sample list after deleting list_sample[3]:",list_sample)
print("---------------")

#students data
students_list = ['archana','bala','christy','christy']
print("students list : ",students_list)
#counting
print("how many bala are there : ",students_list.count('bala'))
print("how many christy are there : ",students_list.count('christy'))
print("---------------")
#appending one more
students_list.append('dhandabani')
print("students list : ",students_list)
print("---------------")
#extend student list
new_students = ['dimple','erickson','franklin']
students_list.extend(new_students)
print("new students list : ",new_students)
print("updated students list : ",students_list)
print("---------------")

#find role number
student_name = input("enter the student name : ")
role_num = students_list.index(student_name)
print(role_num)
print('role number of ' + student_name + ' is ',role_num)

