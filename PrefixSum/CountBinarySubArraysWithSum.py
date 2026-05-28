# https://leetcode.com/problems/binary-subarrays-with-sum/description/
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sub_arrays = 0
        mapping = {0:1} # sum 0, there is one subarray that is empy subarray
        prefix_sum = 0 # we start with 0 sum
        for i in range (len(nums)):
            prefix_sum += nums[i]
            rem = prefix_sum - goal
            if rem in mapping:
                sub_arrays += mapping [rem]  # number of previous prefix sums that make current subarray sum = goal
            mapping [prefix_sum] = mapping.get(prefix_sum,0) + 1
        
        return sub_arrays
