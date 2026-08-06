class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()      # Stores unique characters in the current window
        left = 0            # Left pointer
        max_length = 0      # Stores the maximum length found

        for right in range(len(s)):   # Right pointer moves through the string

            # If duplicate is found, shrink the window
            while s[right] in window:
                window.remove(s[left])
                left += 1

            # Add the current character to the window
            window.add(s[right])

            # Update the maximum length
            max_length = max(max_length, right - left + 1)

        return max_length