class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #11.23
        n = len(nums)
        stk = [0]
        res = [-1 for _ in range(n)]
        for i in range(1, 2*n):
            idx = i % n
            while stk and nums[idx] > nums[stk[-1]]:
                res[stk[-1]] = nums[idx]
                stk.pop()
            if not stk or idx > stk[-1]:
                stk.append(idx)
        return res


