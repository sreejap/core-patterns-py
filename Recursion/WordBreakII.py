# https://leetcode.com/problems/word-break-ii/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        word_set = set(wordDict) # look up in lists in o(n), set is o(1)
        def dfs (start,path):
            if start == len (s):
                ans.append (" ".join(path))
                return
            
            for end_index in range (start+1,len(s)+1):            
                word = s [start:end_index]

                if word in word_set:
                    path.append(word)
                    dfs (end_index,path)
                    path.pop()
        
        dfs (0,[]) # [] is path
        return ans
