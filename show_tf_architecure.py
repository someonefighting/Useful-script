#!/usr/bin/python
import tensorflow as tf
import numpy as np
#import matplotlib.pyplot as plt
Reader = tf.train.NewCheckpointReader('/liry_tf/tf-kaldi-speaker/egs/voxceleb/v1/exp_kftdnn_am/xvector_nnet_tdnn_amsoftmax_m0.20_linear_bn_1e-2/nnet/model-682500')
all_variables = Reader.get_variable_to_shape_map()
for i in all_variables:
    print(i, all_variables[i])
