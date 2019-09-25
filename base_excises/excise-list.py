'''
列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
列表的数据项不需要具有相同的类型
创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可
'''
# list1=['Google','Runoob',1997,2000]
# list2=[1,2,3,4,5,6,7]
# list3=["a","b","c",'d']
'''
访问列表中的值
使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符
'''
# print('list1[0]:',list1[0])
# print('list2[1:5]:',list2[1:5])
'''
更新列表
你可以对列表的数据项进行修改或更新
'''
# print('打印第三个元素:',list1[2])
# list1[2]=2001
# print(list1)
'''
删除列表元素
可以使用 del 语句来删除列表的的元素
'''
# list = ['Google', 'Runoob', 1997, 2000]
# del list[2]
# print(list)

'''
Python列表脚本操作符
+ 号用于组合列表，* 号用于重复列表。
'''
# print(len([1,2,3]))
# print([1,2,3]+[4,5,6])
# print(['hello']*4)
# print(3 in [1,2,3])
# for x in [1,2,3]:
#     print(x,end=" ")

'''
列表还支持拼接操作
使用嵌套列表即在列表里创建其它列表
'''
# squares = [1, 4, 9, 16, 25]
# squares+=[36, 49, 64, 81, 100]
# print(squares)
# a = ['a', 'b', 'c']
# n = [1, 2, 3]
# x=[a,n]
# print(x)
# print(x[0])
# print(x[0][1])
'''
Python列表函数
len()
max()
min()
list(seq) -- 将元组或字符串转换为列表
'''
# list1 = ['Google', 'Runoob', 'Taobao']
# print (len(list1))
# list2=list(range(5)) # 创建一个 0-4 的列表
# print (len(list2))

# list1, list2 = ['Google', 'Runoob', 'Taobao'], [456, 700, 200]
# print ("list1 最大元素值 : ", max(list1))
# print ("list2 最大元素值 : ", min(list2))

# aTuple = (123, 'Google', 'Runoob', 'Taobao')
# list1 = list(aTuple)
# print ("列表元素 : ", list1)

# str="Hello World"
# list2=list(str)
# print ("列表元素 : ", list2)

'''
Python包含以下方法
list.append(obj)--在列表末尾添加新的对象
'''
# list1 = ['Google', 'Runoob', 'Taobao']
# list1.append('Baidu')
# print ("更新后的列表 : ", list1)

a=[1,2,3]
b=[2,3,4]
diff=list(set(a).difference(set(b)))
print(diff)