import numpy as np
from Abstracts import Loss

class MeanSquaredError(Loss):
    def loss(self, y_true, y_pred):
        return np.mean(np.square(y_true - y_pred))

    def gradient(self, y_true, y_pred):
        return 2 * (y_pred - y_true) / len(y_true)

class BinaryCrossEntropy(Loss):
    def loss(self, y_true, y_pred):
        return -np.mean(np.multiply(y_true, np.log(y_pred)) + np.multiply(1 - y_true, np.log(1 - y_pred)))

    def gradient(self, y_true, y_pred):
        return np.divide(y_pred - y_true, np.multiply(y_pred, 1 - y_pred))
