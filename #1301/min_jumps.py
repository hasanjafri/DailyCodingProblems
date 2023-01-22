def min_jumps(N):
    # Initialize the queue with the first node and its distance from the starting point
    queue = [(0, 0)]
    visited = set()
    # Perform Breadth First Search
    while queue:
        # Get the node with the smallest distance
        curr, dist = queue.pop(0)
        # If the current node is the target node, return the distance
        if curr == N:
            return dist
        # Skip if the node has been visited
        if curr in visited:
            continue
        # Mark the node as visited
        visited.add(curr)
        # Add the next possible nodes to the queue
        for i in range(1, dist + 2):
            queue.append((curr + i, dist + 1))
            queue.append((curr - i, dist + 1))
    # If the target node is not reached, return -1
    return -1

N = 10

if __name__ == '__main__':
    print(min_jumps(N)) # Output 2
