You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.

For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.

Three Approaches

        n = len(nums)
        ans = [-1]*n
        # for i in range(k,n-k):
        #     ans[i] = sum(nums[i-k:i]) + sum(nums[i:i+k+1])
        #     ans[i] //= (2*k+1)
        # print(ans)
        # return ans

        # prefix = []
        # s = 0
        # for i in nums:
        #     s += i
        #     prefix.append(s)
        # prev,right,curr_sum = 0,0,0
        # div = (2*k)+1

        # while right+k < n:
        #     if right < k:
        #         curr_sum += nums[right]
        #         right += 1
        #     else:
        #         curr_sum += nums[right]
        #         total = prefix[right+k] - prefix[right] + curr_sum
        #         total //= div
        #         ans[right] = total
        #         curr_sum -= nums[prev]
        #         prev += 1
        #         right += 1
        # return ans

        left,diameter,curr_sum = 0,2*k+1,0
        for right in range(len(nums)):
            curr_sum += nums[right]
            if (right-left+1) >= diameter:
                ans[left+k] = curr_sum//diameter
                curr_sum -= nums[left]
                left += 1
        return ans
