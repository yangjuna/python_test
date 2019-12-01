# coding=utf-8
#学习函数

# def add(*args):  #定义函数
#     total = 0
#     for val in args:   #循环遍历
#         total +=val
#     return total
#
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 3, 5, 7, 9))
#
#
# # 两个名称相同的函数 ,避免可以选用导入的时候自定义名称
#
# def foo():
#     print('hello word')
#
# def foo():
#     print('holle python')
# print(foo())
#
# #避免导入的时候执行代码，需要在被导入的文件中加上__main__,样例如下：
# def foo():
#     pass
# if __name__ == '__main__':
#     print(foo())


#学习函数中变量的作用域;      实际开发中减少全局变量的引用     ①作用域广泛 ②占内存时间长无法垃圾回收       ③降低耦合度
# def foo():
#     b='hello'               #局部变量b,在函数外部不能访问
#     global a                  #声明a 为全局变量
#     a=200                    #在函数里边，优先取局部变量
#     def bar():
#         c=True                    #局部变量a
#         print(a)
#         print(b)
#         print(c)
#     bar()
# if __name__ == '__main__'  :
#     a=100            #定义全局变量 作用于全局
#     foo()
#     print(a)


#学习字符串和常用数据结构
# s1 ='hello word'
# s2 ="hello python"
# #三个单引号可以换行
# s3 ='''
# hello
# birthday!
# '''
# print(s1 ,s2 ,s3 ,end='')
# # \表示转义      ,不希望\表示转义，前方价格r
#
# s1 ='\'hello word\''
# print(s1)
# s1 =r'\'hello word\''
# print(s1)

#字符的运算    +运算符来实现字符串的拼接，可以使用*运算符来重复一个字符串的内容，可以使用in和not in来判断一个字符串是否包含另外一个字符串（成员运算），我们也可以用[]和[:]运算符从字符串取出某个字符或某些字符（切片运算）
# s1 ='hello'*3
# print(s1)
# s2 ='word'
# s3=s1+s2
# print(s3)
#
# print('ll' in s1)   #判断是否包含
#
# s4 ='abcdefg1213145678'
#
# print(s4[0:2])  #取前三个值
# print(s4[:3])
# print(s4[:-1])
# print(s4[::-1])  #倒序
# str1 = 'hello, world!'
# # 通过内置函数len计算字符串的长度
# print(len(str1)) # 13
# # 获得字符串首字母大写的拷贝
# print(str1.capitalize()) # Hello, world!
# # 获得字符串每个单词首字母大写的拷贝
# print(str1.title()) # Hello, World!
# # 获得字符串变大写后的拷贝
# print(str1.upper()) # HELLO, WORLD!
# # 从字符串中查找子串所在位置
# print(str1.find('or')) # 8
# print(str1.find('shit')) # -1
# # 与find类似但找不到子串时会引发异常
# # print(str1.index('or'))
# # print(str1.index('shit'))
# # 检查字符串是否以指定的字符串开头
# print(str1.startswith('He')) # False
# print(str1.startswith('hel')) # True
# # 检查字符串是否以指定的字符串结尾
# print(str1.endswith('!')) # True
# # 将字符串以指定的宽度居中并在两侧填充指定的字符
# print(str1.center(50, '*'))
# # 将字符串以指定的宽度靠右放置左侧填充指定的字符
# print(str1.rjust(50, ' '))
# str2 = 'abc123456'
# # 检查字符串是否由数字构成
# print(str2.isdigit())  # False
# # 检查字符串是否以字母构成
# print(str2.isalpha())  # False
# # 检查字符串是否以数字和字母构成
# print(str2.isalnum())  # True
# str3 = '  jackfrued@126.com '
# print(str3)
# # 获得字符串修剪左右两侧空格之后的拷贝
# print(str3.strip())

#格式化输出字符串

# a,b=5,10
# print('%d * %d = %d' % (a,b,(a*b)))
# print('{} * {} = {}'.format(a,b,(a*b)) )
# print(f'{a} * {b} = {a*b}')              #python 3.6的写法
# 
#
# #列表[]
# a=[1,'a',2,'b',3,'c']
# print(a[2])
# print(len(a))
# print(a[-1])
# print(a[0:2])
# for index in range(len(a)):
#     print(a[index])
# for b in a:
#     print(b)
# for index, elem in enumerate(a):      #  通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
#     print(index, elem)
# a= [1,2,3,4,5]
# a.append(6)         #列表最后最佳
# print(a)
# a.remove(1)         #列表移除
# print(a)
# a.pop(2)               #弹出列表指定位置
# print(a)
# a=[9,8,7,6,5,4,3]
# if 9 in a:
#     a.remove(9)
#     print(a)
# print(a.clear())  #清空列表
#
# #列表的切片操作和字符串一样，不在进行重复操作




#用生成器创建列表

# f =[x for x in range(1,10)]
# print(f)
#
# f =[x+y for x in 'abc' for y in '123']
# print(f)
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a
def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()
