#暴力法
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        #11.21
        length = len(T)
        dic, res, val = {}, [0] * length, 40000
        for i in range(length-1, -1, -1):
            dic[T[i]] = i
            min_idx = min(dic.get(j, val) for j in range(T[i]+1, 102))
            if min_idx != val:
                res[i] = min_idx - i
        return res
#O(mn) O(n)
