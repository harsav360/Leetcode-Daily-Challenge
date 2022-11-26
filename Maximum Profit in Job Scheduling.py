We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Brute force approach -> Take or not Take simple Like Knapsack. But Time Complexity will be O(2^n)
Dynamic Programming or Memoization approach. Time Complexity -> O(N^2)
Third and optimal approach is DP+Binary Search. Time Complexity -> O(NlogN)

#Dynamic Programming Approach
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:


        def solve(dx):
            if dx >= N:
                return 0
            if dp[dx] != -1:
                return dp[dx]
            excl = solve(dx+1)
            incl = jobs[dx][2]

            for i in range(dx+1,N):
                if jobs[dx][1] <= jobs[i][0]:
                    incl += solve(i)
                    break
            dp[dx] = max(incl,excl)
            return dp[dx]
            


        jobs = sorted(zip(startTime,endTime,profit))
        N = len(jobs)
        dp = [-1]*(N)
        return solve(0)
      
      #Optimal Approach.
      class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:


        @lru_cache(None)
        def solve(dx):
            if dx >= N:
                return 0
            new_i = bisect.bisect_left(startTime,jobs[dx][1])  #Act Like Binary Search to find the position for Insertion
            return max(solve(dx+1),jobs[dx][2]+solve(new_i))
            


        jobs = sorted(zip(startTime,endTime,profit))
        startTime = [job[0] for job in jobs]
        N = len(jobs)
        return solve(0)
