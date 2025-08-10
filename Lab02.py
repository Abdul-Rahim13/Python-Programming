from statistics import mean, median, mode

def calculate_stats(numbers):

    total_sum = sum(numbers)

    mean_val = mean(numbers)
    median_val = median(numbers)
    mode_val = mode(numbers)

    print("Numbers:", numbers)
    print("Sum:", total_sum)
    print("Mean:", mean_val)
    print("Median:", median_val)
    print("Mode:", mode_val)


numbers = [4, 1, 2, 2, 3, 5, 4, 2]
calculate_stats(numbers)

def dups(lst):
    duplicates = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j] and lst[i] not in duplicates:
                duplicates.append(lst[i])
    return duplicates

numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7]

result = dups(numbers)

print("Original List:", numbers)
print("Duplicate Elements:", result)


a = [1, 3, 5]
b = [2, 4, 6]

c = a + b

d = sorted(c)
d.reverse()

c[3] = 42

d.append(10)
c.extend([7, 8, 9])

print("First three elements of c:", c[:3])
print("Last element of d:", d[-1])
print("Length of d:", len(d))
