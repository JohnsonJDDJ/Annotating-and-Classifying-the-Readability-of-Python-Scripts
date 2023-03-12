"""
在迷宫中有一个球，里面有空的空间和墙壁。球可以通过滚上，下，左或右移动，
但它不会停止滚动直到撞到墙上。当球停止时，它可以选择下一个方向。

给定球的起始位置，目的地和迷宫，确定球是否可以停在终点。

迷宫由二维数组表示。1表示墙和0表示空的空间。你可以假设迷宫的边界都是墙。开始和目标坐标用行和列索引表示。

map =
[
 [0,0,1,0,0],
 [0,0,0,0,0],
 [0,0,0,1,0],
 [1,1,0,1,1],
 [0,0,0,0,0]
]
start = [0,4]
end = [3,2]
输出:
false

对应lintcode787
"""

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """

    def has_path(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        visited = []
        q = [start]
        visited.append(start)

        while len(q) > 0:
            cur = q.pop(0)
            if cur == destination:
                return True

            for di, dj in dirs:
                ni = cur[0] + di
                nj = cur[1] + dj

                # 重点在这里，因为我们需要往一个方向走到底，就是得走到边界或撞墙才能停
                while 0 <= ni + di < len(maze) and 0 <= nj + dj < len(maze[0]) and maze[ni+di][nj+dj] == 0:
                    ni += di
                    nj += dj

                np = [ni, nj]
                # 假如没走过，则记录这个结果，并往下一个方向走
                if np not in visited:
                    q.append(np)
                    visited.append(np)

        return False

"""
古城算法 30:00
https://www.bilibili.com/video/BV1Rz4j1Z7tJ/?spm_id_from=333.337.search-card.all.click&vd_source=b81616a45fd239becaebfee25e0dbd35
"""