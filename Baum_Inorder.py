arr = [35, 17, 88, 93, 91, 12, 8, 47, 58, 32, 1, 69, 62, 74, 99, 23, 18, 11]

def baum (arr):
    wurzel = arr[0]
    
    i = 0
    if arr[i+1] < wurzel:
        