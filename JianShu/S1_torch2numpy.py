import torch
import numpy as np

numpy_tensor = np.random.randn(10, 20)

# convert numpy array to pytorch array
pytorch_tensor1 = torch.Tensor(numpy_tensor)

# another way
pytorch_tensor2 = torch.from_numpy(numpy_tensor)

# convert torch tensor to numpy representation
pytorch_tensor1.numpy()

# use tensor on GPU provide another type
dtype = torch.cuda.FloatTensor
gpu_tensor1 = torch.randn(10, 20).type(dtype)

# or just call 'cuda()' method
gpu_tensor2 = pytorch_tensor1.cuda()

# call back to the CPU
cpu_tensor = gpu_tensor1.cpu()

# define pytorch tensors
x = torch.randn(10, 20)
y = torch.ones(20, 5)

# '@' means matrix multiplication
res = x @ y
print("x:", x)
print("y:", y)
print("res:", res)

# get the shape
res.shape
print(res.shape)
