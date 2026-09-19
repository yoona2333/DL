import torch


# torch.cat()/concat(tensors=, dim=): 在指定维度上进行拼接, 其他维度值必须相同, 不改变新张量的维度, 指定维度值相加
# tensors: 多个张量列表
# dim: 拼接维度
def dm01():
    torch.manual_seed(0)
    t1 = torch.randint(low=0, high=10, size=(2, 3))
    t2 = torch.randint(low=0, high=10, size=(2, 3))
    t3 = torch.cat(tensors=[t1, t2], dim=0)
    print('t3->', t3)
    print('t3形状->', t3.shape)
    t4 = torch.concat(tensors=[t1, t2], dim=1)
    print('t4->', t4)
    print('t4形状->', t4.shape)


if __name__ == '__main__':
    dm01()
