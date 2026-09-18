from filecmp import demo

import torch as th
from numpy import char


def demo1():
    # 直接创建指定的类型
    t1 = th.tensor([1, 2, 3, 4, 5], dtype=th.float32)
    print(f't1:{t1},类型:{type(t1)}')  # 查看张量的类型
    print(f't1:{t1},元素类型:{t1.dtype}')  # 查看张量的元素类型，默认是float32 内部存储的数据的类型

    t2 = t1.type(th.int16)
    print(f't2:{t2},元素类型:{t2.dtype}')  # 查看张量的元素类型
    print('-' * 100)

    print(t1.half())
    print('-' * 50)
    print(t1.float())  # float类型默认是float32类型
    print('-' * 50)
    print(t1.short())
    print('-' * 50)
    print(t1.int())
    print('-' * 50)
    print(t1.long())  #long类型默认是int64类型
    print('-' * 50)


if __name__ == '__main__':
    demo1()
