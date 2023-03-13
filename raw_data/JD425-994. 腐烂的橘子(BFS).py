class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid) == 0:
            return -1

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        lr = len(grid)
        lc = len(grid[0])

        # 因为腐烂一次
        res = -1
        queue = []

        # count是用来记录存不存在新鲜的橘子，假如说没有新鲜的橘子，那么直接返回0
        # 这是用来处理 corner case的
        count = 0

        for i in range(lr):
            for j in range(lc):
                # 有腐烂的橘子，我们待会就要从腐烂的橘子出发，做BFS
                if grid[i][j] == 2:
                    queue.append([i, j])
                # 解决corner case
                elif grid[i][j] == 1:
                    count += 1

        if count == 0:
            return 0

        while queue:
            lenqueue = len(queue)

            for i in range(lenqueue):
                point = queue.pop(0)
                row = point[0]
                col = point[1]

                for dir in dirs:
                    r = row + dir[0]
                    c = col + dir[1]
                    if r >= 0 and c >= 0 and r < lr and c < lc and grid[r][c] == 1:
                        # 把新鲜橘子腐烂掉
                        grid[r][c] = 2
                        queue.append([r, c])
            res += 1

        # 假如说我们已经腐烂完了，但是里面还有新鲜的橘子，那么说明无法全部腐烂完成
        for row in grid:
            if 1 in row:
                return -1

        # 否则直接返回正确结果
        return res

"""
时间复杂度：O(nm)
即进行一次广度优先搜索的时间，其中 n=grid.length, m=grid[0].length
空间复杂度：O(nm)
广度优先搜索中队列里存放的状态最多不会超过 nm 个，最多需要O(nm)的空间，所以最后的空间复杂度为O(nm)。


本题基本上和289使用的是同一个解题模版，只不过是根据题目的条件不同，来进行略微的调整
"""