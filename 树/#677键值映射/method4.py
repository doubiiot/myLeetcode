class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        prenum = self.isKeyExist(key)

        for i in key:
            if i not in cur:
                cur[i] = {}
                cur[i]['prenum'] = prenum + val
            else:
                cur[i]['prenum'] += val - prenum
            cur = cur[i]
        cur['val'] = val
        cur['end'] = 1

    def isKeyExist(self, key):
        cur = self.root
        for i in key:
            if i not in cur:
                return 0
            else:
                cur = cur[i]
        return cur['val'] if cur.get('end', 0) else 0

    def sum(self, prefix: str) -> int:
        cur = self.root
        for i in prefix:
            if i not in cur:
                return 0
            cur = cur[i]
        return cur['prenum']

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# 稍微改进了一下method1
