# print('输入学生成绩自动计算优良')
# score =  float(input('请输入成绩：'))
# if score >90:
#     print('学生成绩为%2f，成绩优秀' % score)
# elif score >= 60:
#     print('学生成绩为%2f,成绩良好' % score)
# else:
#     print('学生成绩为%2f，成绩差' % score)

#猜数字游戏
# import  random
# print("猜猜我心里的数字：请输入0-100的数字")
# i=1
# a = random.randint(0,100)
# b = int(input("请输入数字："))
# while a != b :
#     if b >a :
#         print('您第%s次输入的数字大于电脑，请重新输入'% i)
#         b = int(input("请输入数字："))
#         i=i+1
#     elif b<a:
#         print('您第%s次输入的数字小于电脑，请重新输入' % i)
#         b = int(input("请输入数字："))
#         i = i + 1
# else:
#     print("恭喜你第%s次答对了数字是%s"%(i,a))


#99乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print()
# num = int(input('num = '))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print(reversed_num)

#引用模块
# from  module2 import foo
# foo()
#
# import module3


# def foo():
#     a = 200
#     print(a)  # 200
#
#
# if __name__ == '__main__':
#     a = 100
#     foo()
#     print(a)  # 100


#字符
# s1 ='hello word'
# s2 ='good \'morning\''
#
# print(s1,s2,end='')
#
# s1 = r'\'hello, world!\''
# s2 = r'\n\\hello, world!\\\n'
# print(s1, s2, end='')


# name = 'yangjun'
# name1 = 'ztl'
# print(name*3)
# name+=name1
# print(name)
#
# print('yang' in name)
# print('yang' not in name)

# str1= 'qwertyuioplkjhg'
# print(str1[1:3])
# print(str1[::2])#每个间隔2
# print(str1[::-1])#倒叙
#
#
# str2= 'hello  chengchuang'
# print(len(str2))#获取字符串长度
# print(str2.capitalize())#将首字母改为大写
# print(str2.title())
# print(str2.find('cheng'))#查找字符串位置
# print(str2.find('666'))#查找不存在字符串会输出-1
# print(str2.index('hello'))#检查字符串是否以指定开头
# a,b=5,10
# print('%d * %d = %d' %(a ,b,a*b) )
# print('{0}*{1}={2}'.format(a,b,a*b))
# print(f'{a}*{b}={a*b}')#p3的写法


#列表学习
# list1 = [1,2,3,4,5,6,7,8,9]
# print(list1)
# list2 =['hello'] *3
# print(list2)
# list1[2]=300
# print(list1)#替换第三个数
# for index in range(len(list1)):
#     print(list1[index])
# for i in list1:
#     print(i)
#
# for index, elem in enumerate(list1):
#     print(index, elem)

# cc = ['yj','ztl','sjx','jp','hhs']
# cc.append('tsq')
# cc.insert(0,'lp')
# print(cc)
# list2 =[1000,2000]
# cc.extend(list2)
# print(cc)
# cc.pop(1)#弹出第二个元素
# print(cc)
# print(cc.pop(len(cc) - 1))
# print(cc.clear())#清空列表

# fruits = ['grape', 'apple', 'strawberry', 'waxberry']
# fruits += ['pitaya', 'pear', 'mango']
# # 列表切片
# fruits2 = fruits[1:4]
# print(fruits2)
#
# list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# list2 = sorted(list1)
# # sorted函数返回列表排序后的拷贝不会修改传入的列表
# # 函数的设计就应该像sorted函数一样尽可能不产生副作用
# list3 = sorted(list1, reverse=True)
# # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
# list4 = sorted(list1, key=len)
# print(list1)
# print(list2)
# print(list3)
# print(list4)
# # 给列表对象发出排序消息直接在列表对象上进行排序
# list1.sort(reverse=True)
# print(list1)
# #列表生成器
# f = [x for x in range(1, 10)]
# print(f)
# f = [x + y for x in 'ABCDE' for y in '1234567']
# print(f)
#
# import sys
# f = (x ** 2 for x in range(1, 1000))
# print(sys.getsizeof(f))
# for val in f:
#     print(val)

#yield 斐波那契数列
# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a
#
#
# def main():
#     for val in fib(20):
#         print(val)
#
#
# if __name__ == '__main__':
#     main()



# #元组内容不允许修改，但是可以转换为列表，元组在创建时间和占用的空间上面都优于列表
# # 定义元组
# t = ('杨军', 25, True, '山东青岛')
# print(t)
# # 获取元组中的元素
# print(t[0])
# print(t[3])
# # 遍历元组中的值
# for member in t:
#     print(member)
# # 重新给元组赋值
# # t[0] = '王大锤'  # TypeError
# # 变量t重新引用了新的元组原来的元组将被垃圾回收
# t = ('王大锤', 20, True, '云南昆明')
# print(t)
# # 将元组转换成列表
# person = list(t)
# print(person)
# # 列表是可以修改它的元素的
# person[0] = '李小龙'
# person[1] = 25
# print(person)
# # 将列表转换成元组
# fruits_list = ['apple', 'banana', 'orange']
# fruits_tuple = tuple(fruits_list)
# print(fruits_tuple)

#
#
# #集合不允许有重复数据
# set1 = {1, 2, 3, 3, 3, 2}
# print(set1)
# print('Length =', len(set1))
# # 创建集合的构造器语法(面向对象部分会进行详细讲解)
# set2 = set(range(1, 10))
# set3 = set((1, 2, 3, 3, 2, 1))
# print(set2, set3)
# # 创建集合的推导式语法(推导式也可以用于推导集合)
# set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
# print(set4)
# #象集合中添加元素
# set1.add(199)
# print(set1)
# set2.update([11, 12])
# print(set2)
# set2.discard(5)#丢弃
# print(set2)
#
#
# if 4 in set2:
#     set2.remove(4)#移除
# print(set1, set2)
# print(set3.pop())#弹出第一个元素
# print(set3)
#
#
# # 集合的交集、并集、差集、对称差运算
# print(set1 & set2)
# # print(set1.intersection(set2))
# print(set1 | set2)
# # print(set1.union(set2))
# print(set1 - set2)
# # print(set1.difference(set2))
# print(set1 ^ set2)
# # print(set1.symmetric_difference(set2))
# # 判断子集和超集
# print(set2 <= set1)
# # print(set2.issubset(set1))
# print(set3 <= set1)
# # print(set3.issubset(set1))
# print(set1 >= set2)
# # print(set1.issuperset(set2))
# print(set1 >= set3)
# # print(set1.issuperset(set3))

# 创建字典的字面量语法
scores = {'杨军': 92, '白元芳': 78, '狄仁杰': 82}
print(scores)
# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1, items2, items3)