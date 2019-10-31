print('输入学生成绩自动计算优良')
score =  float(input('请输入成绩：'))
if score >90:
    print('学生成绩为%2f，成绩优秀' % score)
elif score >= 60:
    print('学生成绩为%2f,成绩良好' % score)
else:
    print('学生成绩为%2f，成绩差' % score)
