Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them

def largestDivisibleSubset(self, arr: List[int]) -> List[int]:
        N = len(arr)
        arr.sort()
        dp = [1 for i in range(N)]
        lst = [0 for i in range(N)]
        maxi = 1
        for ind in range(N):
            lst[ind] = ind
            for prev in range(ind):
                if (arr[ind]%arr[prev] == 0) and 1 + dp[prev] > dp[ind]:
                    dp[ind] = 1+dp[prev]
                    lst[ind] = prev
        
        ans = -1
        lastIndex = -1
        for i in range(N):
            if dp[i] > ans:
                ans = dp[i]
                lastIndex = i
    
        ans = []
        ans.append(arr[lastIndex])
        while lst[lastIndex] != lastIndex:
            lastIndex = lst[lastIndex]
            ans.append(arr[lastIndex])
            
        ans.reverse()
        return ans
