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

# Criando os neurônios
input_data = np.array([0.9, 0.65, 0.999])  # Entradas

neuron1 = Neuron(input_size=len(input_data), activation_function='sigmoid')
neuron2 = Neuron(input_size=1, activation_function='relu')
neuron3 = Neuron(input_size=1, activation_function='tanh')

# Loop de pensamento
output1 = neuron1.activate(input_data)
output2 = neuron2.activate(output1)
output3 = neuron3.activate(output2)

# Resultado
print("Output 1 (Sigmoid):", output1)
print("Output 2 (ReLU):", output2)
print("Output 3 (Tanh):", output3)

# Verificação de classificação simples
threshold = 0.5
classification_result = "baixo" if output3 <= threshold else "alto"
print("Classificação:", classification_result)
