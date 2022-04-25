import sys

input_ = sys.stdin.readline

t = int(input_())

def get_longest_straight(dices):
    longest = 0
    for dice in dices:
        if dice > longest:
            longest += 1
    return longest

for i in range(t):
    n = int(input_())
    dices = sorted(map(int, input_().split()))
    print(f'Case #{i+1}:', get_longest_straight(dices))
