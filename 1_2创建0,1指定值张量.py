import torch as th

t1=th.ones(3,4) # 创建全为1的张量
print(f't1:{t1},type:{type(t1)}')
print('-'*30)

t2=th.tensor([[1,2],[3,4],[5,6]]) # 创建一个2维张量
print(f't2:{t2},type:{type(t2)}')

t3=th.ones_like(t2) # 创建与t2形状相同的张量，元素全为1的张量
print(f't3:{t3},type:{type(t3)}')

t4=th.zeros(3,4) # 创建全为0的张量
print(f't4:{t4},type:{type(t4)}')

t5=th.zeros_like(t2)
print(f't5:{t5},type:{type(t5)}')

print('-'*30)

t6= th.full((4,4),255) # 创建全为255的张量
print(f't6:{t6},type:{type(t6)}')

t7=th.full_like(t2,255)
print(f't7:{t7},type:{type(t7)}')

