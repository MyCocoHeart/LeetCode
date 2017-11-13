#encoding = utf-8
"""
@version:??
@author: xq
@contact:xiaoq_xiaoq@163.com
@file: maxAreaofIsland.py
@time: 2017/11/13 20:38
"""


class Solution(object):
    '''
    Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
    '''
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        seen = set()
        rowNum = len(grid)
        colNum = len(grid[0])

        def areas(row, col):
            if not (0 <= row < rowNum and 0 <= col < colNum and (row, col) not in seen and grid[row][col]):
                return 0
            seen.add((row, col))
            return (1 + areas(row + 1, col) + areas(row - 1, col) + areas(row, col + 1) + areas(row, col - 1))

        if (grid == []):
            return 0
        else:
            return max(areas(row, col) for row in range(rowNum) for col in range(colNum))