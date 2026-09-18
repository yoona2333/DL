import torch as th


def dem1():
    t1=th.tensor([1,2,3])

    t2=t1+10
    t3=t1.add(10)
    t1.add_(10) # 原地操作，修改原张量 等价于 t1=t1+10 t1+=10
    t4=t1.neg() # 取负号
    print(t1)
    print(t4)
    # print(t2)
    # print(t4)

    pass





if __name__ == '__main__':
    dem1()
