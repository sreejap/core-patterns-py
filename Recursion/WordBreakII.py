# https://leetcode.com/problems/word-break-ii/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        word_set = set(wordDict) # look up in lists in o(n), set is o(1)
        def dfs (start,path):
            if start == len (s):
                ans.append (" ".join(path))
                return
            
            for word in word_set:
                if s[start:].startswith(word):
                    path.append(word)
                    dfs (start+len(word),path)
                    path.pop()
        
        dfs (0,[]) # [] is path
        return ans
