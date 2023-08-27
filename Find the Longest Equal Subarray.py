Problem and Appraoch Link -> https://leetcode.com/problems/find-the-longest-equal-subarray/description/

def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        # n,ans = len(nums),0
        # for i in range(n):
        #     count = 1
        #     check = k
        #     index = i+1
        #     while index < n:
        #         if nums[i] == nums[index]:
        #             count += 1
        #             index += 1
        #         elif check > 0:
        #             check -= 1
        #             index += 1
        #         else:
        #             break
        #     ans = max(ans,count)
        # return ans
        
        # temp = []
        # n = len(nums)
        # for i in range(n):
        #     temp.append([nums[i],i])
        # temp.sort()
        # ans = 1
        # check = k
        # flag = 1
        # count = 1
        # for i in range(1,n):
        #     if temp[i-1][0] == temp[i][0] and flag:
        #         diff = temp[i][1]-temp[i-1][1]-1
        #         if diff <= check:
        #             check -= diff
        #             count += 1
        #         else:
        #             flag = 0
        #     else:
        #         count = 1
        #         check = k
        #         flag = 1
        #     ans = max(ans,count)
        # return ans
                
        maxf = i = 0
        count = Counter()
        for j in range(len(nums)):
            count[nums[j]] += 1
            maxf = max(maxf, count[nums[j]])
            if j - i + 1 - maxf > k:
                count[nums[i]] -= 1
                i += 1
        return maxf
