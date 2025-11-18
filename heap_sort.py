arr = [44,55,12,42,94,18,6,67]

def heapify(arr, n, i):
    wurzel = i
    linkes_kind = i*2+1 # + 1 wegen Array
    rechtes_kind = i*2+2 # + 2 wegen Array

    if linkes_kind < n and arr[i] < arr[linkes_kind]: # WENN LINKES KIND EXISTIERT UND GRÖßER IST ALS i
        wurzel = linkes_kind

    if rechtes_kind < n and arr[wurzel] < arr[rechtes_kind]: # WENN RECHTES KIND EXISTIERT UND GRÖßER IST ALS DIE NEUE WURZEL (evtl. links!)
        wurzel = rechtes_kind

    if wurzel != i: # WENN DIE WURZEL VERÄNDERT WURDE, DANN TAUSCHEN
        tmp = arr[i]
        arr[i] = arr[wurzel]
        arr[wurzel] = tmp

        heapify(arr, n, wurzel) # STARTE HEAPIFY FÜR EVTL. NUN UNSORTIERTE KINDER

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1): # START AB ARRAY-PLATZ MIT DER HÄLFTE VON n, BIS -1 (inkl. 0)
        print("i =",i)
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1): # FÜR DIE GESAMTE ARRAY LÄNGE, TAUSCHE LETZTES MIT ERSTEM ELEMENT
        tmp = arr[i]
        arr[i] = arr[0]
        arr[0] = tmp

        heapify(arr, i, 0) # RUFE HEAPIFY AUF


heap_sort(arr)
print(arr)
