import numpy as np
import pandas as pd

img_r = np.array([ [1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],])
# in the format of(#, depth, x_dim, y_dim)
img_r = img_r.reshape(1,1,8,8)
#print haha
img_g = np.array([ [1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],])
# in the format of(#, depth, x_dim, y_dim)
img_g = img_g.reshape(1,1,8,8)
img_b = np.array([ [1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],])
img_b = img_b.reshape(1,1,8,8)
print img_r.shape
print img_b.shape
img_1 = np.dstack((img_r,img_g))
img_1 = img_1.reshape(1,2,8,8)
print img_1.shape
#array = np.empty((1,3,8,8))
#print array
img_b = img_b.reshape(1,1,8,8)
img_1 = np.concatenate((img_b,img_1), axis=1).reshape(1,3,8,8)
img_1 = img_1.reshape(1,3,8,8)
print img_1.shape
# in the format of(#, depth, x_dim, y_dim)
# now the depth equals to 2

img2_r = np.array([ [1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],])
# in the format of(#, depth, x_dim, y_dim)
img2_r = img2_r.reshape(1,1,8,8)
#print haha
img2_g = np.array([ [1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],])
# in the format of(#, depth, x_dim, y_dim)
img2_g = img2_g.reshape(1,1,8,8)
img2_b = np.array([ [1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],
				[1, 1, 1, 1, 1, 1, 1, 1,],])
img2_b = img2_b.reshape(1,1,8,8)
img_2 = np.dstack((img2_r,img2_g))
img_2 = img_2.reshape(1,2,8,8)

img_2 = np.concatenate((img_b,img_2), axis=1).reshape(1,3,8,8)

#print gg
'''
wpaeog = np.stack((haha,hehe),axis=1)
wpaeog = wpaeog.reshape(2,8,8)'''

# vertically stack them together can increase the row.

print img_1.shape
print img_2.shape
print img_1
print img_2
#t