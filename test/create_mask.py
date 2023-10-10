import torch
from torch import nn
import numpy as np
from scipy.io import loadmat 
import math

# x = torch.zeros(400, 461)
x = loadmat("/Users/yych/repositry/Reconstruction_pxw/test/mask.mat")['x']
print(x)
s = np.zeros((1, 400, 461))
# s[0][100][100] = 1
for i in range(1,400,1):
    for j in range(1, 461, 1):
        # x = i
        # y = j + 500
        # if round(math.sqrt(x * x + y * y), 0) in [520, 620, 720, 820, 920]:
        #     s[0][i][j] = 1
        if x[i][j] != 0:
            s[0][i][j] = 1
        #     print(i, j, x[i][j])
# print(x)
# s[0][300][19] = 0
# s[0][300][29] = 0
torch.save(s, 'ind_yych_new.pt')