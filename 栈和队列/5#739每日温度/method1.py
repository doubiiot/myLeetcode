class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        #11.21
        length = len(T)
        idx_stk = []
        res = [0] * length
        for i in range(length):
            while idx_stk and T[i] > T[idx_stk[-1]]:
                res[idx_stk[-1]] = i - idx_stk[-1]
                idx_stk.pop()
            idx_stk.append(i)
        return res
# O(N) o(N)
