# -*- coding: utf-8 -*-
from rbm import RBM
from au import AutoEncoder
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

import PreprocessGenerative as i


inputData = i.importData()

# Train 2-Layer Deep Belief Network
print('DBN')

rbm1 = RBM(inputData[0].shape[0], 900, ['rbmw1', 'rbvb1', 'rbmhb1'], 0.3)
rbm2 = RBM(900, 500, ['rbmw2', 'rbvb2', 'rbmhb2'], 0.3)
epoch = 1

# Train First RBM
print('first rbm')

for g in range(epoch):
    for it in range(len(inputData)):
        trX = inputData[it][np.newaxis]
        rbm1.partial_fit(trX)
        print(rbm1.compute_cost(trX))
    print(rbm1.compute_cost(trX))
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
rbm2.save_weights('./rbmw2.chp')

print("Training Complete")
















