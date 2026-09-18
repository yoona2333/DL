import torch as th
import numpy as np



def dem1():
    t1=th.tensor([1,2,3,4,5]) # 创建一个1维的张量，元素为1,2,3,4,5
    t2=th.tensor(t1)
    print(f't1:{t1},type:{type(t1)}')
    print(f't2:{t2},type:{type(t2)}')

    n1=t1.numpy() # 将张量转换为numpy数组
    n2=t1.numpy().copy() # 将张量转换为numpy数组的拷贝 ，与张量是独立的内存空间 ，修改拷贝不会影响张量 深拷贝
    print(f'n1:{n1},type:{type(n1)}')

    n1[0]=100# 修改numpy数组的第一个元素为100 ，张量也会被修改 ，因为张量和numpy数组是共享内存的
    n2[0]=200# 修改numpy数组的第一个元素为200 ，张量不会被修改 ，因为张量和numpy数组是独立的内存空间
    print(f'n1:{n1},type:{type(n1)}')
    print(f't1:{t1},type:{type(t1)}')
    print(f'n2:{n2},type:{type(n2)}')
    print(f't2:{t2},type:{type(t2)}')



    pass


def dem2():

    n1=np.array([11,22,33,44,55])
    print(f'n1:{n1},type:{type(n1)}')
    t1=th.from_numpy(n1) # 将numpy数组转换为张量 ，与numpy数组是共享内存的 ，修改张量也会被numpy数组修改
    t2=t1.type(th.float32)
    t3=th.from_numpy(n1).type(th.float32) #数据类型发生变化，必须分配新内存，把数值转换后复制过去**，返回全新张量
    t4=th.tensor(n1)  # 将numpy数组转换为张量 ，与numpy数组是独立的内存空间 ，修改拷贝不会影响张量 深拷贝
    n1[0]=100
    print(f'n1:{n1},type:{type(n1)}')
    print(f't1:{t1},type:{type(t1)}')
    print(f't2:{t2},type:{type(t2)}')
    print(f't3:{t3},type:{type(t3)}')
    print(f't4:{t4},type:{type(t4)}')
    pass


def dem3():
    t1=th.tensor(100.3)
    # t2=th.tensor(200,) 这种可以理解为标量

    t3=th.tensor(200,300)
    print(f't1:{t1},type:{type(t1)}')
    a=t3.item()
    print(f'a:{a},type:{type(a)}')
    t2=t1.item()
    b=t3.item() #只能将1维张量转换为标量，2维以上量不能转换为标量
    print(f'a:{a},type:{type(a)}')
    print(f'b:{b},type:{type(b)}')

    print(f't2:{t2},type:{type(t2)}')
    pass


def dem4():
    pass

if __name__ == '__main__':
    # dem1()
    # dem2()
    dem3()
