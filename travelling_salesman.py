# Rekursive Funktion zur Erzeugung aller Permutationen
def generate_permutations(elements):
    if len(elements) == 0:
        return [[]]
    perms = []
    for i in range(len(elements)):
        rest = elements[:i] + elements[i+1:]
        for p in generate_permutations(rest):
            perms.append([elements[i]] + p)
    return perms


def shortest_tour(distance_matrix):
    n = len(distance_matrix)
    nodes = list(range(n))
    start = 0  # Startpunkt fixieren
    
    # Alle Permutationen der übrigen Punkte erzeugen
    permutations = generate_permutations(nodes[1:])
    
    best_distance = float('inf')
    best_path = None
    worst_distance = float('-inf')
    worst_path = None
    
    for perm in permutations:
        path = [start] + perm + [start]
        # Berechne die Gesamtdistanz
        distance = 0
        for i in range(len(path) - 1):
            distance += distance_matrix[path[i]][path[i+1]]
        
        if distance <= best_distance:
            best_distance = distance
            best_path = path

        if distance >= worst_distance:
            worst_distance = distance
            worst_path = path
    
    return best_path, best_distance, worst_path, worst_distance


# Deine Matrix
staedte = [
    [0, 101, 111, 114, 113, 140, 154],
    [101, 0, 125, 33, 64, 24, 76],
    [111, 125, 0, 150, 179, 139, 143],
    [114, 33, 150, 0, 33, 68, 106],
    [113, 64, 179, 33, 0, 85, 135],
    [140, 24, 139, 68, 85, 0, 83],
    [154, 76, 143, 106, 135, 83, 0]
]


#print(generate_permutations(staedte))
bpath, bdist, wpath, wdist = shortest_tour(staedte)
print("Kürzester Pfad:", bpath)
print("Minimale Distanz:", bdist, "km")
print("Längster Pfad:", wpath)
print("Maximale Distanz:", wdist, "km")