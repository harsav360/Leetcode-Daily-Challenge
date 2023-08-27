Problem Link -> https://leetcode.com/problems/maximize-the-profit-as-the-salesman/description/


def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        # Memoization Approach
        def solve(index,offers,memo):
            if index == len(offers):
                return 0
            if memo[index] != -1:
                return memo[index]
            notTake = solve(index+1,offers,memo)
            low ,high = index+1,len(offers)-1
            next_index = len(offers)
            while low <= high:
                mid = (low+high)//2
                if offers[mid][0] > offers[index][1]:
                    high = mid-1
                    next_index = mid
                else:
                    low = mid+1
            take = offers[index][2] + solve(next_index,offers,memo)
            memo[index] = max(take,notTake)
            return memo[index]

        n = len(offers)
        offers.sort()
        memo = [-1]*n
        return solve(0,offers,memo)
