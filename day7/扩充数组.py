name=['小明','小红','小白']
print(name)
name.append('小雨')  #每次只能添加一个元素，被添加的元素自动添加到列表末尾
name.append(['小猫','小鸡','小狗'])#这种直接添加了数组
print(name)
name.insert(0,'小雨') #member.insert(a,b)a表示要追加的位置（注意起始位置为0），b表示被插入的元素
print(name)
name.extend(['小周','小李']) #以列表的形式追加新元素到原列表
print(name)