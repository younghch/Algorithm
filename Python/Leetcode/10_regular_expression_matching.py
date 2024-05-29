class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s, len_p = len(s), len(p)
        matched = [[False for _ in range(len_p+1)] for _ in range(len_s+1)]

        matched[0][0] = True
        for i in range(1, len_p+1):
            if p[i-1] == '*':
                matched[0][i] = matched[0][i-2]
        
        for i in range(1, len_s+1):
            for j in range(1, len_p + 1):
                if p[j-1] == '*':
                    matched[i][j] = matched[i][j-2]
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        matched[i][j] = matched[i][j] or matched[i-1][j]
                elif p[j-1] == '.' or p[j-1] == s[i-1]:
                    matched[i][j] = matched[i-1][j-1]
        
        return matched[len_s][len_p]



    
solution = Solution()

assert solution.isMatch('aaaaa', 'aa*a') == True
assert solution.isMatch('aa', 'a') == False
assert solution.isMatch('abc', 'a***abc') == True