from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs_iterative(graph, start_node):
    visited = set()
    # Use a queue (FIFO) for BFS
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        # Remove the first element added
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("Iterative BFS:")
bfs_iterative(graph, 'A')