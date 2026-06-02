class TimeMap:
    data = {}
    
    def __init__(self):
        self.data = {}
        return

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = [[], []]
        self.data[key][0].append(timestamp)
        self.data[key][1].append(value)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        if timestamp < self.data[key][0][0]:
            return ""
        
        if timestamp > self.data[key][0][-1]:
            return self.data[key][1][-1]

        target = -1
        nearest = -1
        l, r = 0, len(self.data[key][0]) - 1
        while l <= r:
            a = (l + r)//2
            if self.data[key][0][a] == timestamp:
                target = a
                break
            if self.data[key][0][a] < timestamp:
                nearest = a
                l += 1
            else:
                r -= 1
        if target == -1:
            target = nearest
        
        return self.data[key][1][target]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)