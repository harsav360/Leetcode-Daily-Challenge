Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

Three Solution -> Recursive, Memoization and Top-Down DP

#Just remove memo part to fullly convert it into recursive

def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # def solve(index,target):
        #     if target == 0:
        #         return True
        #     if index == 0:
        #         return nums[index] == target
        #     if memo[index][target] != -1:
        #         return memo[index][target]
        #     notTake = solve(index-1,target)
        #     take = False
        #     if nums[index] <= target:
        #         take = solve(index-1,target-nums[index])
        #     memo[index][target] =  notTake or take
        #     return notTake or take
        # target = sum(nums)
        # if target%2 != 0:
        #     return False
        # else:
        #     target //= 2
        # N = len(nums)-1
        # memo = [[-1 for j in range(target+1)] for i in range(N+1)]
        # return solve(N,target)

        target = sum(nums)
        if target%2 != 0:
            return False
        else:
            target //= 2

        N = len(nums)
        dp = [[False for i in range(target+1)] for j in range(N)]
        for i in range(N):
            dp[i][0] = True
        dp[0][target] = nums[0] == target 
        for i in range(1,N):
            for j in range(1,target+1):
                notTake = dp[i-1][j]
                take = False
                if nums[i] <= j:
                    take = dp[i-1][j-nums[i]]
                dp[i][j] = notTake or take
        return dp[N-1][target]
