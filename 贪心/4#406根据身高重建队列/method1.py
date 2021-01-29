class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x:(-x[0], x[1]))
        out = []
        for p in people:
            out.insert(p[1], p)
        return out
#O(N^2) O(N)
