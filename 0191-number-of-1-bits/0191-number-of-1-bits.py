class Solution:
    def hammingWeight(self, n: int) -> int:
        ans= n^0
        count=0
        for i in range(0,32):
            if ans&(1<<i):
                count+=1
        return count        
        