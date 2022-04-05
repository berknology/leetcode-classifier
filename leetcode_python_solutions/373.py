import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        ans = []
        visited = {(0, 0)}
        p1 = p2 = 0
        min_heap = [(nums1[p1]+nums2[p2], p1, p2)]
        while k > 0 and min_heap:
            k -= 1
            _, p1, p2 = heapq.heappop(min_heap)
            ans.append([nums1[p1], nums2[p2]])
            if p2+1 < len(nums2) and (p1, p2+1) not in visited:
                visited.add((p1, p2+1))
                heapq.heappush(min_heap, (nums1[p1]+nums2[p2+1], p1, p2+1))
            if p1+1 < len(nums1) and (p1+1, p2) not in visited:
                visited.add((p1+1, p2))
                heapq.heappush(min_heap, (nums1[p1+1]+nums2[p2], p1+1, p2))
        return ans

        
"""
Top K problem

heap: in python, heap is min heap

(1, 1)   (0, 0)
(1, 2)   (0, 1)
(1, 1)   (1, 0)
(1, 2)   (1, 1)
(2, 1)   (2, 0)
         (0, 2)
         (1, 1)



"""
