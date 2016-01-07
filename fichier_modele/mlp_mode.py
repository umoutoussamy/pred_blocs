#!/usr/bin/python


import os
import sys
import numpy as np

import lasagne
from lasagne.layers import DenseLayer
from lasagne.layers import InputLayer
from lasagne.nonlinearities import softmax
from lasagne import layers
from nolearn.lasagne import NeuralNet
from lasagne.updates import nesterov_momentum


def load(csvfile, w=False):
    """
    Loads data from a csv file with "," delimiter and format :
        - 1st column : X - real data
        - 2nd-to-n column : Y attributes

    Input:
        csvfile : 'str' of the path to the csv file
        w       : 'boolean' uniform weight (WARNING! loss of data)
    """

    dat = np.genfromtxt(csvfile, delimiter=" ")
    
    if w==True:
        # separate datas in each class and get the minimum number from a class
        d = []
        mi = -1 # init
        for i in xrange(16):
            sh = dat[np.where(dat[:,0]==i)]
            
            if mi < 0 or mi > sh.shape[0]:
                mi = sh.shape[0]

            d.append(dat[np.where(dat[:,0]==i)])
        
        
        # Concatenate datas with the minimum amount
        dat = d[0][np.random.choice(d[0].shape[0], mi, replace=False)]
        for mat in d[1:]:
            dat = np.concatenate((dat, mat[np.random.choice(mat.shape[0], mi, replace=False)]), axis=0)
        # shuffle datas
        np.random.shuffle(dat)
        
    ytmp = dat[:, 0] # target matrix
    Xtmp = dat[:,1:]

    Xtmp = Xtmp.astype(np.float32)
    ytmp = ytmp.astype(np.int32)    

    X = Xtmp[:(3.0/4*ytmp.size),:]
    y = ytmp[:(3.0/4*ytmp.size)]
   
    X_t = Xtmp[((3.0/4*ytmp.size)+1):,:]
    y_t = ytmp[((3.0/4*ytmp.size)+1):]

    

    return X,y, X_t, y_t


net1 = NeuralNet(
    layers=[  # three layers: one hidden layer
        ('input', layers.InputLayer),
        ('hidden1', layers.DenseLayer),
        ('output', layers.DenseLayer),
        ],
    # input layer
    input_shape=(None, 220),  # 11x20 input pssm profile per batch
    # hidden layers
    hidden1_num_units=50,
    hidden1_nonlinearity=lasagne.nonlinearities.softmax,
    # output layer
    output_nonlinearity=lasagne.nonlinearities.softmax,
    output_num_units=16,
    # optimization method:
    update=nesterov_momentum,
    update_learning_rate=0.01,
    update_momentum=0.9,
    regression=False,  # flag to indicate we're dealing with regression problem
    max_epochs=100,  # we want to train this many epochs
    verbose=1,
    )


net2 = NeuralNet(
    layers=[  # three layers: one hidden layer
        ('input', layers.InputLayer),
        ('hidden1', layers.DenseLayer),
        ('dropout1', layers.DropoutLayer),
        ('output', layers.DenseLayer),
        ],
    # input layer
    input_shape=(None, 220),  # 11x20 input pssm profile per batch
    # hidden layers
    hidden1_num_units=50,
    hidden1_nonlinearity=lasagne.nonlinearities.softmax,
    # Dropout layer
    dropout1_p = 0.5,
    # output layer
    output_nonlinearity=lasagne.nonlinearities.softmax,
    output_num_units=16,
    # optimization method:
    update=nesterov_momentum,
    update_learning_rate=0.01,
    update_momentum=0.9,
    regression=False,  # flag to indicate we're dealing with regression problem
    max_epochs=100,  # we want to train this many epochs
    verbose=1,
    )



if __name__ == "__main__":
    X,y,X_t,y_t = load(sys.argv[1], True)

    nn1 = net1.fit(X,y)
    pred1 = nn1.predict(X_t)

    nn2 = net2.fit(X,y)
    pred2 = nn2.predict(X_t)

    
    out1 = open("output1.dat", "w")
    out2 = open("output2.dat", "w")
    
    for d in pred1:
        out1.write(str(d)+"\n")
    
    for d in pred2:
        out2.write(str(d)+"\n")

    out1.close()
    out2.close()
