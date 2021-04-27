name=['小明','小红','小白','小猫','小鸡','小狗']
print(name[1])
name.remove('小明')
print(name)
del name[1]
print(name)
print( name.pop()) #弹出最后一个元素
print(name.pop(1)) #指定弹出位置
name1=['小明','小红','小白','小猫','小鸡','小狗']
print(name1[1:3]) #控制范围
print(name1[:])   #获得整个数组