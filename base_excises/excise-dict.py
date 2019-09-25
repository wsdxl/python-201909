'''
Python3 字典
字典是另一种可变容器模型，且可存储任意类型对象
'''
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# dict['Age']=8
# dict['School']='菜鸟教程'
# print(dict)

'''
删除字典元素
能删单一的元素也能清空字典，清空只需一项操作。
显示删除一个字典用del命令
'''
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# del dict['Age'] # 删除字典元素
# print(dict)
# dict.clear() #清空字典
# print(dict)
# del dict  #删除字典
# print(dict)

'''
字典键的特性
1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
'''
# dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
# print('dict[Name]:',dict['Name'])
# dict = {['Name']: 'Runoob', 'Age': 7}
# print ("dict['Name']: ", dict['Name'])

'''
内置函数：
str(dict)--输出字典，以可打印的字符串表示。
type(variable)--返回输入的变量类型，如果变量是字典就返回字典类型。
'''
# dict={'Name':'Jack','Age':9,'Class':'python'}
# print(str(dict))
# print(type(dict))

'''
内置方法：
1	radiansdict.clear()
删除字典内所有元素
2	radiansdict.copy()
返回一个字典的浅复制
3	radiansdict.fromkeys()
创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
4	radiansdict.get(key, default=None)
返回指定键的值，如果值不在字典中返回default值
5	key in dict
如果键在字典dict里返回true，否则返回false
6	radiansdict.items()
以列表返回可遍历的(键, 值) 元组数组
7	radiansdict.keys()
返回一个迭代器，可以使用 list() 来转换为列表
8	radiansdict.setdefault(key, default=None)
和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
9	radiansdict.update(dict2)
把字典dict2的键/值对更新到dict里
10	radiansdict.values()
返回一个迭代器，可以使用 list() 来转换为列表
11	pop(key[,default])
删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
12	popitem()
随机返回并删除字典中的最后一对键和值。
'''

dict = {'Name': 'Runoob', 'Age': 7}
for i,j in dict.items():
    print(i,':',j)