
staedte = [
    [0, 101, 111, 114, 113, 140, 154],
    [101, 0, 125, 33, 64, 24, 76],
    [111, 125, 0, 150, 179, 139, 143],
    [114, 33, 150, 0, 33, 68, 106],
    [113, 64, 179, 33, 0, 85, 135],
    [140, 24, 139, 68, 85, 0, 83],
    [154, 76, 143, 106, 135, 83, 0]
]



kuerzester_weg = 1000000

for i in range(1):
    tmp = 0
    for j in range(7):
       tmp = tmp + staedte[i][j]
    
    if(tmp < kuerzester_weg):
        kuerzester_weg = tmp

print(kuerzester_weg)