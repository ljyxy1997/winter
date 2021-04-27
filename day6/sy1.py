n=6
q=3
while n>0:
    print(n)
    n-=1
    if q:
        print(q)
        q-=1
        if q<2:
            break  #这个break终止了while但是并不需要写在while下，只要顺着步骤写就行
