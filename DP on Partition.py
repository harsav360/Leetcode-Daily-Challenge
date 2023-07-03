Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
.

Return the minimum cuts needed for a palindrome partitioning of s.

def minCut(self, s: str) -> int:
        def isPalin(i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        # def solve(i):
        #     if i == n:
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]

        #     minCost = float('inf')
        #     for j in range(i,n):
        #         if isPalin(i,j):
        #             cost = 1 + solve(j+1)
        #             minCost = min(minCost,cost)
        #     dp[i] = minCost
        #     return minCost

        if s == s[::-1]:
            return 0
        
        for i in range(len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1

        n = len(s)
        dp = [0 for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            minCost = float('inf')
            for j in range(i,n):
                if isPalin(i,j):
                    cost = 1 + dp[j+1]
                    minCost = min(minCost,cost)
            dp[i] = minCost
        return dp[0]-1
