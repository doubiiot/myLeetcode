class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_pos = [0] * 26
        for idx,s in enumerate(S):
            last_pos[ord(s)-ord('a')] = idx
        partition = []
        start = end = 0
        for idx,s in enumerate(S):
            end = max(end, last_pos[ord(s)-ord('a')])
            if idx == end:
                partition.append(end - start + 1)
                start = end + 1
        return partition

