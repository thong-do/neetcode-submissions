class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            first, second = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            if first != second:
                remaining = first - second
                heapq.heappush(maxHeap, remaining)

        return abs(maxHeap[0]) if len(maxHeap) == 1 else 0