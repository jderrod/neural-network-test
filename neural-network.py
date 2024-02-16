# neural_network.py
import torch
import torch.nn as nn
import torch.nn.functional as F

class DotController(nn.Module):
    def __init__(self):
        super(DotController, self).__init__()
        # Define the architecture of the neural network
        # Input layer: 2 inputs for the relative X and Y positions of the food to the dot
        # Hidden layer: 16 neurons, chosen arbitrarily
        # Output layer: 4 neurons, corresponding to movement directions (up, down, left, right)
        self.fc1 = nn.Linear(2, 16)  # Input layer to hidden layer
        self.fc2 = nn.Linear(16, 4)  # Hidden layer to output layer

    def forward(self, x):
        """
        Forward pass through the network
        :param x: The input tensor containing the state (relative position of food to dot)
        :return: Output tensor with action preferences
        """
        x = F.relu(self.fc1(x))  # Activation function for hidden layer
        x = self.fc2(x)  # Output layer
        return x

def get_model():
    """
    Utility function to create a new instance of the neural network model
    :return: An instance of DotController
    """
    model = DotController()
    return model