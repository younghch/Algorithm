from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = []
        if len(s) > 12 or len(s) < 4:
            return answer
        for i in range(1,4):
            for j in range(1,4):
                for k in range(1,4):
                    try:
                        a1 = s[:i]
                        a2 = s[i:i+j]
                        a3 = s[i+j:i+j+k]
                        a4 = s[i+j+k:]
                        if  check_valid(a1) and \
                            check_valid(a2) and \
                            check_valid(a3) and \
                            check_valid(a4):
                            answer.append(f'{a1}.{a2}.{a3}.{a4}')
                    except IndexError:
                        break
        return answer

def check_valid(s):
    if not s or (len(s) > 1 and s[0] == '0'):
        return False
    return 0 <= int(s) < 256

solution = Solution()
assert solution.restoreIpAddresses('25525511135') == ["255.255.11.135","255.255.111.35"]

        