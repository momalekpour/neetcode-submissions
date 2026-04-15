import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ## Solution 1: naive approche - sorting the array and picking index k
        # time complexity: O(n.log(n))
        # space complexity: O(n)

        ## Solution 2: max heap
        # time complexity: O(n + k.long(n))
        # space complexity

        # python only supports minHeap -> so we change sign of each num to negative to have maxHeap
        nums = [-num for num in nums]
        min_heap = heapq.heapify(nums)
        for i in range(k):
            res = heapq.heappop(nums)
        return -res
