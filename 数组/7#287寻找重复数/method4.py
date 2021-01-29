class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        quick = nums[nums[0]]
        while slow != quick:
            slow = nums[slow]
            quick = nums[nums[quick]]
        slow = 0
        while slow != quick:
            slow = nums[slow]
            quick = nums[quick]
        return slow
# 双指针 O(n) O(1)
# 第一阶段： 快慢指针先到达相遇点p，慢指针设为0，快指针为p
# 第二阶段： 快慢指针同时+1, 如果相等，相当于到达链表环的入口即为题解
