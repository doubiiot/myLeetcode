class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = []
        l, r = 1, n
        while l <= r:
            # 加入k-1数
            if k > 1:
                if k % 2:
                    res.append(l)
                    l += 1
                else:
                    res.append(r)
                    r -= 1
                k -= 1
            # 补1
            else:
                res.append(l)
                l += 1
        return res
