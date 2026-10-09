class Solution:
    def romanToInt(self, s):
        # Map each Roman symbol to its integer value
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        
        for i in range(len(s)):
            # If the current symbol is smaller than the next one, subtract it
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            # Otherwise, add it to the total
            else:
                total += roman_map[s[i]]
                
        return total