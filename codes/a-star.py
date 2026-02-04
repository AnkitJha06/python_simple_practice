import heapq

def astar(grid, start, goal):
    
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    pq = [(0, start)]
    
    came_from = {}
    g_score = {start: 0}
    
    while pq:
        
    
        current_f, current = heapq.heappop(pq)
        
        if current == goal:
            
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1] # Return reversed path

        for dx, dy in neighbors:
            neighbor = (current[0] + dx, current[1] + dy)
            
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue
                
                tentative_g = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:

                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    
                    h = abs(neighbor[0] - goal[0]) + abs(neighbor[1] - goal[1])
                    f = tentative_g + h
                    
                    heapq.heappush(pq, (f, neighbor))
                    
    return None # 


grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]
start_pos = (0, 0)
goal_pos = (2, 4)

path = astar(grid, start_pos, goal_pos)
print(f"Path found: {path}")
