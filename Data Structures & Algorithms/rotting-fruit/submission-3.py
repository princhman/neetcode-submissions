class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        y_size = len(grid)
        x_size = len(grid[0])

        dirs = [(1,0), (-1, 0), (0, -1), (0, 1)]
        
        queue = []
        visited = []
        adj = []
        count = 0
        for y in range(y_size):
            for x in range(x_size):
                neighbours = []
                if grid[y][x] == 1 or grid[y][x] ==2:
                    if grid[y][x] == 2:
                        queue.append(y*x_size + x)
                    else:
                        count +=1
                    for dir in dirs:
                        new_x = x + dir[0]
                        new_y = y + dir[1]

                        if new_x >= 0 and new_x < x_size and new_y >= 0 and new_y < y_size:
                            if grid[new_y][new_x] == 1: 
                                neighbours.append(new_y * x_size + new_x)
                visited.append(False)
                adj.append(neighbours)
        
        if count == 0:
            return 0

        if len(queue) == 0:
            return -1
        
        queue.append("A")
        new_queue = []
        minutes = 0
        while len(queue) != 0:
            item = queue.pop(0)
            if item == "A":
                if (len(new_queue) == 0): 
                    break
                queue = new_queue + ["A"]
                new_queue = []
                minutes +=1
            else:
                for k in adj[item]:
                    if not visited[k]:
                        new_queue.append(k)
                        visited[k] = True
                        count -= 1
        if count != 0:
            return -1
        return minutes
            
        

           

