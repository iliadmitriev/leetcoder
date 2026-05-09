import bisect

class TimeMap:

    def __init__(self):
        self.timestamps = defaultdict(list)
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # store tuples ordered by timestamp ascending
        # since timestamps are increasing
        self.timestamps[key].append(timestamp)
        self.values[key].append(value)
        
    def get(self, key: str, timestamp: int) -> str:
        # if there is no such key, or first item stored under key has a greater timestamp
        # there is no value
        if key not in self.timestamps or timestamp < self.timestamps[key][0]:
            return ""
        
        # search for index
        index = bisect.bisect_left(self.timestamps[key], timestamp)
        
        # shift position left if not found
        if index == len(self.timestamps[key]) or self.timestamps[key][index] != timestamp:
            index -= 1
        
        return self.values[key][index]
        
