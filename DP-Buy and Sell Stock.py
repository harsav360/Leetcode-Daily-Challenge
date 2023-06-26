You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

def maxProfit(self, prices):
        # notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
        # for p in prices:
        #     hold, notHold, notHold_cooldown = max(hold, notHold - p), max(notHold, notHold_cooldown), hold + p
        # return max(notHold, notHold_cooldown)

        # Recursion + Memoization

        # def solve(ind,buy):
        #     if ind >= n:
        #         return 0
        #     if memo[ind][buy] != -1:
        #         return memo[ind][buy]
        #     if buy:
        #         memo[ind][buy] =  max(-prices[ind] + solve(ind+1,0),solve(ind+1,buy))
        #         return memo[ind][buy]
        #     else:
        #         memo[ind][buy] =  max(prices[ind] + solve(ind+2,1),solve(ind+1,buy))
        #         return memo[ind][buy]

        # n = len(prices)
        # memo = [[-1 for _ in range(2)] for _ in range(n)]
        # return solve(0,1)

        # Tabulation

        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n+2)]
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                if buy:
                    dp[ind][buy] = max(-prices[ind]+dp[ind+1][0],dp[ind+1][buy])
                else:
                    dp[ind][buy] = max(prices[ind]+dp[ind+2][1],dp[ind+1][buy])

        return dp[0][1]
