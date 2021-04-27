import random
n=random.randint(1,100)
while n:
    print(' '*(n-1)+'*'*n)
    n=n-1             #另一种表达：n-=1