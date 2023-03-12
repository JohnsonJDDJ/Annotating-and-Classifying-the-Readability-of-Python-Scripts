from typing import List
from collections import deque

class Solution:
    def maxAreaofIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        biggest_island = 0
        visited = [[False for i in range(col)] for j in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and visited[i][j] is False:
                    island_area = self.visitIsland(grid, visited, i,j)
                    biggest_island = max(island_area,biggest_island)
        return biggest_island

    def visitIsland(self, grid: List[List[int]], visited: List[List[int]], i: int, j: int) -> int:
        neighbours = deque([(i,j)])
        area = 0
        while neighbours:
            row,col = neighbours.popleft()
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                continue
            if visited[row][col] is False and grid[row][col] == 1:
                visited[row][col] = True
                area += 1
                neighbours.extend([(row + 1,col)])
                neighbours.extend([(row - 1, col)])
                neighbours.extend([(row, col + 1)])
                neighbours.extend([(row, col - 1)])
        return area

if __name__ == '__main__':
    solution = Solution()
    case1 = [[0,0,0,0,0,0,0,0]]
    assert solution.maxAreaofIsland(case1) == 0

    case2 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
             [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    assert solution.maxAreaofIsland(case2) == 6

    case3 = [[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 1, 0, 0]]

    assert solution.maxAreaofIsland(case3) == 5