import torch
from torch.autograd import Variable


# define an inputs
x_tensor = torch.randn(10, 20)
y_tensor = torch.randn(10, 5)
x = Variable(x_tensor, requires_grad=False)
y = Variable(y_tensor, requires_grad=False)

# define some weights
w = Variable(torch.randn(20, 5), requires_grad=True)

# get variable tensor
print(type(w.data))     # torch.FloatTensor
# get variable gradient
print("grad1", w.grad)  # None

iter_max = 1000
for i in range(iter_max):
    loss = torch.mean((y - x @ w) ** 2)
    print("loss", loss)

    # calculate the gradients
    loss.backward()
    # print("grad2", w.grad)   # some gradients

    # manually apply gradients
    w.data -= 0.01 * w.grad.data

    # manually zero gradient after update
    w.grad.data.zero_()









