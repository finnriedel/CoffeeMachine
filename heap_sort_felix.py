arr = [44, 55, 12, 42, 94, 18, 6, 67]
sort_arr = []

# Start-Element ist die Mitte des Arrays
Start_Element = len(arr) // 2
n = Start_Element

def kindtauschen(n):
    # Prüfen, ob Kinder existieren
    if n * 2 < len(arr):
        left = n * 2
        right = n * 2 + 1 if n * 2 + 1 < len(arr) else None

        print("n: ", n)
        print("Array: ", arr)
        # Wenn linkes oder rechtes Kind größer als Eltern
        if (arr[left] > arr[n]) or (right and arr[right] > arr[n]):
            if right and arr[left] > arr[right]:
                arr[n], arr[left] = arr[left], arr[n]
                kindtauschen(left)  # Rekursiv weiter
            elif right:
                arr[n], arr[right] = arr[right], arr[n]
                kindtauschen(right) #Rekursiv weiter
            else:
                arr[n], arr[left] = arr[left], arr[n]

def heapsort():
    global arr, sort_arr
    # Heap aufbauen (1. Heap)
    for i in range(len(arr) // 2, -1, -1):
        kindtauschen(i)

    # Sortieren (Weitere Heaps)
    while arr:
        arr[0], arr[-1] = arr[-1], arr[0]
        print("Zwischenschritt:", "Array: ", arr)
        sort_arr.append(arr.pop())  # Größtes Element ans Ende
        print("Zwischenschritt:", "Sortiertes Array: ", sort_arr)
        for i in range(len(arr) // 2, -1, -1):
            kindtauschen(i)

heapsort()
print("Sortiertes finales Array: ", sort_arr)