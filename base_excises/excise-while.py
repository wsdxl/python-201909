'''
Python中的循环语句有 for 和 while
'''
# sum=0
# counter=1
# while counter <= 100:
#     sum+=counter
#     counter+=1
# print(sum)
'''
无限循环
我们可以通过设置条件表达式永远不为 false 来实现无限循环
'''
# while True:
#     num=int(input('请输入一个数字：'))
#     print('你输入的数是：',num)
# print('Good bye!')

# try:
#     while True:
#         num=int(input('请输入一个数字：'))
#         print('你输入的数是：',num)
# except ValueError:
#     print('你是在逗我吧！')

'''
while 循环使用 else 语句
'''
# count = 0
# while count < 5:
#     print('%d 小于5' % count)
#     count += 1
# else:
#     print('%d 大于或等于5' % count)

'''
for 实例中使用了 break 语句，break 语句用于跳出当前循环体
'''
# # sites = ["Baidu", "Google","Runoob","Taobao"]
# # for site in sites:
# #     if site == "Runoob":
# #         print("菜鸟教程!")
# #         break
# #     print("循环数据 " + site)
# # else:
# #     print("没有循环数据!")
# # print("完成循环!")
# for x in range(2,2):
#     print(x)

'''
循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 
false (以while循环)导致循环终止时被执行,但循环被break终止时不执行。
'''
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')