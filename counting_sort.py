arr = [44,55,12,42,94,18,6,67,6]
count_arr = [0]*(max(arr)+1)

for i in range(len(arr)):
    index = arr[i]
    count_arr[index] = count_arr[index]+1

print("Counting-Array:",count_arr)

print("\nFertiges Array (Aufsteigend):")
for i in range(len(count_arr)):
    if(count_arr[i] > 0):
        print(i,end=", ")

print("\n\nFertiges Array (Absteigend):")
for i in range(len(count_arr)-1, 0, -1):
    if(count_arr[i] > 0):
        print(i, end=", ")