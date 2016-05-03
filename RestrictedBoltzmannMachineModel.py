from rbm import RBM
from au import AutoEncoder
import tensorflow as tf
import input_data
from utilsnn import show_image, min_max_scale
import matplotlib.pyplot as plt
import numpy as np

import PreprocessGenerative as i


inputData = i.importData()


rbm1 = RBM(inputData[0].shape[0], 900, ['rbmw1', 'rbvb1', 'rbmhb1'], 0.3)


epoch = 1

# Train RBM
print('rbm')

for g in range(epoch):
    for it in range(len(inputData)):
        trX = inputData[it][np.newaxis]
        rbm1.partial_fit(trX)
        print(rbm1.compute_cost(trX))
    print(rbm1.compute_cost(trX))
rbm1.save_weights('./rbmw1.chp')


print("Training Complete")



