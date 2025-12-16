nodes = {
    "A":{
        "B": 7,
        "E": 8
    },
    "B":{
        "A": 7,
        "C": 4,
        "D": 12,
        "E": 2
    },
    "C":{
        "B": 4,
        "E": 6,
        "D": 4
    },
    "D":{
        "C": 4,
        "B": 12
    },
    "E":{
        "A": 8,
        "B": 2,
        "C": 6
    }
}

unvisited_nodes = ["A", "B", "C", "D", "E"] 

def dijkstra(nodes, source_node):

    dist = {node: float("inf") for node in nodes}
    dist[source_node] = 0

    while unvisited_nodes:
        current = None
        
        for node in unvisited_nodes:
            if node in dist:
                if current is None or dist[node] < dist[current]:
                    current = node
        
        if current is None or dist[current] == float("inf"):
            break

        unvisited_nodes.remove(current)

        for neighbor, weight in nodes[current].items():
            new_dist = dist[current] + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist

    return dist

print(dijkstra(nodes, "A"))