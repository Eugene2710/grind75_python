class TimeMap:
    """
    Using a hashmap and binary search,
    hashmap to store the str as key, a nested list of tuple of str and int(timestamp_ as value
    set operation: create empty list to key if key does not exist, and append value to key accordingly
    time complexity: O(1), space complexity: O(N)
    get operation:
    if key does not exist, return ""
    else: perform binary search to look for str in value of input key
    time complexity: O(logN)
    space complexity: O(1)
    """
    def __init__(self):
        self.store: dict[list[tuple[str, int]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key is not in self.store:
            self.store[key] = []
        self.store[key].append((value, str))

    def get(self, key: str, timestamp: int) -> str:
        if key is not in self.store:
            return ""
        res: str = ""
        values: list[tuple[str, int]] = self.store[key]
        l: int = 0
        r: int = len(values)-1

        while l<=r:
            m: (l+r)//2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m+1
            else:
                r = m-1
        return res