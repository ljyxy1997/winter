import random
secret=random.randint(1,10)               #产生随机值
temp = input('猜测我设定的值')
while not temp.isdigit():
    temp=input("请输入一个数字：")
    num=int(temp)
n=1
while temp!=secret:
    temp=int(input('错了，再来一次'))
    if temp==secret:
        print('厉害')
    else:
        if temp>secret:
            print('太大了')
        else:
            print('太小了')
            n=n+1
    if n > 3:
        break


print('结束')