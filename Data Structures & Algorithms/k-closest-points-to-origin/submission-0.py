import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Solution 1: a naive approach -> 1) compute distnaces 2) sort distances and pick top-k points
        # time complexity: O(n + n.log(n))
        # space complexity: O(n) + O(1) or O(n) based on sorting algo

        # Solution 2: using min-heap -> 1) compute distances 2) heapfiy them 3 ) pop top-k points from heap
        # time complexity: O(n + n + k.long(n))
        # space complexity: O(n)
        
        def get_distance(p1, p2):
            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]
            d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            return d

        for p in points:
            p.insert(0, get_distance(p, [0,0]))
        
        heapq.heapify(points)
    
        res = []
        for i in range(k):
            curr_closest = heapq.heappop(points)
            res.append(curr_closest[1:])
        
        return res
