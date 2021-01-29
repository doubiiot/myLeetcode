class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def push_up(dic_l, dic_r):
            dic = {}
            dic['isum'] = dic_l['isum'] + dic_r['isum']
            dic['lsum'] = max(dic_l['lsum'], dic_l['isum'] + dic_r['lsum'])
            dic['rsum'] = max(dic_r['rsum'], dic_l['rsum'] + dic_r['isum'])
            dic['msum'] = max(dic_l['msum'], dic_r['msum'], dic_l['rsum'] + dic_r['lsum'])
            return dic
        def get_max_subarray(l, r):
            dic = {}
            if l == r:
                dic['isum']=dic['lsum']=dic['rsum']=dic['msum']=nums[l]
            else:
                mid = (l + r) // 2
                dic_l = get_max_subarray(l, mid)
                dic_r = get_max_subarray(mid+1 , r)
                dic = push_up(dic_l, dic_r)
            return dic
        return get_max_subarray(0, len(nums)-1)['msum']
