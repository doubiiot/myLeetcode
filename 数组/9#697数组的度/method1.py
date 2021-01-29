class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = {}
        max_fre = 1
        for idx, num in enumerate(nums):
            if num in dic:
                dic[num][1] = idx
                dic[num][2] += 1
                max_fre = max(dic[num][2], max_fre)
            else:
                dic[num] = [idx,idx,1]
        min_len = 50001
        for k, v in dic.items():
            if v[2] == max_fre:
                min_len = min(v[1]-v[0]+1, min_len)
        return min_len

#O(N) O(MN)
