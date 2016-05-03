from rbm import RBM
from au import AutoEncoder
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

import PreprocessGenerative as i

inputData = i.importData()

epoch = 1


autoencoder = AutoEncoder(inputData[0].shape[0], [900], [['rbmw1', 'rbmhb1']], tied_weights=False)

autoencoder.load_rbm_weights('./rbmw1.chp', ['rbmw1', 'rbmhb1'], 0)


# Train Autoencoder
print('autoencoder')
for i in range(epoch):
    cost = 0.0
    for it in range(len(inputData)):
        trX = inputData[it][np.newaxis]
        cost += autoencoder.partial_fit(trX)
        print(cost)

autoencoder.save_weights('./au.chp')


print("Training Complete")