import numpy as np

random_array = np.random.randint(0, 100, size=10)

print(random_array)

def quick_sort(arr):
    pivot = arr[0]
    i = 0
    j = len(arr) - 1
    while i >= j:
        while arr[i] >= pivot:
            i+1
        while arr[j] <= pivot:
            j-1
        tmp = i
        arr[i] = arr [j]
        arr[j] = tmp
    
    tmp = arr[i]
    arr[i] = pivot
    arr[0] = tmp

    kleiner = []
    groesser = []

    for y in range(i-1):
        kleiner.append(arr[y])
        
    for x in range(j, len(arr-1)):
        groesser.append(arr[x])
    
    return quick_sort(kleiner)+pivot+quick_sort(groesser)


quick_sort(random_array)
print("Ergebnis:", random_array)