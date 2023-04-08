import pickle
import numpy as np
import matplotlib.pyplot as plt





file = open('imagenet_valset.pkl', 'rb')

# dump information to that file
ds_p = pickle.load(file)



plt.figure()
plt.imshow(ds_p[4])







# close the file
file.close()