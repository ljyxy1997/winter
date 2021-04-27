secret=123456
time=3
n=0
while time>0 and n==0:
    time-=1
    temp = input('请输入：')
    while not temp.isdigit():
        temp=(input('请输入正确形式：'))
    num=int(temp)
    if num==secret:
        print('输入正确')
        break
    else:
        print('输入错误')




