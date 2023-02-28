import random
import time

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]

        j = i - 1

        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array

def quicksort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = array[random.randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quicksort(low) + same + quicksort(high)

n = []

for i in range(10000):
    n.append(random.randint(0, 10000))

start_time = time.time()
print("Insertion sort time started")

sortedWithInsertion = insertion_sort(n)

print("--- Insertion sort %s seconds ---" % (time.time() - start_time))

start_time2 = time.time()
print("Quick sort time started")

sortedWithQuickSort = quicksort(n)

print("--- Quick sort %s seconds ---" % (time.time() - start_time2))