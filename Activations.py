import numpy as np
from Layers import Layer

class Activation(Layer):
    def __init__(self, activation, activation_prime):
        self.activation = activation
        self.activation_prime = activation_prime

    def forward(self, input):
        self.input = input
        return self.activation(input)

    def backward(self, output_gradient, learning_rate):
        return np.multiply(output_gradient, self.activation_prime(self.input))

class Tanh(Activation):
    @staticmethod
    def activation(x):
        return np.tanh(x)

    @staticmethod
    def activation_prime(x):
        return 1 - np.tanh(x) ** 2

    def __init__(self):
        super().__init__(Tanh.activation, Tanh.activation_prime)

class Sigmoid(Activation):

    @staticmethod
    def activation(x):
        x = np.clip(x, -100, 100)
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def activation_prime(x):
        sig = Sigmoid.activation(x)
        return sig * (1 - sig)

    def __init__(self):
        super().__init__(Sigmoid.activation, Sigmoid.activation_prime)

class ReLU(Activation):
    @staticmethod
    def activation(x):
        return np.maximum(0, x)

    @staticmethod
    def activation_prime(x):
        return np.where(x > 0, 1, 0)

    def __init__(self):
        super().__init__(ReLU.activation, ReLU.activation_prime)
