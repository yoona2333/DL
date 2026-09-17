import torch
import numpy as np
from sympy.codegen.fnodes import size

#torch.tensor()根据指定的数据创建张量
# 可以根据标量、向量、矩阵、数组等创建张量
#torch.Tensor()根据指定的维度创建张量，根据形状创建张量，默认创建的是0张量,已有数据不能指定类型
#Tensor与tensor的区别：Tensor可以直接根据形状创建张量


def demo01():
    t1=torch.tensor(10) # 创建一个标量张量
    print(f't1:{t1},type:{type(t1)}')

    print('-'*30)

    t2=torch.tensor([10,20,30]) # 创建一个向量张量
    print(f't2:{t2},type:{type(t2)}')
    print('-'*30)

    data=[10,20,30],[40,50,60] # 创建一个矩阵张量
    t3=torch.tensor(data,dtype=torch.float) # 创建一个矩阵张量
    print(f't3:{t3},type:{type(t3)}')
    print('-'*30)

    data=np.random.randint(0,10,size=(3,4)) # 创建一个3*4的矩阵张量 ，元素在0-9之间 行3 列4
    t4=torch.tensor(data) # 创建一个矩阵张量
    print(f't4:{t4},type:{type(t4)}')
    print('-'*30)

    #t5=torch.tensor(2,3) #尝试直接创建指定维度的张量
    #print(f't5:{t5},type:{type(t5)}')


    t6 = torch.Tensor(4,3)  # 尝试直接创建指定维度的张量
    print(f't6:{t6},type:{type(t6)}')

def demo02():
    t1=torch.Tensor(10) # 创建一个标量张量
    print(f't1:{t1},type:{type(t1)}')

    print('-'*30)

    t2=torch.Tensor([10,20,30]) # 创建一个向量张量
    print(f't2:{t2},type:{type(t2)}')
    print('-'*30)

    data=[10,20,30],[40,50,60] # 创建一个矩阵张量
    t3=torch.Tensor(data) # 创建一个矩阵张量
    print(f't3:{t3},type:{type(t3)}')
    print('-'*30)

    data=np.random.randint(0,10,size=(3,4)) # 创建一个3*4的矩阵张量 ，元素在0-9之间 行3 列4
    t4=torch.Tensor(data) # 创建一个矩阵张量
    print(f't4:{t4},type:{type(t4)}')
    print('-'*30)

    t5=torch.Tensor(2,3) #尝试直接创建指定维度的张量
    print(f't5:{t5},type:{type(t5)}')


    t6 = torch.Tensor(4,3)  # 尝试直接创建指定维度的张量
    print(f't6:{t6},type:{type(t6)}')

def demo03():
    t1=torch.IntTensor(10) # 创建一个标量张量
    print(f't1:{t1},type:{type(t1)}')

    print('-'*30)

    t2=torch.IntTensor([10,20,30]) # 创建一个向量张量
    print(f't2:{t2},type:{type(t2)}')
    print('-'*30)

    data=[10,20,30],[40,50,60] # 创建一个矩阵张量
    t3=torch.IntTensor(data) # 创建一个矩阵张量
    print(f't3:{t3},type:{type(t3)}')
    print('-'*30)
    
    
    data=[10,20,30],[40,50,60] # 创建一个矩阵张量
    t4=torch.FloatTensor(data) # 创建一个矩阵张量
    print(f't4:{t4},type:{type(t4)}')
    print('-'*30)

    data=np.random.randint(0,10,size=(3,4)) # 创建一个3*4的矩阵张量 ，元素在0-9之间 行3 列4
    t8=torch.IntTensor(data) # 创建一个矩阵张量
    print(f't8:{t8},type:{type(t8)}')
    print('-'*30)

    #t5=torch.tensor(2,3) #尝试直接创建指定维度的张量
    #print(f't5:{t5},type:{type(t5)}')


    t6 = torch.IntTensor(4,3)  # 尝试直接创建指定维度的张量
    print(f't6:{t6},type:{type(t6)}')




if __name__=='__main__': # 主函数 解释：当脚本作为主程序运行时，会执行主函数中的代码
    # demo01()
    # demo02()
    demo03()