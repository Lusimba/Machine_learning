#Item     ## Inputs  ## Outputs #
##############################
#Example1 ## 0  0  1 ## 0 
#Example1 ## 1  1  1 ## 1 
#Example1 ## 1  0  1 ## 1 
#Example1 ## 0  1  1 ## 0 
#############################
#New Data ## 1  0  0 ## ? 

import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))
def sigmoid_derivative(x):
    return np.exp(-x)/(np.power(1+np.exp(-x),2))

training_inputs = np.array(
                    [[0,0,1],
                    [1,1,1],
                    [1,0,1],
                    [0,1,1]])
training_output = np.array([[0,1,1,0]]).T
np.random.seed(1)
synaptic_weights = 2*np.random.random((3,1))-1
print('Random starting synaptic weights: \n', synaptic_weights)
for iteration in range(20000):
    input_layer =training_inputs
    outputs = sigmoid(np.dot(input_layer,synaptic_weights))
    error = training_output-outputs
    adjustments = error*sigmoid_derivative(outputs)
    synaptic_weights+=np.dot(input_layer.T, adjustments)
print("Synaptic weights after training:\n ",synaptic_weights)

print('Outputs after training set: \n', outputs)
