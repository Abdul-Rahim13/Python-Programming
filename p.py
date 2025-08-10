# 1. Create list a (odd numbers) and b (even numbers)
a = [1, 3, 5]       # first three odd positive integers
b = [2, 4, 6]       # first three even positive integers

# 2. Create list c by combining a and b
c = a + b

# 3. Create sorted copy d of c (leave c unchanged)
d = sorted(c)

# 4. Reverse d in-place
d.reverse()

# 5. Set fourth element of c to 42
c[3] = 42

# 6. Append 10 to d
d.append(10)

# 7. Append 7, 8, and 9 to c
c.extend([7, 8, 9])

# 8. Print first three elements of c
print("First three elements of c:", c[:3])

# 9. Print last element of d without using length
print("Last element of d:", d[-1])

# 10. Print length of d
print("Length of d:", len(d))
