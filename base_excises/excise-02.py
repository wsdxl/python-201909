'''
条件语句
'''
# age=5
# if age>18:
#     print('your age is',age)
#     print('adult')
# else:
#     print('your age is',age)


# try:
#     s=int(input('请输入您的出生日期: '))
#     if s<2000:
#         print('您是00前')
#     else:
#         print('您是00后')
# except ValueError as e:
#     print('您输入的不是数字')
#     print('Goodbye')

'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''
# t=1.75
# w=80.5
# bmi=w/t**2
# if bmi<18.5:
#     print('过轻')
# elif bmi>=18.5 and bmi<25:
#     print('正常')
# elif bmi>=25 and bmi<28:
#     print('过重')
# elif bmi>=28 and bmi<32:
#     print('肥胖')
# else:
#     print('严重肥胖')

'''
计算1-100的整数之和
'''
# sum=0
# for x in range(101):
#     sum+=x
# print(sum)

# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)