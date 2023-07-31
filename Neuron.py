import numpy as np

class Neuron:
    def __init__(self, input_size, activation_function='sigmoid'):
        self.weights = np.random.randn(input_size)  # Inicialização aleatória dos pesos
        self.bias = np.random.randn()  # Inicialização aleatória do bias
        self.activation_function = self._choose_activation_function(activation_function)

    def _choose_activation_function(self, activation_function):
        if activation_function == 'sigmoid':
            return self._sigmoid
        elif activation_function == 'relu':
            return self._relu
        elif activation_function == 'tanh':
            return self._tanh
        else:
            raise ValueError("Invalid activation function. Choose from 'sigmoid', 'relu', or 'tanh'.")

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def _relu(self, x):
        return np.maximum(0, x)

    def _tanh(self, x):
        return np.tanh(x)

    def activate(self, inputs):
        weighted_sum = np.dot(inputs, self.weights) + self.bias
        output = self.activation_function(weighted_sum)
        return output

# Exemplo de uso do neurônio
input_data = np.array([0.9, 0.65, 0.999])  # Entradas

neuron = Neuron(input_size=len(input_data), activation_function='sigmoid')  # Criação do neurônio com função sigmoid

output = neuron.activate(input_data)  # Ativação do neurônio

print(output)
