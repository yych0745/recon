import matplotlib.pyplot as plt
from scipy.io import loadmat 

# path = "/Users/yych/repositry/Reconstruction_pxw/dataset/data/90.0-1500.mat"
path = "mask.mat"
ut = loadmat(path)['x']
plt.imshow(ut,cmap=plt.get_cmap('hot'), origin = 'lower')
# ut = loadmat("/Users/yych/repositry/Reconstruction_pxw/dataset_back/matlab.mat")['t']
# plt.imshow(ut,cmap=plt.get_cmap('hot'), origin = 'lower')
plt.colorbar()
plt.show()

# for idi, i in enumerate(cnd):
#     for idz, z in enumerate(i):
#         if z > 0:
#             print(idi, idz, z)
