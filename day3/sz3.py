import random
secret=2            #产生随机值
temp = input('猜测我设定的值')
num=int(temp)
n=1
while num!=secret:
    num=int(input('错了，再来一次'))
    if num==secret:
        print('厉害')
    else:
        if num>secret:
            print('太大了')
        else:
            print('太小了')
            n=n+1
    if n>3:
        break

print('结束')
