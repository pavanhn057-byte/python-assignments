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

List: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

Generator gives these values:
0 1 4 9 16 25 36 49 64 81 

Empty generator now:
Difference between lists and generators:-

List stores all elements in memory at once, generator generates values one by one which results into low memory usage
List computes everything immediately, generator computes values only when requested
List can be iterated multiple times, generators can be interated only once unless it is recreated
List is useful for small datasets & random access, and generators are used when working with large datasets and where memory is limited
Thus if data has to be iterated only once then use generator, if data is needed multiple times or want to find length using len() then use list

