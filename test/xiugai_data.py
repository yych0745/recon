import torch
from torch import nn
import numpy as np
import scipy.io
import math
import numpy as np

x = torch.zeros(400, 461)
print(type(x))
# for i in np.arange(30.0, 50.05, 0.1):
#     file = str(round(i, 1)) + '-1500'
#     print(file)
#     x = scipy.io.loadmat("/Users/yych/repositry/Reconstruction_pxw/dataset/"+file+'.mat')['u']
#     # x -= 1000
#     print(x)
    # scipy.io.savemat("/Users/yych/repositry/Reconstruction_pxw/dataset/"+file+'_2.mat', {'u':x})
x = scipy.io.loadmat("/Users/yych/repositry/Reconstruction_pxw/dataset/matlab.mat")['t']
scipy.io.savemat("/Users/yych/repositry/Reconstruction_pxw/dataset/matlab_2.mat", {'u':x})
    # x -= 1000
print(x)
