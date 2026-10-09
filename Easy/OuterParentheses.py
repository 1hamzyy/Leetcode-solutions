class Solution(object):
    def removeOuterParentheses(self, s):
        ans = ""
        balance = 0

        for ch in s:
            if ch == '(':
                if balance > 0:
                    ans += ch
                balance += 1

            else:
                balance -= 1
                if balance > 0:
                    ans += ch

        return ans