Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.


def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            dp[i][0] = matrix[i][0]
        for j in range(col):
            dp[0][j] = matrix[0][j]
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) + 1
        ans = 0
        for i in range(row):
            for j in range(col):
                ans += dp[i][j]
        
        return ans
