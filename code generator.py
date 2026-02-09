# Basic Generator Function

def simple_generator():
    print("Start")
    yield 1
    print("Middle")
    yield 2
    print("End")
    yield 3


# Using the generator
gen = simple_generator()

print(next(gen))  # First value
print(next(gen))  # Second value
print(next(gen))  # Third value

output

Start
1
Middle
2
End
3

