arr = [44, 55, 12, 42, 94, 18, 6, 67]
sort_arr = []

Start_Element = arr[len]//2
n = Start_Element

def kindtauschen(n):
    if arr[n*2] > arr[n] or arr[n*2+1] > arr[n]:
        if arr[n*2] > arr[n*2+1]:
            x = arr[n*2]
            y = arr[n]
            arr[n] = x
            arr[n*2] = y
        elif arr[n*2+1] > arr[n*2]:
            x = arr[n*2+1]
            y = arr[n]
            arr[n] = x
            arr[n*2+1] = y

def heapsort():
    
