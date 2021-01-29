class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        m = len(nums)
        flag = 0
        for i in range(1, m):
            if nums[i] < nums[i-1]:
                flag += 1
                if i-2 >= 0:
                    #increase i
                    if i+1 < m and nums[i] < nums[i-2] and nums[i+1] < nums[i-1]:
                        return False
                    #decrease i-1
                    #elif nums[i] >= nums[i-2] and nums[i-1] < nums[i]:
                        #return False
                if flag >= 2:
                    return False
        return True
#O(N) O(1)
