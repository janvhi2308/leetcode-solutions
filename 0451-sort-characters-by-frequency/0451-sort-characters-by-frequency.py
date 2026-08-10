class Solution:
    def frequencySort(self, s: str) -> str:
        count={}
        for char in s:
            count[char]= count.get(char,0)+1
            sorted_count= sorted(count.items(),key=lambda item:item[1],reverse=True)
            answer=""
        for char, frequency in sorted_count:
            answer+= char*frequency
        return answer        

        