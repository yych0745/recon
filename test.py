# encoding: utf-8
#    Authors: Xingwen Peng
#    National University of Defense Technology, China
#    Defense Innovation Institute, Chinese Academy of Military Science, China
#    EMAIL: vincent1990@126.com
#    DATE:  Jun 2022
# ------------------------------------------------------------------------
# This code is part of the program that produces the results in the following paper:
#
# Peng, X., Li, X., Gong, Z., Zhao, X., Yao, W., 2022. A Deep Learning Method Based on Partition Modeling For reconstructing Temperature Field. SSRN Journal. https://doi.org/10.2139/ssrn.4065493
#
# You are free to use it for non-commercial purposes. However, we do not offer any forms of guanrantee or warranty associated with the code. We would appreciate your acknowledgement.
# ------------------------------------------------------------------------

import time
# import torch
import scipy.io
# from torch.utils.data import DataLoader
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
# import src.loss as loss
# from src.data.dataset import MyNewData
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

if __name__ == '__main__':
    train_log = np.load("/Users/yych/repositry/Reconstruction_pxw/results/lr0.005_UNetV2/train_log_200epoch.txt")
    print(train_log[:, 0])


