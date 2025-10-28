import numpy as np

# Zufälliges Array erzeugen
random_array = np.random.randint(0, 100, size=10)
print("Original:", random_array)

# In-place Quicksort mit Hilfsfunktion
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Sortieren
quick_sort(random_array, 0, len(random_array) - 1)
print("Ergebnis:", random_array)