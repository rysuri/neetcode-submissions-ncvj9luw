class TimeMap:

    def __init__(self):
        self.mem = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mem[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.mem[key]) - 1
        array = self.mem[key]
        while l <= r:
            mid = l + ((r-l)//2)
            
            if timestamp < array[mid][0]:
                r = mid - 1
            elif timestamp > array[mid][0]:
                l = mid + 1
            else:
                return array[mid][1]

        if r < 0:
            return ""
        else:
            return array[r][1]


