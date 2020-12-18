import heapq


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        self.n = 0

    def addNum(self, num: int) -> None:
        self.n += 1
        if len(self.max_heap) == 0:
            self.max_heap = [-num]
        else:
            if num > -self.max_heap[0]:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
            while len(self.min_heap) >= len(self.max_heap):
                element = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -element)
            while len(self.min_heap) + 1 < len(self.max_heap):
                element = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, -element)            

    def findMedian(self) -> float:
        if self.n%2 != 0:
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0]+self.min_heap[0])/2
        

"""
[4, 2, 3, 5, 6]

max_heap       [-4, -3, -2]  in max heap, all elments are smaller or equal to the elements in the min heap
----------------------------
min_heap       [5, 6] 


in Python, heap is default min heap

len(max_heap) == len(min_heap) + 1

"""
        
    

        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
