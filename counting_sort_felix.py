arr = [44, 44, 55, 12, 42, 94, 18, 6, 67]
zahlen = list(range(max(arr)+1))

count_aufsteigend = []

max = max(arr)
count_zählen=[0]*(max+1)

for i in range(len(arr)):
    index = arr[i]
    count_zählen[index] = count_zählen[index]+1

print(count_zählen)
print(zahlen)

for i, anzahl in enumerate(count_zählen):
    count_aufsteigend.extend([i] * anzahl)

print(count_aufsteigend)
count_absteigend = count_aufsteigend
count_absteigend.reverse()



print(count_absteigend)