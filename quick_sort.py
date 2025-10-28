import random

random_array = [random.randint(1, 100) for _ in range(10)]

print("\nHier ist das random Array:",random_array,"\n")

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    kleiner = []
    groesser = []

    print("\n","-"*20)
    print("\nDas Pivot-Element ist:",pivot,"und das Array ist:",arr,"\n")

    for element in arr[1:]:
        if element < pivot:
            print(element, "Wird dem kleineren Array hinzugefügt")
            kleiner.append(element)
        else:
            print(element, "Wird dem größeren Array hinzugefügt")
            groesser.append(element)
    
    
    print("\nHier ist das gesamte kleinere Array:",kleiner)
    print("Hier ist das gesamte größere Array:",groesser)
    return quick_sort(kleiner)+[pivot]+quick_sort(groesser)

print("\nHier ist das sortierte Array:", quick_sort(random_array),"\n")