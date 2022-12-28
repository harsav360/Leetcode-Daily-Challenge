Problem Statement -> You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile, and an integer k. You should apply the following operation exactly k times:

Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
Notice that you can apply the operation on the same pile more than once.

Return the minimum possible total number of stones remaining after applying the k operations.

floor(x) is the greatest integer that is smaller than or equal to x (i.e., rounds x down).

For Example -> Input: piles = [5,4,9], k = 2
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [5,4,5].
- Apply the operation on pile 0. The resulting piles are [3,4,5].
The total number of stones in [3,4,5] is 12.

Brute Force Approach : Iterate in while until k is not equal to zero and sort the piles array every time in reverse order and make operation on first element of piles
 everytime.
Time Complexity -> O(N*LogN) for sorting and k times for iteration in while loop.
Total Time complexity -> O(K*NlogN)
Space Complexity -> O(1)

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        while k:
            piles.sort(reverse = True)
            piles[0] = math.ceil(piles[0]/2)
            k -= 1
        return sum(piles)
      
Optimized Version -> We will use the concept of heapify to stop sorting the array everytime.

In Python, we don't have max heap, so we have to convert the below list to max heap by multiplying each element by -1.
Time Complexity - O(K*logn)
Space Complexity -> O(N) #For making heap

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = -1*piles[i]
        heapq.heapify(piles)
        while k:
            heapq.heapreplace(piles,math.floor(piles[0]/2))
            k -= 1
        ans = sum(piles)
        return -1*ans
