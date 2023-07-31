**Neuron Class with Different Activation Functions**

**Description:**
This Python script demonstrates a simple implementation of a neural network neuron class with three different activation functions: sigmoid, ReLU (Rectified Linear Unit), and tanh (hyperbolic tangent). The purpose of this code is to show how a neuron can be initialized with random weights and bias, and how it performs the activation process based on the chosen activation function. It also includes a simple classification example using the neuron outputs.

**Neuron Class:**
- The `Neuron` class represents a single neuron in a neural network. It is initialized with the size of the input data and the desired activation function, which can be 'sigmoid', 'relu', or 'tanh'.
- The `_choose_activation_function` method is used to select the appropriate activation function based on the given activation function name.
- The `_sigmoid`, `_relu`, and `_tanh` methods implement the sigmoid, ReLU, and tanh activation functions, respectively.
- The `activate` method takes the input data, performs a weighted sum with the neuron's weights and bias, and then applies the chosen activation function to generate the output.

**Usage:**
- To create a `Neuron` object, simply instantiate it with the desired input size and activation function. For example:
  ```
  neuron1 = Neuron(input_size=len(input_data), activation_function='sigmoid')
  neuron2 = Neuron(input_size=1, activation_function='relu')
  neuron3 = Neuron(input_size=1, activation_function='tanh')
  ```
- After creating the neurons, you can use the `activate` method to get the output for given inputs:
  ```
  output1 = neuron1.activate(input_data)
  output2 = neuron2.activate(output1)
  output3 = neuron3.activate(output2)
  ```
- The script then prints the outputs of each neuron for the given input data.

**Classification Example:**
The script also demonstrates a simple classification example using the output of the `tanh` neuron. It classifies the output into either "baixo" (low) or "alto" (high) based on a threshold value (0.5) that you can adjust. The classification result is printed to the console.

**Dependencies:**
This code requires the `numpy` library, which is a powerful library for numerical computing in Python.

**Note:**
This code is a simple demonstration of neuron functionality and does not constitute a full neural network implementation. It serves as a starting point for understanding the fundamental concepts of neural networks and can be extended for more complex use cases.

**Author:**
Rafael Parish

**Date:**
31/07/2023 - Initial Commit

**References:**
CS50's Introduction to Programming with Python
Machine Learning with Python: from Linear Models to Deep Learning
