secret=123456
temp=input('请输入密码：')
while not temp.isdigit():
    temp=input('请输入正确形式')
num=int(temp)
n=3
while num!=secret:
    num = int(input('错误，请再次输入:'))
if num==secret:
    print('正确')





