while True:
    A = float(input("Enter first number: "))
    B = float(input("Enter second number: "))

    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Result:", A + B)

    elif choice == "2":
        print("Result:", A - B)

    elif choice == "3":
        print("Result:", A * B)

    elif choice == "4":
        if num2 != 0:
            print("Result:", A / B)
        else:
            print("Divide by 0 is not possible")

    elif choice == "5":
        print("Calculator closed")
        break

    else:
        print("Invalid choice")

    print("-----------------------")
     
Enter first number: 5
Enter second number: 10

Select operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Enter choice: 1
Result: 15.0
-----------------------
Enter first number: 6
Enter second number: 12

Select operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Enter choice: 5
Calculator closed
