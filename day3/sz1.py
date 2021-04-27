temp = input('猜测我设定的值')
num=int(temp)
while num!=8:
    num=int(input('错了，再来一次'))
    if num==8:
        print('厉害')
    else:
        if num>8:
            print('太大了')
        else:
            print('太小了')
print('结束')







