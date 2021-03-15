import tensorflow as tf
import sklearn
import numpy
import matplotlib.pyplot as plt
import IPython.display import clear_output
from six.moves import urllib

# Tensor Types
# Constant - wont change
# Variable - can change
# ---------------------------------------------

# Useful functions Remember
# .rank
# .shape Shows shape
# .reshape(,,)
# .version
# ---------------------------------------------

# Tensor Examples
stringTensor = tf.Variable("My name is Dre", tf.string)
numberTensor = tf.Variable(22, tf.int16)
floatTensor = tf.Variable(1999.2211, tf.float64)

# Tensor of Rank (N)
rank1_tensor = tf.Variable(["test", "okay", "Dre"], tf.string)
rank2_tensor = (tf.Variable(["test", "okay", "Dre"], ["name", "thing", "othe    r"]), tf.string)


print(stringTensor)
