import heapq

def astar(grid, start, goal):
    # Directions: Up, Down, Left, Right
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Priority queue stores: (priority, current_node)
    # priority = g_score + heuristic
    pq = [(0, start)]
    
    came_from = {}
    g_score = {start: 0}
    
    while pq:
        # Get the node with the lowest f_score
    
        current_f, current = heapq.heappop(pq)
        
        if current == goal:
            # Reconstruct the path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1] # Return reversed path

        for dx, dy in neighbors:
            neighbor = (current[0] + dx, current[1] + dy)
            
            # Check boundaries and obstacles
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue
                
                # Distance from start to neighbor is (current g_score + 1)
                tentative_g = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    # This path to neighbor is better than any previous one
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    
                    # Manhattan Distance Heuristic: |x1 - x2| + |y1 - y2|
                    h = abs(neighbor[0] - goal[0]) + abs(neighbor[1] - goal[1])
                    f = tentative_g + h
                    
                    heapq.heappush(pq, (f, neighbor))
                    
    return None # No path found

# Example Usage:
# 0 = Path, 1 = Wall
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]
start_pos = (0, 0)
goal_pos = (2, 4)

path = astar(grid, start_pos, goal_pos)
print(f"Path found: {path}")