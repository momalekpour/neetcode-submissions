import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ## Solution 1: brtue force - sort given array after each game
        # time complexity: O(n. nlog(n)) = O(n^2.log(n))
        # sapce complexity: O(1)

        ## Solution 2: maxHeap - pop top 2 max values each game
        # time complexity: O(n . (log(n) + log(n))) = O(n.log(n))
        # space complexity: O(1)
        stones = [-1 * s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x, y = -heapq.heappop(stones), -heapq.heappop(stones)
            if x == y:
                continue
            else:
                new_stone = x - y if x > y else y - x
                heapq.heappush(stones, -new_stone)
        return -stones[0] if stones else 0
