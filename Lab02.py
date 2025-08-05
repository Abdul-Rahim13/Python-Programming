from statistics import mean, median, mode

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst

def merge_sort(lst):

    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1

        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

arr = [5, 3, 2, 1, 4]
print("Insertion Sort:", insertion_sort(arr))

arr = [5, 3, 2, 1, 4]
print("Selection Sort:", selection_sort(arr))

arr = [5, 3, 2, 1, 4]
sorted_arr = merge_sort(arr)
print("Sorted list:", sorted_arr)

result = bubble_sort(['P','Y','T','H','O','N'])
print(result)

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
