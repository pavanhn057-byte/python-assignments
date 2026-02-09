# Comparing List and Generator

import sys

# Creating a List
list_numbers = [i for i in range(1, 1000001)]

# Creating a Generator
generator_numbers = (i for i in range(1, 1000001))

# Printing first 5 elements
print("First 5 elements from List:")
print(list_numbers[:5])

print("\nFirst 5 elements from Generator:")
for i in range(5):
    print(next(generator_numbers))

# Memory usage comparison
print("\nMemory used by List:", sys.getsizeof(list_numbers))
print("Memory used by Generator:", sys.getsizeof(generator_numbers))

