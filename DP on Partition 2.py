Given a wooden stick of length n units. The stick is labelled from 0 to n. For example, a stick of length 6 is labelled as follows:


Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.

You should perform the cuts in order, you can change the order of the cuts as you wish.

The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.

Return the minimum total cost of the cuts.Given a wooden stick of length n units. The stick is labelled from 0 to n. For example, a stick of length 6 is labelled as follows:


Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.

You should perform the cuts in order, you can change the order of the cuts as you wish.

The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.

Return the minimum total cost of the cuts.


def minCost(self, n: int, cuts: List[int]) -> int:
        def solve(i,j):
            if i > j:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            ans = float('inf')
            for ind in range(i,j+1):
                steps = cuts[j+1] - cuts[i-1] + solve(i,ind-1) + solve(ind+1,j)
                ans = min(ans,steps)
            memo[i][j] = ans
            return ans
        c = len(cuts)
        memo = [[-1 for _ in range(c+1)] for _ in range(c+1)]
        cuts.insert(0,0)
        cuts.append(n)
        cuts.sort()
        return solve(1,c)
