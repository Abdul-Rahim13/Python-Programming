def cube(x):
    return x * x * x

def fac(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fac(x - 1)

def count_pattern(pattern, lst):
    count = 0
    pat_len = len(pattern)
    for i in range(len(lst) - pat_len + 1):
        if tuple(lst[i:i+pat_len]) == tuple(pattern):
            count += 1
    return count

def mul(x):
    for i in range(1, 11):
        print(f"{x} X {i} = {x * i}")

def calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operator!"

def sort_sentence(sentence):
    return ' '.join(sorted(sentence.split()))

def menu():
    while True:
        print("\nMenu:")
        print("1. Cube of a number")
        print("2. Factorial of a number")
        print("3. Count Pattern")
        print("4. Multiplication Table")
        print("5. Calculator")
        print("6. Sort the sentence in alphabetical order")
        print("7. Exit")

        choice = input("Enter Choice: ")

        if choice == '1':
            n = int(input("Enter number: "))
            print("Cube:", cube(n))
        elif choice == '2':
            n = int(input("Enter number: "))
            print("Factorial:", fac(n))
        elif choice == '3':
            pattern = tuple(input("Enter pattern (space separated): ").split())
            lst = tuple(input("Enter list elements (space separated): ").split())
            count = count_pattern(pattern, lst)
            print("Pattern count:", count)
        elif choice == '4':
            n = int(input("Enter number: "))
            mul(n)
        elif choice == '5':
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            result = calculator(num1, operator, num2)
            print("Result:", result)
        elif choice == '6':
            sentence = input("Enter a sentence: ")
            sorted_sentence = sort_sentence(sentence)
            print("Sorted sentence:", sorted_sentence)
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")

menu()
