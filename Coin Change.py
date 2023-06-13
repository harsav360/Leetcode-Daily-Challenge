You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Recursion + Memoization
        
        mod = 1000000007
        # def solve(index,amt):
        #     if index == 0:
        #         if amt%coins[index] == 0:
        #             return amt//coins[index]
        #         else:
        #             return mod 
        #     if memo[index][amt] != -1:
        #         return memo[index][amt]
        #     notTake = solve(index-1,amt)
        #     take = float('inf')
        #     if coins[index] <= amt:
        #         take = 1 + solve(index,amt-coins[index])
        #     memo[index][amt] =  min(notTake,take)
        #     return memo[index][amt]

        # memo = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]

        # ans =  solve(len(coins)-1,amount)
        # if ans == mod:
        #     return -1
        # return ans

        # Tabulation

        n = len(coins)
        dp = [[mod]*(amount+1) for _ in range(n)]
        # Write Base Cases
        for i in range(amount+1):
            if i%coins[0] == 0:
                dp[0][i] = i//coins[0]

        for index in range(1,n):
            for amt in range(amount+1):
                notTake = dp[index-1][amt]
                take = mod
                if coins[index] <= amt:
                    take = 1 + dp[index][amt-coins[index]]
                dp[index][amt] =  min(notTake,take)
        if dp[n-1][amount] == mod:
            return -1
        return dp[n-1][amount]
