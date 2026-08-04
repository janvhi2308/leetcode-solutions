class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length= len(strs[0])
        for i in range(1,len(strs)):
          if len(strs[i])<min_length:
             min_length= len(strs[i])

        ans=""
        for i in range(min_length):
            for j in range(1,len(strs)):
                if strs[0][i]!=strs[j][i]:
                    return ans
            ans+=strs[0][i]    
        return ans                    