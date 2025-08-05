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