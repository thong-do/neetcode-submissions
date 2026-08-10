class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        for i in nums:
            count[i] = 1 + count.get(i, 0)

        heap = []
        for num, cnt in count.items():
            heapq.heappush(heap, (cnt, num))
            if len(heap) > k:
                heapq.heappop(heap)

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
        