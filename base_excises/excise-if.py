'''
if – elif – else
1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
3、在Python中没有switch – case语句
'''
# age=int(input('请输入你家狗狗的年龄：'))
# print("")
# if age <0:
#     print('你是在逗我吧！')
# elif age==1:
#     print('相当于14岁的人。')
# elif age==2:
#     print('相当于22岁的人。')
# elif age>2:
#     human=22+(age-2)*5
#     print('对应的人类年龄是：',human)
# ###退出提示
# input('点击enter键退出')
'''
# 数字猜谜游戏
# '''
# number = 7
# guess = -1
# print('数字猜谜游戏！')
# while guess != number:
#     guess = int(input('请输入你猜的数字：'))
#     if guess < number:
#         print('你猜的数字小了')
#     elif guess > number:
#         print('你猜的数字大了')
#     elif guess == number:
#         print('恭喜你猜对了')

'''
if 嵌套
在嵌套 if 语句中，可以把 if...elif...else 结构放在另外一个 if...elif...else 结构中。
'''
num = int(input('请输入一个数字：'))
if num % 2 == 0:
    if num%3==0:
        print('你输入的数字可以整除2和3')
    else:
        print('你输入的数字可以整除2不能整除3')
else:
    if num%3==0:
        print('你输入的数字可以整除3不能整除2')
    else:
        print('你输入的数字不能整除3和2')
    
