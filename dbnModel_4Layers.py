# -*- coding: utf-8 -*-
from rbm import RBM
from au import AutoEncoder
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

import PreprocessGenerative as i


inputData = i.importData()

# Train 4-Layer Deep Belief Network
print('DBN')

rbm1 = RBM(inputData[0].shape[0], 900, ['rbmw1', 'rbvb1', 'rbmhb1'], 0.3)
rbm2 = RBM(900, 500, ['rbmw2', 'rbvb2', 'rbmhb2'], 0.3)
rbm3 = RBM(500, 250, ['rbmw3', 'rbvb3', 'rbmhb3'], 0.3)
rbm4 = RBM(250, 2,   ['rbmw4', 'rbvb4', 'rbmhb4'], 0.3)

epoch = 1

# Train First RBM
print('first rbm')

for g in range(epoch):
    for it in range(len(inputData)):
        trX = inputData[it][np.newaxis]
        rbm1.partial_fit(trX)
        print(rbm1.compute_cost(trX))
    print(rbm1.compute_cost(trX))
    #show_image("1rbm.jpg", rbm1.n_w, (28, 28), (30, 30))
rbm1.save_weights('./rbmw1.chp')

# Train Second RBM2
print('second rbm')

for g in range(epoch):
    for it in range(len(inputData)):
        trX = inputData[it][np.newaxis]
        # Transform features with first rbm for second rbm
        trX = rbm1.transform(trX)
        rbm2.partial_fit(trX)
        print(rbm2.compute_cost(trX))
    print(rbm2.compute_cost(trX))
    #show_image("2rbm.jpg", rbmobject2.n_w, (30, 30), (25, 20))
rbm2.save_weights('./rbmw2.chp')

# Train Third RBM
print('third rbm')
for i in range(epoch):
    for it in range(len(inputData)):
        trX = inputData[it][np.newaxis]
        # Transform features
        trX = rbm1.transform(trX)
        trX = rbm2.transform(trX)
        rbm3.partial_fit(trX)
        print(rbm3.compute_cost(trX))
    print(rbm3.compute_cost(trX))
    #show_image("3rbm.jpg", rbmobject3.n_w, (25, 20), (25, 10))
rbm3.save_weights('./rbmw3.chp')

# Train Third RBM
print('fourth rbm')
for i in range(epoch):
    for it in range(len(inputData)):
        trX = inputData[it][np.newaxis]
        # Transform features
        trX = rbm1.transform(trX)
        trX = rbm2.transform(trX)
        trX = rbm3.transform(trX)
        rbm4.partial_fit(trX)
        print(rbm4.compute_cost(trX))
    print(rbm4.compute_cost(trX))
rbm4.save_weights('./rbmw4.chp')


print("Training Complete")



