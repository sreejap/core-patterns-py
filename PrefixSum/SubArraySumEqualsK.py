# https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0

        sum_map = {0:1} # map of sum to number
        sub_arrays = 0
        for i in range (len(nums)):
            prefix_sum += nums[i]

            if (prefix_sum - k) in sum_map:
                sub_arrays += sum_map [prefix_sum-k]
            
            sum_map [prefix_sum] = sum_map.get(prefix_sum,0)+1 

        return sub_arrays
