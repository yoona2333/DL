
import numpy as np
import torch as th


# 两个张量的维度保持一致，对应元素直接做相应的操作
# 矩阵的乘法 两个张量，第一个张量的列数必须与第二个张量的行数相同，才能进行矩阵乘法操作
# (a,b)*(b,c)=(a,c)

def dem1():
    t1 = th.tensor([[1, 2], [3, 4]])
    t2 = th.tensor([[5, 6], [7, 8]])
    t3 = t1.multiply(t2)  # 张量的点乘操作
    print(t3)
    pass


def dem2(): #矩阵乘法 两个张量，第一个张量的列数必须与第二个张量的行数相同，才能进行矩阵乘法操作
    # (a,b)*(b,c)=(a,c)
    # 矩阵乘法的规则是：第一个矩阵的列数必须与第二个矩阵的行数相同，才能进行矩阵乘法操作
    t1 = th.tensor([[1, 2], [3, 4], [5, 6]])
    t2 = th.tensor([[5, 6], [7, 8]])
    t4 = t1 @ t2 # 矩阵乘法
    t3=t1.matmul(t2)
    print(t4)
    print(t3)
    # dot()只针对1维张量，不能对2维以上张量进行点乘操作
    pass


if __name__ == '__main__':
    # dem1()
    dem2()
