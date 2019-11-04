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

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
# 列表切片
fruits2 = fruits[1:4]
print(fruits2)