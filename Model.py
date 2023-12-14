
import numpy as np
import pickle
from tqdm import tqdm
from Layers import Layer

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
    def __init__(self, network, loss, x_test, y_test):
        self.network = Network(network)
        self.loss = loss
        self.x_test = x_test
        self.y_test = y_test
        self.test_count = self.x_test.shape[0]
        self.train_loss = []
        self.test_loss = []
        self.train_acc = []
        self.test_acc = []
    
    def train(self, x_train, y_train, epochs, batch_size=64, learning_rate=0.001, early_stop=0, verbose=True, progress_bar=False):
        for epoch in range(epochs):
            perm = np.random.permutation(len(x_train))
            x_train = x_train[perm]
            y_train = y_train[perm]
            mean_loss = 0
            for i in tqdm(range(0, len(x_train), batch_size), disable=not progress_bar):
                x_batch = x_train[i:i+batch_size]
                y_batch = y_train[i:i+batch_size]
                output = self.network.forward(x_batch)
                loss = self.loss.loss(y_batch, output)
                mean_loss += loss
                loss_gradient = self.loss.gradient(y_batch, output)
                self.network.backward(loss_gradient, learning_rate)
                if early_stop > 0 and len(self.test_acc) > early_stop and self.test_acc[-1] <= self.test_acc[-early_stop]:
                    return
            mean_loss /= len(x_train) / batch_size
            self.train_loss.append(mean_loss)
            train_accu = self.test_accuracy(x_train[:self.test_count], y_train[:self.test_count])
            self.train_acc.append(train_accu)
            self.evaluate(self.x_test, self.y_test)
            
            if verbose:
                print(f"Epoch {epoch + 1} - Train loss: {round(self.train_loss[-1], 4)} - Test loss: {round(self.test_loss[-1], 4)} - Train acc: {round(self.train_acc[-1], 4)} - Test acc: {round(self.test_acc[-1], 4)}")
    
    def evaluate(self, x_test, y_test):
        total_loss = 0
        correct_predictions = 0
        for x, y in zip(x_test, y_test):
            output = self.network.forward(x)
            total_loss += self.loss.loss(y, output)
            if np.argmax(output) == np.argmax(y):
                correct_predictions += 1
        avg_loss = total_loss / len(x_test)
        accuracy = correct_predictions / len(x_test)
        self.test_loss.append(avg_loss)
        self.test_acc.append(accuracy)

    def predict_one(self, x):
        return self.network.forward(x)

    def predict(self, x_test):
        y_pred = []
        for x in x_test:
            y_pred.append(self.predict_one(x))
        return np.array(y_pred)

    def test_accuracy(self, x_test, y_test):
        correct_predictions = 0
        for x, y in zip(x_test, y_test):
            output = self.network.forward(x)
            if np.argmax(output) == np.argmax(y):
                correct_predictions += 1
        accuracy = correct_predictions / len(x_test)
        return accuracy        

    def save(self, path):
        with open(path, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(path):
        with open(path, "rb") as f:
            return pickle.load(f)
