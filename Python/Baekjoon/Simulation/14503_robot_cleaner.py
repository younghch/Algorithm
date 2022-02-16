"""
https://www.acmicpc.net/problem/14503
"""
import sys


# initialize variable
north, east, south, west = 0, 1, 2, 3
dirty, wall, clean = 0, 1, 2
row, col = map(int, sys.stdin.readline().split())
x, y, direction = map(int, sys.stdin.readline().split())

# initialize map
room = []
for i in range(row):
    room.append(list(map(int, sys.stdin.readline().split())))

ans = 1

room[x][y] = clean
rot_count = 0

while True:
    if rot_count == 4:
        if x + 1 < row and direction == north:
            if room[x + 1][y] != wall:
                if room[x][y] != clean:
                    room[x][y] = clean
                    ans += 1
                x += 1
                rot_count = 0
            else:
                if room[x][y] != clean:
                    room[x][y] = clean
                    ans += 1
                break
        elif y + 1 < col and direction == west:
            if room[x][y + 1] != wall:
                if room[x][y] != clean:
                    room[x][y] = clean
                    ans += 1
                y += 1
                rot_count = 0
            else:
                if room[x][y] != clean:
                    room[x][y] = clean
                    ans += 1
                break
        elif x - 1 > -1 and direction == south:
            if room[x - 1][y] != wall:
                if room[x][y] != clean:
                    room[x][y] = clean
                    ans += 1
                x -= 1
                rot_count = 0
            else:
                if room[x][y] != clean:
                    room[x][y] = clean
                    ans += 1
                break
        elif y - 1 > -1 and direction == east:
            if room[x][y - 1] != wall:
                if room[x][y] != clean:
                    room[x][y] = clean
                    ans += 1
                y -= 1
                rot_count = 0
            else:
                if room[x][y] != clean:
                    room[x][y] = clean
                    ans += 1
                break
        else:
            if room[x][y] != clean:
                room[x][y] = clean
                ans += 1
            break

    # check direction and clean
    direction = (direction - 1) % 4
    if x-1 > -1 and direction == north:
        if room[x-1][y] == dirty:
            if room[x][y] != clean:
                room[x][y] = clean
                ans += 1
            x -= 1
            rot_count = 0
        else:
            rot_count += 1
    elif y-1 > -1 and direction == west:
        if room[x][y - 1] == dirty:
            if room[x][y] != clean:
                room[x][y] = clean
                ans += 1
            y -= 1
            rot_count = 0
        else:
            rot_count += 1
    elif x+1 < row and direction == south:
        if room[x+1][y] == dirty:
            if room[x][y] != clean:
                room[x][y] = clean
                ans += 1
            x += 1
            rot_count = 0
        else:
            rot_count += 1
    elif y+1 < col and direction == east:
        if room[x][y+1] == dirty:
            if room[x][y] != clean:
                room[x][y] = clean
                ans += 1
            y += 1
            rot_count = 0
        else:
            rot_count += 1
print(ans)
