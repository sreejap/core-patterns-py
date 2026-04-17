# https://leetcode.com/problems/word-break/

# https://algo.monster/problems/word_break
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo : dict[int,bool] = {}

        def dfs (start):
            if start == len(s):
                return True
            
            if start in memo:
                return memo [start]
            
            ans = False
            for word in wordDict:
                if s[start:].startswith (word):
                    if dfs (start + len(word)):
                        ans = True
                        break
            
            memo [start] = ans
            
            return ans
        return dfs (0)
