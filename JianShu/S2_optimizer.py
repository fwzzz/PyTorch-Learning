import torch
from torch.autograd import Variable
import torch.nn.functional as F


x = Variable(torch.randn(10, 20), requires_grad=False)
y = Variable(torch.randn(10, 3), requires_grad=False)

# define some weights
w1 = Variable(torch.randn(20, 5), requires_grad=True)
w2 = Variable(torch.randn(5, 3), requires_grad=True)

learning_rate = 0.2
loss_fn = torch.nn.MSELoss()
optimizer = torch.optim.SGD([w1, w2], lr=learning_rate)

iter_max = 5000
for step in range(iter_max):

    # pred = F.sigmoid(x @ w1)
    # pred = F.sigmoid(pred @ w2)   # nn.functional.sigmoid is deprecated. Use torch.sigmoid instead.

    pred = torch.sigmoid(x @ w1)
    pred = torch.sigmoid(pred @ w2)
    loss = loss_fn(pred, y)
    print(loss)

    # manually zero all previous gradients
    optimizer.zero_grad()
    # calculate new gradients
    loss.backward()
    # apply new gradients
    optimizer.step()
























