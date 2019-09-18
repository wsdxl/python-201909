# '''
# Python字符串
# '''
# var1 = 'Hello World!'
# var2 = "welcome to wiki"
 
# print ("var1[0]: ", var1[0])
# print ("var2[1:5]: ", var2[1:5])
# var1 = 'Hello World!'
 
# print ("更新字符串 :- ", var1[:6] + 'coding!')

# a = "Hello"
# b = "Python"
 
# print ("a + b 输出结果：", a + b) 
# print ("a * 2 输出结果：", a * 2) 
# print ("a[1] 输出结果：", a[1]) 
# print ("a[1:4] 输出结果：", a[1:4]) 
 
# if( "H" in a) :
#     print ("H 在变量 a 中") 
# else :
#     print ("H 不在变量 a 中") 
     
# if( "M" not in a) :
#     print ("M 不在变量 a 中") 
# else :
#     print ("M 在变量 a 中")
 
# print (r'\n')
# print (R'\n')

# #Python字符串格式化

# print('My name is %s and weight is %d KG!' %('jack',60))



# '''
# Python列表
# '''
# list1 = ['physics', 'chemistry', 1997, 2000]
# list2 = [1, 2, 3, 4, 5, 6, 7 ]
 
# print ("list1[0]: ", list1[0])
# print ("list2[1:5]: ", list2[1:5])

# #更新列表:append()
# list=[]
# list.append('Google')
# list.append('coding')
# print(list)
# #末尾添加：extend()
# list.extend(['python','java'])
# print(list)

# #删除列表元素:del()
# list1 = ['physics', 'chemistry', 1997, 2000]
# print(list1)
# del list1[2]
# print(list1)
# print(len(list1))
# print([1, 2, 3,7] + [4, 5, 6])

# for x in [1,2,3,4]:
#     print(x)

# print(list((2,3,4)))
# print(len([2,3,4]))
# print([1,2,3].__len__())

# list1 = ['physics', 'chemistry', 1997, 2000]
# list3=[2,3,4,5]
# list3.reverse()
# list1.pop()
# print(list1,list3)
# list3.sort()
# print(list3)
# list1.insert(-1,2001)
# print(list1)
# print(list1.index(2001))

'''
Python元组,Python的元组与列表类似，不同之处在于元组的元素不能修改
'''
# tup = ('physics', 'chemistry', 1997, 2000)
# print (tup)
# del tup
# print ("After deleting tup : ")
# print (tup)

'''
Python字典:键一般是唯一的，如果重复最后一个键值对会替换前面的，值不需要唯一。
'''

# dict = {'Name': 'Sherlock', 'Age': 18, 'Class': 'First'}
 
# del dict['Name'] # 删除键是'Name'的条目
# print(dict)

# dict = {'Name': 'Sherlock', 'Age': 18, 'Class': 'First'}
 
# del dict['Age'] # 删除键是'Name'的条目
# print(dict)
# dict.clear()     # 清空词典所有条目
# print(dict)
# del dict        # 删除词典
# print(dict)

# #字典内置方法
# dict = {'Name': 'Sherlock', 'Age': 18, 'Class': 'First'}
# print(len(dict))
# print(dict.get('Name'))
# print(dict.items())
# print(dict.keys())
# print(dict.values())
# dict.pop('Class')
# print(dict)

# while 循环语句
# count=0
# while count<9:
#     print('The count value is: ',count)
#     count+=1
# print('Goodbye')


# i=1
# while i<10:
#     i+=1
#     if i%2 != 0:
#         continue  
#     print(i)

# i = 1
# while 1:      # 循环条件为1必定成立
#     print(i)         # 输出1~10
#     i += 1
#     if i > 10:      # 当i大于10时跳出循环
#         break


var = 1
while var == 1 : # 该条件永远为true，循环将无限执行下去
    num = input("Enter a number  :")
    print ("You entered: ", num) 
print ("Good bye!")

