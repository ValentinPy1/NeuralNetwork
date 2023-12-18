
import numpy as np

class Loss:
    def loss(self, y_true, y_pred):
        raise NotImplementedError()

    def gradient(self, y_true, y_pred):
        raise NotImplementedError()

class MeanSquaredError(Loss):
    def loss(self, y_true, y_pred):
        return np.mean(np.power(y_true - y_pred, 2))

    def gradient(self, y_true, y_pred):
        return 2 * (y_pred - y_true) / y_true.size

class BinaryCrossEntropy(Loss):
    def loss(self, y_true, y_pred):
        epsilon = 1e-15
        return -np.mean(np.multiply(y_true, np.log(y_pred + epsilon)) + np.multiply(1 - y_true, np.log(1 - y_pred + epsilon)))

    def gradient(self, y_true, y_pred):
        epsilon = 1e-15
        return np.divide(y_pred - y_true, np.multiply(y_pred + epsilon, 1 - y_pred + epsilon))
