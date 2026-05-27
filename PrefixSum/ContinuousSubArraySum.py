# https://leetcode.com/problems/continuous-subarray-sum/editorial/
# https://leetcode.com/problems/continuous-subarray-sum/solutions/5276981/prefix-sum-hashmap-patterns-7-problems/ 
# We need Prefix Sum + Hashmap pattern because sliding window is only applicable when we know for sure if the prefixsum 
# is an increasing or decreasing function (i.e. Monotonous in nature)
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_mod = 0
        mod_seen = {0:-1}

        for i in range (len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k

            if prefix_mod in mod_seen:
                if i - mod_seen [prefix_mod] > 1:
                    return True
            
            else:
                mod_seen [prefix_mod] = i
        return False
