import numpy as np

class Layer:
    def __init__(self):
        self.input = None
        self.output = None

    def forward(self, input):
        raise NotImplementedError

    def backward(self, output_gradient, learning_rate):
        raise NotImplementedError

class Dense(Layer):
    def __init__(self, input_size, output_size, beta1=0.9, beta2=0.999, epsilon=1e-8):
        self.weights = np.random.randn(output_size, input_size)
        self.bias = np.random.randn(output_size, 1)
        self.m_w, self.v_w = np.zeros_like(self.weights), np.zeros_like(self.weights)
        self.m_b, self.v_b = np.zeros_like(self.bias), np.zeros_like(self.bias)
        self.t = 0
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon

    def forward(self, input):
        self.input = input
        return np.dot(input, self.weights.T) + self.bias.T

    def backward(self, output_gradient, learning_rate):
        self.t += 1
        input_gradient = np.dot(output_gradient, self.weights)
        weights_gradient = np.dot(output_gradient.T, self.input)
        bias_gradient = np.sum(output_gradient, axis=0, keepdims=True).T

        self.m_w = self.beta1 * self.m_w + (1 - self.beta1) * weights_gradient
        self.v_w = self.beta2 * self.v_w + (1 - self.beta2) * weights_gradient**2
        m_w_hat = self.m_w / (1 - self.beta1**self.t)
        v_w_hat = self.v_w / (1 - self.beta2**self.t)
        self.weights -= learning_rate * m_w_hat / (np.sqrt(v_w_hat) + self.epsilon)

        self.m_b = self.beta1 * self.m_b + (1 - self.beta1) * bias_gradient
        self.v_b = self.beta2 * self.v_b + (1 - self.beta2) * bias_gradient**2
        m_b_hat = self.m_b / (1 - self.beta1**self.t)
        v_b_hat = self.v_b / (1 - self.beta2**self.t)
        self.bias -= learning_rate * m_b_hat / (np.sqrt(v_b_hat) + self.epsilon)

        return input_gradient

class Dropout(Layer):
    def __init__(self, drop_rate):
        self.drop_rate = drop_rate
        self.mask = None

    def forward(self, input):
        self.mask = np.random.rand(*input.shape) > self.drop_rate
        return input * self.mask

    def backward(self, output_gradient, learning_rate):
        return output_gradient * self.mask
