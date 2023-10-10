import torch
import matplotlib.pyplot as plt
cnd = torch.load('../ind/ind_yych.pt')
print(type(cnd[0]))
figure, ax = plt.subplots(1, 1)
patch = ax.patch
patch.set_color("white")
print(cnd)
plt.imshow(cnd[0],cmap=plt.get_cmap('gray'), origin = 'lower')
plt.colorbar()
plt.show()

# for idi, i in enumerate(cnd):
#     for idz, z in enumerate(i):
#         if z > 0:
#             print(idi, idz, z)
