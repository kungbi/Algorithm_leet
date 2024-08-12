from heapq import heapify
from heapq import heappop
from heapq import heappush

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        sorted_nums = sorted(nums)[::-1]
        self.heap = sorted_nums[:k]
        heapify(self.heap)
        self.k = k
        

    def add(self, val: int) -> int:
        if self.k <= len(self.heap) and self.heap[0] < val:
            heappop(self.heap)
            heappush(self.heap, val)

        if len(self.heap) == 0 or len(self.heap) < self.k:
            heappush(self.heap, val)
        
        return self.heap[0] if len(self.heap) == self.k else None

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)