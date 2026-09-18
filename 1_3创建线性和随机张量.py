import torch as th


# 定义函数 演示创建线性张量
# th.manual_seed(3)
def dem1():
    t1 = th.arange(0, 10, 2)  # 创建一个0-9之间的线性张量，步长为2 ，元素为0,2,4,6,8 包左不包右 参数起始值，结束值，步长
    print(t1)
    print(f'-' * 30)

    t2 = th.linspace(0, 10, 4)  # 包左也包右 等差数列 参数起始值，结束值，等差元素的个数
    print(t2)
    print(f'-' * 30)


def dem2():
    # th.initial_seed()  # 系统默认采取当前时间戳作为随机种子

    th.manual_seed(3)  # 手动设置随机种子，每次运行结果都相同

    t1 = th.rand(size=(2, 3))  # 创建一个2*3的随机张量，元素在0-1之间
    print(t1)
    print(f'-' * 30)


def dem3():
    t1 = th.randn(size=(2, 3))  # 创建一个2*3的随机张量，元素服从标准正态分布
    print(f't1:{t1},type:{type(t1)}')
    print(f'-' * 30)


def dem4():
    th.manual_seed(3)
    t1 = th.randint(low=0, high=10, size=(2, 3))  # 创建一个2*3的随机整量，元素在0-9之间
    print(f't1:{t1},type:{type(t1)}')
    print(f'-' * 30)

    t2=th.randn(size=(2, 3))  # 创建一个2*3的随机张量，元素服从标准正态分布 ，均值为0，标准差为1
    print(f't2:{t2},type:{type(t2)}')
    print(f'-' * 30)




if __name__ == '__main__':
    # dem1()
    # dem2()
    # dem3()
    dem4()

# t1=th.ones((2,3),dtype=th.float32)
# print(t1)
#
# t2=th.ones(10) # 创建一个10维的张量，元素全为1
# print(t2)
#
# t3=th.tensor(6)# 创建一个标量张量
# print(t3)
#
# t4 = th.ones((6,1))
# print(t4)
