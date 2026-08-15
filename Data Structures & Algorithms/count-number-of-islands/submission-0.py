import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                # Fixed the typo here: [0, -1]
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    # Check boundaries and if it's land we haven't visited
                    if (nr in range(rows) and 
                        nc in range(cols) and 
                        grid[nr][nc] == "1" and 
                        (nr, nc) not in visit):
                        q.append((nr, nc))
                        visit.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                # Only start a BFS if we find unvisited land
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
                    
        return islands