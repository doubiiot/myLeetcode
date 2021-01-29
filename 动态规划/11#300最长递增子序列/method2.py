class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            if not res or num > res[-1]: res.append(num)
            else:
                l, r = 0, len(res) - 1
                loc = r
                while l <= r:
                    mid = l + (r - l) // 2
                    if res[mid] >= num:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                res[loc] = num
        return len(res)

# O(logn) O(n)
