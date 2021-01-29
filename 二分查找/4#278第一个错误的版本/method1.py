# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while True:
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                if mid - 1 > 0 and isBadVersion(mid-1): r = mid - 1
                else: return mid
            else:
                if isBadVersion(mid+1): return mid + 1
                else: l = mid + 1
