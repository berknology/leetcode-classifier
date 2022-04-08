import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            if len(self.min_heap) < self.k:
                heapq.heappush(self.min_heap, num)
            else:
                if num > self.min_heap[0]:
                    heapq.heappushpop(self.min_heap, num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        else: 
            heapq.heappushpop(self.min_heap, val)
        return self.min_heap[0]
