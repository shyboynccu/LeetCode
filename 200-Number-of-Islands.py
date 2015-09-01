# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# 11110
# 11010
# 11000
# 00000
# Answer: 1

# Example 2:

# 11000
# 11000
# 00100
# 00011
# Answer: 3
import unittest

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        land_count = 0

        for row_index in range(len(grid)):
            for col_index in range(len(grid[row_index])):
                if grid[row_index][col_index] == '1':
                    self.visit_neighboring_land(row_index, col_index, grid)
                    land_count += 1
        
        return land_count

    def visit_neighboring_land(self, row_index, col_index, grid):
        grid[row_index][col_index] = '0'
        
        if col_index - 1 >= 0 and grid[row_index][col_index - 1] == '1': # go left 
            self.visit_neighboring_land(row_index, col_index - 1, grid)

        if col_index + 1 < len(grid[row_index]) and grid[row_index][col_index + 1] == '1': # go right 
            self.visit_neighboring_land(row_index, col_index + 1, grid)

        if row_index - 1 >= 0 and grid[row_index - 1][col_index] == '1': # go up
            self.visit_neighboring_land(row_index - 1, col_index, grid)

        if row_index + 1 < len(grid) and grid[row_index + 1][col_index] == '1': # go down
            self.visit_neighboring_land(row_index + 1, col_index, grid)
        
class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        grid = [['1', '1', '1', '1', '0'],
                ['1', '1', '0', '1', '0'],
                ['1', '1', '0', '0', '0'],
                ['0', '0', '0', '0', '0']]    
        
        self.assertEqual(1, self.solution.numIslands(grid))

    def test_case2(self):
        grid = [['1', '1', '0', '0', '0'],
                ['1', '1', '0', '0', '0'],
                ['0', '0', '1', '0', '0'],
                ['0', '0', '0', '1', '1']]
        
        self.assertEqual(3, self.solution.numIslands(grid))

    def test_case3(self):
        grid = [['1']]
        
        self.assertEqual(1, self.solution.numIslands(grid))

    def test_case3(self):
        grid = [['1', '1', '1'],
                ['0', '1', '0'],
                ['1', '1', '1']]
        
        self.assertEqual(1, self.solution.numIslands(grid))


if __name__ == '__main__':
    unittest.main()        
    
