from numpy import mean
import torch as th


def dem1():
    t1 = th.tensor([
        [1, 2],
        [3, 4]
    ], dtype=th.float32)

    print(t1.sum())
    print(t1.sum(dim=0))  # dim=0即对每一列进行求和
    print(t1.sum(dim=1))  # dim=1即对每一行进行求和
    print('-' * 50)

    print(t1.max())
    print(t1.max(dim=0))  # dim=0即对每一列进行求最大值
    print(t1.max(dim=1))  # dim=1即对每一行进行求最大值
    print('-' * 50)

    print(t1.mean())  # 对张量的所有元素进行求平均值
    print(t1.mean(dim=0))  # dim=0即对每一列进行求平均值
    print(t1.mean(dim=1))  # dim=1即对每一行进行求平均值
    pass

    # pow()#n次方
    # sqrt()#开平方
    #exp()#指数函数
    #log()#对数函数
    #log2()#以2为底的对数函数
    #log10()#以10为底的对数函数



if __name__ == '__main__':
    dem1()
