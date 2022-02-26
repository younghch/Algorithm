'''
https://www.acmicpc.net/problem/1992
'''
import sys

input_ = sys.stdin.readline

n =  int(input_())
square = [list(input_().rstrip()) for _ in range(n)]

def compressible(x, y, l):
    cur = square[x][y]
    for i in range(x, x+l):
        for j in range(y, y+l):
            if cur != square[i][j]:
                return ''
    return cur

def get_quard_tree(x, y, l):
    l = l//2
    xs = (x, x+l)
    ys = (y, y+l)
    ans = []

    for n_x in xs:
        for n_y in ys:
            result = compressible(n_x, n_y, l)
            if not result:
                ans.append(get_quard_tree(n_x, n_y, l))
            else:
                ans.append(result)

    if ans[0] in ('0', '1') and len(set(ans)) == 1:
        return ans[0]
    return f"({''.join(ans)})"

print(get_quard_tree(0, 0, n))
