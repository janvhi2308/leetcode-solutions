class Solution:
    def singleNumber(self, nums: list[int]) -> int:
      ones=0
      twos=0
      for num in nums:
        new_ones= (ones^num) & ~twos
        new_twos= (twos^num) & ~new_ones
        ones, twos= new_ones, new_twos
      return ones 