import sys

input_ = sys.stdin.readline

t = int(input_())

def get_ascii_art(r, c):
    punched_line_top = '..+'+'-+'*(c-1)
    punched_line_bottom = '..|'+'.|'*(c-1)
    normal_line_top = '+-+'+'-+'*(c-1)
    normal_line_bottom = '|.|'+'.|'*(c-1)

    ascii_art = [punched_line_top, punched_line_bottom]+[normal_line_top, normal_line_bottom]*(r-1)+[normal_line_top]
    return ascii_art

for i in range(t):
    print(f'Case #{i+1}:')
    print('\n'.join(get_ascii_art(*map(int, input_().split()))))
