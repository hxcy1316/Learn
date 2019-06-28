# -*-coding:utf-8 -*-

from functools import reduce

# CHAR_TO_INT = {
#     '0':0,
#     '1':1,
#     '2':2,
#     '3':3,
#     '4':4,
#     '5':5,
#     '6':6,
#     '7':7,
#     '8':8,
#     '9':9
# }
#
# def str2int(s):
#     ints = map(lambda ch:CHAR_TO_INT[ch],s)
#     return reduce(lambda x,y:x*10+y,ints)
# print(str2int('0'))
# print(str2int('12300'))
# print(str2int('0012345'))

# CHAR_TO_FLOAT = {
#     '0': 0,
#     '1': 1,
#     '2': 2,
#     '3': 3,
#     '4': 4,
#     '5': 5,
#     '6': 6,
#     '7': 7,
#     '8': 8,
#     '9': 9,
#     '.': -1
# }
#
# def str2float(s):
#     nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
#     point = 0
#     def to_float(f, n):
#         nonlocal point
#         if n == -1:
#             point = 1
#             return f
#         if point == 0:
#             return f * 10 + n
#         else:
#             point = point * 10
#             return f + n / point
#     return reduce(to_float, nums, 0.0)
#
# print(str2float('0'))
# print(str2float('123.456'))
# print(str2float('123.45600'))
# print(str2float('0.1234'))
# print(str2float('.1234'))
# print(str2float('120.0034'))

# def f(x,y):
#     return x * y
#
# def prod(L):
#     return reduce(f,L)
#
# # print(list(map(f,[1,2,3,4,5,6,7,8,9])))
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')
# # print(prod([1,2,3,4,5,6,7,8,9]))
# 首字母大写函数 capitalize()
# def normalize(name):
#     return name.capitalize()
#
# L1=['adam','LISA','barT']
# L2=list(map(normalize,L1))
# print(L2)

#大小写转换函数upper()和lower(),isupper()，islower()，istitle()方法用来判断字符串的大小写
# def normalize(name):
#     return name[:1].upper() + name[1:].lower()
#
# if __name__ == '__main__':
#     L1 = ['adam', 'LISA', 'barT']
#     L2 = list(map(normalize, L1))
#     print(L2)

# Python内建的filter()函数用于过滤序列
# def is_odd(n):
#     return n%2==1
#
# print(list(filter(is_odd,[1,2,4,5,6,9,10,15])))
#
# def not_empty(s):
#     return s and s.strip()
#
# print(list(filter(not_empty,['A','B',None,'C',' '])))

# 请利用filter()筛选出回数,利用切片
# def is_palindrome(n):
#     return n == int(str(n)[::-1])
#
# # def is_palindrome(n):
# #     s=str(n)
# #     for i in range((len(s)+1)//2):
# #         if s[i] != s[-(i+1)]:
# #             return False
# #     return True
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

# Python内置的sorted()函数就可以对list进行排序，也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
# L=[36, 5, -12, 9, -21]
# L1=sorted(L) #默认情况下，对字符串排序，是按照ASCII的大小比较的
# L2=sorted(L,key=abs)
# print(L1,L2)
# S=['bob', 'about', 'Zoo', 'Credit']
# S1=sorted(S)
# S2=sorted(S,key=str.lower)
# print(S1,S2)

# -*- coding: utf-8 -*-

# from operator import itemgetter
#
# L = ['bob', 'about', 'Zoo', 'Credit']
#
# print(sorted(L))
# print(sorted(L, key=str.lower))
#
# students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#
# print(sorted(students, key=itemgetter(0)))
# print(sorted(students, key=lambda t: t[1]))
# print(sorted(students, key=itemgetter(1), reverse=True))

# def by_name(t):
#     return t[0].lower()
# L=[('Dob',75),('Adam',92),('Bart',66),('Cisa',88)]
# L1=sorted(L,key=by_name)
# print(L1)
#
# def by_scort(t):
#     return t[1]
# L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
# L1=sorted(L,key=by_scort,reverse=True)# 数字默认顺序是由低到高
# print(L1)

# def calc_sum(*args): #可变参数定义
#     ax = 0
#     for n in args:
#         ax = ax + n
#     return ax
#
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
# 匿名函数关键字lambda表示匿名函数，冒号前面的x表示函数参数,lambda x: x * x
# def is_odd(n):
#     return n % 2 == 1 # 转换为匿名函数 lambda n:n%2 ==1
#
# L = list(filter(is_odd, range(1, 20)))
# L1 = list(filter(lambda n:n % 2 == 1, range(1, 20)))
# print(L)
# print(L1)
# 装饰函数decorator()
# def now():
#     print('2019-02-14')
#
# f=now  #f赋值为函数
# print(now.__name__)
# print(f.__name__) #f的函数名仍为now
# 在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# decorator就是一个返回函数的高阶函数。定义一个能打印日志的decorator
# def log(func):
#     def wrapper(*args,**kw):
#         *args,**kw)
#
# @log
# def now():
#     print('2019-02-14')
# decorator本身需要传入参数
# def log(text):
#     def decorator(func):
#         def wrapper(*args,**kw):
#             print('%s %s():'%text,func.__name__)
#             return func(*args,**kw)
#         return wrapper
#     return decorator
#
# @log('execute')
# def now():
#     print('2019-2-14')
#
# import functools  #导入functools模块
#
# def log(func):
#     @functools.wraps(func) #Python内置的functools.wraps作用等同于wrapper.__name__ = func.__name__
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# import functools
#
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
# 设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
# -*- coding: utf-8 -*-
# import time,functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         t1=time.time()
#         r=func(*args, **kw)
#         print('%s excute in %s ms' %(func.__name__,1000*(time.time()-t1)))
#         return r
#     return wrapper

# import time,functools
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args,**kw):
#         print('%s executed in %s ms' % (fn.__name__, 10.24))
#         return fn(*args,**kw)
#     return wrapper
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z
#
# f = fast(11, 22)
# s = slow(11, 22, 33)

# 偏函数 functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
# import functools
# int2 = functools.partial(int,base=2)
# print('1000000=',int2('1000000'))
# print('1010101=',int2('1010101'))
# import sys
# def test():
#     args = sys.argv
#     if len(args)==1:
#         print('Hello, world')
#     elif len(args)==2:
#         print('Hello, %s' % args[1])
#     else:
#         print('Too many arguments!')
#
# if __name__ =='__main__':
#     test()
# 安装pyminizip包
# import pyminizip
# compression_level = 5 # 1-9
# pyminizip.compress("src.txt", "dst.zip", "password", compression_level)

# import os,sys,subprocess
# rc = subprocess.call(['7z', 'a', '-pP4$$W0rd', '-y', 'myarchive.zip'] +
#                      ['first_file.txt', 'second.file'])

