import numpy as np

# Take input from the user
elements = input().split()  # Use input() for Python 3

# Convert input to integers
int_elements = list(map(int, elements))

# Create an identity matrix with the given dimensions
result = np.eye(int_elements[0], int_elements[1])

# Print the result
print(result)
