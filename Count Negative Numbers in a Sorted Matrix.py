Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

Solution:
  
  def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Binary Search Solution
        # def binary_search(arr):
        #     high = 0
        #     low = len(arr) - 1

        #     while high <= low:
        #         mid = (low+high)//2
        #         if arr[mid] < 0:
        #             low -= 1
        #         else:
        #             high += 1
        #     return low+1
        
        # ans = 0
        # row = len(grid)
        # col = len(grid[0])
        # for i in range(row):
        #     res = col - binary_search(grid[i])
        #     ans += res
        # return ans

        #Staircase Solution

        m,n = len(grid),len(grid[0])
        r,c,ans = 0,n-1,0
        while r < m and c >= 0:
            if grid[r][c] < 0:
                ans += m-r
                c -= 1
            else:
                r += 1
        return ans
