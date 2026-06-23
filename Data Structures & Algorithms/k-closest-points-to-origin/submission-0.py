class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        res = []
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            distances.append((distance, point))

        heapq.heapify(distances)

        while k:
            point = heapq.heappop(distances)
            res.append(point[1])
            k -= 1

        return res