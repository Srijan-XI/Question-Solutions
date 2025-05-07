import numpy as np

elements = input().split()  # Use input() for Python 3
int_elements = list(map(int, elements))

n_A = []
for i in range(int_elements[0]):
    N_ = input().split()  # Use input() for Python 3
    n = list(map(int, N_))
    n_A.append(n)

m_B = []
for i in range(int_elements[0]):
    M_ = input().split()  # Use input() for Python 3
    m = list(map(int, M_))
    m_B.append(m)

a = np.array(n_A)
b = np.array(m_B)

print(np.add(a, b))        # Add parentheses for Python 3
print(np.subtract(a, b))   # Add parentheses for Python 3
print(np.multiply(a, b))   # Add parentheses for Python 3
print(np.divide(a, b))     # Add parentheses for Python 3
print(np.mod(a, b))        # Add parentheses for Python 3
print(np.power(a, b))      # Add parentheses for Python 3
