import heapq

def find_minimum_spanning_tree(pipes):
    edges = []
    for node1, connections in pipes.items():
        for node2, cost in connections.items():
            edges.append((cost, node1, node2))
    heapq.heapify(edges)
    visited = set()
    result = []
    while edges:
        cost, node1, node2 = heapq.heappop(edges)
        if node1 in visited and node2 in visited:
            continue
        visited.add(node1)
        visited.add(node2)
        result.append((node1, node2, cost))
    return result

pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}

if __name__ == '__main__':
    minimum_spanning_tree = find_minimum_spanning_tree(pipes)
    total_cost = sum(cost for _, _, cost in minimum_spanning_tree)
    print(minimum_spanning_tree)
    print(total_cost)
