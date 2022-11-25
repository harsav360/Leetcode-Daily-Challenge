Problem Statement -> 
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. 
Since the answer may be large, return the answer modulo 109 + 7.
Example -> 
          Input: arr = [3,1,2,4]
          Output: 17
          Explanation: 
          Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
          Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
          Sum is 17.
          
 class node:
    def __init__(self,value,count):
        self.value = value
        self.count = count
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        left = [0]*len(arr)
        right = [0]*len(arr)
        stack1 = []  #This stack is used to find, How many numbers are greater than the current number in array in left side.
        stack2 = []  #This stack is used to find, How many numbers are greater than the current number in array in right side.
        mod = 1000000007

        #filling the left subarray

        for i in range(len(arr)):
            count = 1
            while stack1 and stack1[-1].value > arr[i]:
                count += stack1[-1].count
                stack1.pop()
            stack1.append(node(arr[i],count))
            left[i] = count
            
        #Filling the right Subarray.

        for j in range(len(arr)-1,-1,-1):
            count = 1
            while stack2 and stack2[-1].value >= arr[j]:
                count += stack2[-1].count
                stack2.pop()
            stack2.append(node(arr[j],count))
            right[j] = count
       ans = 0
        for k in range(len(arr)):
            ans += arr[k]*left[k]*right[k]  #Multiplying the number with left count and right count, Because we need to return the Sum.
        return ans%mod
