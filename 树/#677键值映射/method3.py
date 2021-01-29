class MapSum:
    def __init__(self):
        self.root = {}

    def insert(self, key: str, val: int) -> None:
        self.root[key] = val

    def sum(self, prefix: str) -> int:
        return sum(self.root[s] for s in self.root if s.startswith(prefix))

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

# 方法2的改进 暴力法
