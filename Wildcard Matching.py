Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # def solve(ind1,ind2):
        #     if ind1 < 0 and ind2 < 0:
        #         return True
        #     elif ind2 < 0 and ind1 >= 0:
        #         return False
        #     elif ind1 < 0:
        #         for k in range(ind2+1):
        #             if p[k] != '*':
        #                 return False
        #         return True
        #     if memo[ind1][ind2] != -1:
        #         return memo[ind1][ind2]

        #     if s[ind1] == p[ind2] or p[ind2] == '?':
        #         memo[ind1][ind2] = solve(ind1-1,ind2-1)
        #         return memo[ind1][ind2]
        #     elif p[ind2] == '*':
        #         memo[ind1][ind2] = solve(ind1-1,ind2) or solve(ind1,ind2-1)
        #         return memo[ind1][ind2]
        #     return False

        # memo = [[-1]*(len(p)) for _ in range(len(s))]

        # return solve(len(s)-1,len(p)-1)

        n,m = len(p),len(s)
        dp = [[False]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            flag = True
            for k in range(1,i+1):
                if p[k-1] != "*":
                    flag = False
                    break
            dp[i][0] = flag
        dp[0][0] = True


        for i in range(1,n+1):
            for j in range(1,m+1):
                if p[i-1] == s[j-1] or p[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = False

        return dp[n][m]
