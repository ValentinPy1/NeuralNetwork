import numpy as np
from Abstracts import Layer
from Abstracts import Loss
from Abstracts import Activation

class Network(Layer):
    def __init__(self, layers):
        self.layers = layers
    
    def forward(self, input):
        output = input
        for layer in self.layers:
            output = layer.forward(output)
        return output
    
    def backward(self, output_error, learning_rate):
        for layer in reversed(self.layers):
            output_error = layer.backward(output_error, learning_rate)
        return output_error

class Model:
    def __init__(self, network, loss):
        self.network = Network(network)
        self.loss = loss
    
    def train(self, x_train, y_train, epochs, learning_rate):
        for epoch in range(epochs):
            for x, y in zip(x_train, y_train):
                output = self.network.forward(x)
                loss = self.loss.loss(y, output)
                loss_gradient = self.loss.gradient(y, output)
                self.network.backward(loss_gradient, learning_rate)
            print('epoch %d/%d   loss=%f' % (epoch+1, epochs, loss))
    
    def predict(self, x_test):
        if len(x_test.shape) == 1:
            return self.network.forward(x_test.reshape(-1, 1))
        y_pred = []
        for x in x_test:
            y_pred.append(self.network.forward(x.reshape(-1, 1)))
        return np.array(y_pred).squeeze()
