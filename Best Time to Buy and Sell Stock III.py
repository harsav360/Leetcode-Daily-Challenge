You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Approach => Recursion + Memoization + Tabulation

def maxProfit(self, prices: List[int]) -> int:
        # def solve(ind,buy,cap):
        #     if cap == 0 or ind == n:
        #         return 0
        #     if (ind,buy,cap) in memo:
        #         return memo[(ind,buy,cap)]
        #     if buy:
        #         memo[(ind,buy,cap)] =  max(-prices[ind] + solve(ind+1,0,cap),solve(ind+1,1,cap))
        #         return memo[(ind,buy,cap)]
        #     else:
        #         memo[(ind,buy,cap)] =  max(prices[ind] + solve(ind+1,1,cap-1),solve(ind+1,0,cap))
        #         return memo[(ind,buy,cap)]

        # n = len(prices)
        # memo = {}
        # return solve(0,1,2)

        #Tabulation
        n = len(prices)

        dp = [[[0 for i in range(3)] for _ in range(2)] for _ in range(n+1)]

        for ind in range(n):
            for buy in range(2):
                dp[ind][buy][0] = 0

        for buy in range(2):
            for cap in range(3):
                dp[n][buy][cap] = 0

        for ind in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(1,3):
                    if buy:
                        dp[ind][buy][cap] = max(-prices[ind] + dp[ind+1][0][cap],dp[ind+1][1][cap])
                    else:
                        dp[ind][buy][cap] = max(prices[ind]+dp[ind+1][1][cap-1],dp[ind+1][0][cap])
        return dp[ind][1][2]
