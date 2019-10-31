# print('输入学生成绩自动计算优良')
# score =  float(input('请输入成绩：'))
# if score >90:
#     print('学生成绩为%2f，成绩优秀' % score)
# elif score >= 60:
#     print('学生成绩为%2f,成绩良好' % score)
# else:
#     print('学生成绩为%2f，成绩差' % score)

import  random
print("猜猜我心里的数字：请输入0-100的数字")
i=1
a = random.randint(0,100)
b = int(input("请输入数字："))
while a != b :
    if b >a :
        print('您第%s次输入的数字大于电脑，请重新输入'% i)
        b = int(input("请输入数字："))
        i=i+1
    elif b<a:
        print('您第%s次输入的数字小于电脑，请重新输入' % i)
        b = int(input("请输入数字："))
        i = i + 1
else:
    print("恭喜你第%s次答对了数字是%s"%(i,a))
