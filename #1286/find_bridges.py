def find_bridges(graph, num_vertices):
    # Initialize a list to store the bridges
    bridges = []

    # Initialize a counter to assign discovery times to the vertices
    disc_time = [0] * (num_vertices + 1)

    # Initialize an array to store the lowest discovery time reachable from a given vertex
    low = [0] * (num_vertices + 1)

    # Initialize a parent array to store the parent of each vertex in the DFS tree
    parent = [-1] * (num_vertices + 1)

    # Initialize a counter to keep track of the time during the DFS
    time = 0

    # Perform a DFS traversal of the graph
    for i in range(1, num_vertices + 1):
        if not disc_time[i]:
            # Start a new DFS tree rooted at vertex i
            time = dfs_util(graph, i, disc_time, low, parent, bridges, time)

    return bridges


def dfs_util(graph, u, disc_time, low, parent, bridges, time):
    # Return immediately if the vertex is not connected to the root of the DFS tree
    if not parent[u]:
        return time

    # Mark the discovery time of the current vertex
    disc_time[u] = low[u] = time + 1

    # Explore each adjacent vertex of the current vertex
    for v in graph[u]:
        # If the vertex has not been visited yet,
        # explore it and update the low time of the current vertex
        if not disc_time[v]:
            parent[v] = u
            time = dfs_util(graph, v, disc_time, low, parent, bridges, time)

            # Update the low time of the current vertex
            low[u] = min(low[u], low[v])

            # If the low time of the adjacent vertex is greater than the discovery time of the current vertex,
            # then the edge (u, v) is a bridge
            if low[v] > disc_time[u]:
                bridges.append((u, v))
        elif v != parent[u]:
            # If the vertex has been visited before and it is not the parent of the current vertex,
            # update the low time of the current vertex
            low[u] = min(low[u], disc_time[v])

    return time


# Construct an undirected graph as an adjacency list
graph = {
    1: [2],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5],
    5: [4, 6],
    6: [5]
}

if __name__ == '__main__':
    bridges = find_bridges(graph, 6)
    print(bridges)
