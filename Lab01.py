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

def count_pattern(pattern, lst):
    count = 0
    for i in range(len(pattern)):
        for j in range(len(lst)):
            if pattern[i] == lst[j]:
                count+=1
    print(count)

count_pattern(['a','b'],['a','b', 'c', 'e', 'b', 'a', 'b', 'f'])
                
#choice = input("Enter Choice: ")
print("1. Cube of a number")
print("2. Factorialof a number")
print("3. Count Pattern")
print("4. Multiplication Table")
print("5. Calculator")
print("6.sort the sentence in alphabetical order")

def cube(x):
    return x*x*x

def fac(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x*fac(x-1)

cube(3)
fac(5)