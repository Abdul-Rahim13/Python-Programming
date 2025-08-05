x = 250
print(type(x))

x = 28 % 5
print(type(x))

x = 2.5e2
print(type(x))

x = 3e5
print(type(x))

x = 3 * 10**5
print(type(x))

x = 20 + 35 * 2
print(type(x))
print(x)

y = (20 + 35) * 2
print(type(y))
print(y)
#  The difference is due to the order of operations in 20 + 35 * 2 -> multiplication is done first
#  while in (20 + 35) \ 2 -> addition inside parentheses is done first.

x = 2 / 3 * 3
print(type(x))

x = 2 // 3 * 3
print(type(x))
print(x)

y = 2 / 3 * 3
print(type(y))
print(y)

# /-/ is floor division which returns an integer by discarding the decimal part 
#  while / is true division, which keeps the decimal

x = 25 - 5 * 2 - 9
print(type(x))
print(x)

y = ((25 - 5) * 2) - 9
print(type(y))
print(y)

z = 25 - ((5 * 2) - 9)
print(type(z))
print(z)

#  they are different because parentheses change which parts are done first 
#  while without them, math rules say to do multiplication before subtraction
#  then go left to right. So each version gives a different result


flavours= ["vanilla","choclate", "strawberry", "pistacchio"]
sauces= ["caramel", "butterscotch","choclate"]
count= 0
for i in range(len(flavours)):
    for j in range(len(sauces)):
        count+=1
        print(f"{count}. {flavours[i]} ice cream with {sauces[j]} sauce")

print(f"Total no of combinations: ",count)


def triangle():
     value = 1
     row = 1
     while row <=10:
         column = 1
         while column <=row:
             if column !=row:
                 print(value, ' ', sep = '', end = '')
             else:
                 print(value)
             value = value + 1
             column = column + 1
         row = row + 1
         
triangle()

string = input("enter string:")
freq = {}
for x in string:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

print(freq)
                
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

class Find_pair:
    def __init__(self, lst, target):
        self.lst = lst
        self.target = target
    
    def find_pair(self):
        for i in range(len(self.lst)):
            for j in range(i+1, len(self.lst)):
                if self.lst[i] + self.lst[j] == self.target:
                    print(f"Pair found at indices: {i}, {j}")

list = [1,2,3,4,5,6,7,8,9,10]
tar = 6
FP = Find_pair(list, tar)
FP.find_pair()

class Reverse_String:
    def __init__(self, str):
        self.str = str

    def reverse_str(self):
        for i in range(len(self.str)-1, -1, -1):
            print({self.str[i]}, end = " ")

string = "hello.py"
RS = Reverse_String(string)
RS.reverse_str()

matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

n = len(matrix1)
result = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

for items in result:
    print(items)

matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

n = len(matrix1)
result = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(matrix1[i][j] * matrix2[i][j])
    result.append(row)

for items in result:
    print(items)

class Number:
    Multiplier = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    
    def mul(self):
        return self.x * self.__class__.Multiplier
    
    def sub(self):
        return self.x - self.y
    
    def value(self):
        return(self.x, self.y)
    
    def value(self, val):
        self.x, self.y = val

    def value(self):
        self.x = None
        self.y = None

num = Number(4,5)

print(f"Add: {num.add()}")
print(f"Multiply: {num.mul()}")
print(f"sub: {num.sub()}")

num.value = (1,2)
print(f"updated value: {num.value}")

del num.value
print(f"Deleted: {num.value}")
