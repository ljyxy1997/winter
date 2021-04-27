temp=input('请输入成绩：')
score=int(temp)
if 60<score<80:
    print(temp+'为C等级')
elif 80<score<90:
    print(temp + '为B等级')      #if与elif区别在于，多个if要一个一个去执行，但是elif只要有一个成立就不要执行其余的
elif 90<score:
    print(temp + '为A等级')
elif score<60:
    print(temp + '为D等级')
