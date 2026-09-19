import torch
from networkx.algorithms.assortativity.mixing import degree_mixing_matrix


# torch.cat()/concat(tensors=, dim=): 在指定维度上进行拼接, 其他维度值必须相同, 不改变新张量的维度, 指定维度值相加
# tensors: 多个张量列表
#cat不改变维度数，拼接张量，除了拼接的那个维度外，其他维度必须保持一致
#stack() 会改变未读书
# dim: 拼接维度
def dm01():
    torch.manual_seed(0)
    t1 = torch.randint(low=1, high=10, size=(2, 3))
    print(f't1:{t1}, t1.shape:{t1.shape}')

    # t2 = torch.randn(2, 3)
    # print(f't2:{t2}, t2.shape:{t2.shape}')
    t2 = torch.randint(low=1, high=10, size=(2, 3))
    print(f't2:{t2}, t2.shape:{t2.shape}')
    t3 = torch.cat(tensors=[t1, t2], dim=0)
    print('t3->', t3)
    print('t3形状->', t3.shape)
    t4 = torch.concat(tensors=[t1, t2], dim=1)
    print('t4->', t4)
    print('t4形状->', t4.shape)


# torch.stack(tensors=, dim=): 根据指定维度进行堆叠, 在指定维度上新增一个维度(维度值张量个数), 新张量维度发生改变
# tensors: 多个张量列表
# dim: 拼接维度
def dm02():
	torch.manual_seed(0)
	t1 = torch.randint(low=0, high=10, size=(2, 3))
	t2 = torch.randint(low=0, high=10, size=(2, 3))
	t3 = torch.stack(tensors=[t1, t2], dim=0)
	# t3 = torch.stack(tensors=[t1, t2], dim=1)
	print('t3->', t3)
	print('t3形状->', t3.shape)

if __name__ == '__main__':
    # dm01()
    dm02()

