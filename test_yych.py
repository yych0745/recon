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
import torch
from torch.utils.data import DataLoader
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import src.loss as loss
from src.data.dataset import MyNewData
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


def test(logname1, logname2, logname3, datasetname):
    '''
    测试模型效果
    '''
    st = time.time()   #  测试开始时间
    print('model = ' + str(logname2) + '+' + str(logname3) + ' \ndataset = ' + str(datasetname), l_test)

    # 读取UNet模型
    tfr_path1 = 'results/' + str(logname1) + '/' + str(logname2) + '.pt'
    tfr_path2 = 'results/' + str(logname1) + '/' + str(logname2) + '_params.pt'
    net = torch.load(tfr_path1)                           #载入模型
    print("net:", net)
    net.load_state_dict(torch.load(tfr_path2))            #载入参数

    if logname3 != None:
        # 读取MLP模型
        mlp_path1 = 'results/vp/MLP/' + str(logname3) + '.pt'
        mlp_path2 = 'results/vp/MLP/' + str(logname3) + '_params.pt'
        mlp = torch.load(mlp_path1)                           #载入模型
        mlp.load_state_dict(torch.load(mlp_path2))            #载入参数
       
    # 评价指标
    MAE_epoch, CMAE_epoch = [], []                         # 记录每一个batch的 MAE, CMAE
    MAE, CMAE = 0.0, 0.0                                   # 记录测试误差 MAE, 组件平均误差CMAE 
    MaxAE_batch, MTAE_batch = [], []                       # 记录每一个batch的 MaxAE, MT-AE
    MaxAE_epoch, MTAE_epoch = 0.0, 0.0
    MaxAE, MTAE = [], []                                   # 记录每一个epoch的 MaxAE, MT-AE  
    criterion = torch.nn.L1Loss()                          # 训练loss, L1 loss, 亦可采用torch.nn.MSELoss(),效果相当
             

    net.eval()
    with torch.no_grad():
        for _, data in enumerate(test_iter):
            X, y = data
            X = X.to(device)
            y = y.to(device)
            output = net(X)                                              # UNet预测温度场

            print("y:", y.reshape(-1,1,200,200)[0,0,0,:])
            plt.subplot(1,2,1)
            plt.imshow(y.reshape(-1,1,200,200)[0,0,:,:])
            plt.subplot(1,2,2)
            plt.imshow(output.reshape(-1,1,200,200)[0,0,:,:])
            plt.show()
            print("output:", output)

        #     if logname3 != None:
        #         observation_y = X[X > 0]                                 # 提取温度测点数据
        #         observation_y = (observation_y - 298) / 50               # 归一化
        #         # print(i, observation_y.shape)
        #         observation_y = observation_y.reshape(-1, num_input)            # MLP输入                                
        #         heatsink_y = mlp(observation_y)                          # MLP预测温度场
        #         heatsink_y = (heatsink_y * 50) + 298                     # 归一化后还原
        #         heatsink_y = heatsink_y.reshape(-1, 1, 2, 26)            # MLP 输出

        #         output[:, :, 0:2, 86:112] = heatsink_y                   # 热沉区域替换
           
        #     l2 = criterion(y, output)                                    # MAE loss, 第一评价指标
        #     lc2 = criterion(y * cnd, output * cnd)                       # 组件loss,第二评价指标 
        #     MAE += l2.cpu().item() * y.size(0)
        #     CMAE += lc2.cpu().item() * y.size(0)

        #     MAE_epoch.append(l2.cpu().item())
        #     CMAE_epoch.append(lc2.cpu().item())
            
        #     MaxAE_batch, MTAE_batch = loss.loss_error(output, y, batch_size)       # 调用函数获取每个batch的MaxAE和MTAE
        #     MaxAE.append(MaxAE_batch.cpu().numpy().tolist())                       # 将每个batch的MaxAE加入列表
        #     MTAE.append(MTAE_batch.cpu().numpy().tolist())                         # 将每个batch的MTAE加入列表

        # np.savetxt("error_distr/Distribution_MAE.txt", np.array(MAE_epoch))
        # np.savetxt("error_distr/Distribution_CMAE.txt", np.array(CMAE_epoch))
        # np.savetxt("error_distr/Distribution_MaxAE.txt", np.array(MaxAE))
        # np.savetxt("error_distr/Distribution_MTAE.txt", np.array(MTAE))
        # # print('MAE', len(MAE_epoch), '\n', MAE_epoch, '\n', 'CMAE', len(CMAE_epoch), '\n', CMAE_epoch)
        
        # print('MAE', torch.mean(torch.tensor(MAE_epoch).reshape(-1)), '\n', 'CMAE', torch.mean(torch.tensor(CMAE_epoch).reshape(-1)))

        # MaxAE = torch.tensor(MaxAE).reshape(-1)
        # MTAE = torch.tensor(MTAE).reshape(-1)
        # print('MaxAE', MaxAE.shape, '\n', MaxAE, '\n', 'MTAE', MTAE.shape, '\n', MTAE)

        # # MaxAE_epoch = torch.max(MaxAE)                                      # 全局最大误差 
        # # MTAE_epoch = torch.max(MTAE)                                        # 全局最高温度误差
        # MaxAE_epoch = torch.mean(MaxAE)                                      # 平均最大误差 
        # MTAE_epoch = torch.mean(MTAE)                                        # 平均最高温度误差

        # print('MAE: {:.6f} \nCMAE: {:.6f} \nMaxAE: {:.6f} \nMT-AE: {:.6f} \ntime {:.1f}s' \
        # .format(MAE / l_test, CMAE / l_test, MaxAE_epoch, MTAE_epoch, time.time() - st))


if __name__ == '__main__':
    '''
    主函数,读取测试集,测试不同模型的效果
    '''

    '''------------------------------------Case 1------------------------------------'''
    cnd = torch.load('ind/cnd_c1.pt')
    cnd = cnd.to(device)   

    '''第一大类,general数据集测试'''
    ind = torch.load('ind/ind_4.pt')
    # ind = torch.load('ind/ind_4_refine.pt')
    root = 'dataset/'
    test_path = 'test.txt'  
    test_dataset = MyNewData(root, test_path, ind, None)
    batch_size = 1 
    test_iter  = DataLoader(test_dataset, batch_size = batch_size, shuffle= False, num_workers=16)
    l_test = test_dataset.__len__()                               
    ind = torch.load('ind/ind_4.pt')
    cnd = torch.load('ind/cnd_c1.pt')
    # plt.subplot(1,2,1)
    # plt.imshow(ind.reshape(-1,1,200,200)[0,0,:,:])
    # plt.subplot(1,2,2)
    # plt.imshow(cnd.reshape(-1,1,200,200)[0,0,:,:])
    # plt.show()
    # ind = ind.reshape(1, 200, 200)
    # print(ind.shape)
    # num_input = 16      
    test('lr0.005_UNetV2', 'lr0.005_UNetV2_30epoch', None, 'test.txt')
    # test('vp_10_c1_0.1grad_4ob_UNetV2', 'vp_10_c1_0.1grad_4ob_UNetV2_200epoch', None, 'test.txt')
    # test('vp_10_c1_0.1grad_4ob_UNetV2', 'vp_10_c1_0.1grad_4ob_UNetV2_200epoch', 'vp_10_c1_4ob_MLP_100epoch', 'test.txt')




