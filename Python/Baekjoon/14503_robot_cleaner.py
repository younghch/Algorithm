"""
로봇 청소기가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

로봇 청소기가 있는 장소는 N×M 크기의 직사각형으로 나타낼 수 있으며, 1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북중 하나이다. 지도의 각 칸은 (r, c)로 나타낼 수 있고, r은 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로 부터 떨어진 칸의 개수이다.

로봇 청소기는 다음과 같이 작동한다.

1. 현재 위치를 청소한다.
2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
    a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    d. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.
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


def ft_print(room):
    for row in room:
        print(row)
    print()


while True:

    # if all clean or wall
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
            # ft_print(room)
        else:
            rot_count += 1
    elif y-1 > -1 and direction == west:
        if room[x][y - 1] == dirty:
            if room[x][y] != clean:
                room[x][y] = clean
                ans += 1
            y -= 1
            rot_count = 0
            # ft_print(room)
        else:
            rot_count += 1
    elif x+1 < row and direction == south:
        if room[x+1][y] == dirty:
            if room[x][y] != clean:
                room[x][y] = clean
                ans += 1
            x += 1
            rot_count = 0
            # ft_print(room)
        else:
            rot_count += 1
    elif y+1 < col and direction == east:
        if room[x][y+1] == dirty:
            if room[x][y] != clean:
                room[x][y] = clean
                ans += 1
            y += 1
            rot_count = 0
            # ft_print(room)
        else:
            rot_count += 1
print(ans)
