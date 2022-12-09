# Part 1
with open('day 9 input.txt') as input:
    data = input.read().strip('\n').splitlines()

head, tail = (0, 0), (0, 0)
visited = {(0, 0)}


def go_up(h, t):
    h = (h[0], h[1]+1)

    if abs(h[0]-t[0]) == 0 and abs(h[1]-t[1]) == 2:
        t = (h[0], h[1]-1)

    elif abs(h[0]-t[0]) == 1 and abs(h[1]-t[1]) == 2:
        t = (h[0], h[1]-1)

    return h, t


def go_down(h, t):
    h = (h[0], h[1]-1)

    if abs(h[0]-t[0]) == 0 and abs(h[1]-t[1]) == 2:
        t = (h[0], h[1]+1)

    elif abs(h[0]-t[0]) == 1 and abs(h[1]-t[1]) == 2:
        t = (h[0], h[1]+1)

    return h, t


def go_left(h, t):
    h = (h[0]-1, h[1])

    if abs(h[0]-t[0]) == 2 and abs(h[1]-t[1]) == 0:
        t = (h[0]+1, h[1])

    elif abs(h[0]-t[0]) == 2 and abs(h[1]-t[1]) == 1:
        t = (h[0]+1, h[1])

    return h, t


def go_right(h, t):
    h = (h[0]+1, h[1])

    if abs(h[0]-t[0]) == 2 and abs(h[1]-t[1]) == 0:
        t = (h[0]-1, h[1])

    elif abs(h[0]-t[0]) == 2 and abs(h[1]-t[1]) == 1:
        t = (h[0]-1, h[1])

    return h, t


for move in data:
    dir, num = move[0], move[2:]

    if dir == 'U':
        for i in range(int(num)):
            head, tail = go_up(head, tail)
            visited.add(tail)

    elif dir == 'D':
        for i in range(int(num)):
            head, tail = go_down(head, tail)
            visited.add(tail)

    elif dir == 'L':
        for i in range(int(num)):
            head, tail = go_left(head, tail)
            visited.add(tail)

    elif dir == 'R':
        for i in range(int(num)):
            head, tail = go_right(head, tail)
            visited.add(tail)

print(len(visited))
# 6044

# Part 2


def response(h, t):

    if abs(h[0]-t[0]) == 0 and h[1]-t[1] == 2:
        t = h[0], h[1]-1
    elif abs(h[0]-t[0]) == 0 and h[1]-t[1] == -2:
        t = h[0], h[1]+1

    elif h[0]-t[0] == 2 and abs(h[1]-t[1]) == 0:
        t = h[0]-1, h[1]
    elif h[0]-t[0] == -2 and abs(h[1]-t[1]) == 0:
        t = h[0]+1, h[1]

    elif h[0]-t[0] == 2 and h[1]-t[1] == 2:
        t = t[0]+1, t[1]+1
    elif h[0]-t[0] == -2 and h[1]-t[1] == 2:
        t = t[0]-1, t[1]+1
    elif h[0]-t[0] == 2 and h[1]-t[1] == -2:
        t = t[0]+1, t[1]-1
    elif h[0]-t[0] == -2 and h[1]-t[1] == -2:
        t = t[0]-1, t[1]-1

    elif abs(h[0]-t[0]) == 1 and h[1]-t[1] == 2:
        t = h[0], h[1]-1
    elif abs(h[0]-t[0]) == 1 and h[1]-t[1] == -2:
        t = h[0], h[1]+1

    elif h[0]-t[0] == 2 and abs(h[1]-t[1]) == 1:
        t = h[0]-1, h[1]
    elif h[0]-t[0] == -2 and abs(h[1]-t[1]) == 1:
        t = h[0]+1, h[1]

    return h, t


knots = [(0, 0)]*10
visited2 = {(0, 0)}

for move in data:
    dir, num = move[0], move[2:]

    if dir == 'U':
        for _ in range(int(num)):
            knots[0], knots[1] = go_up(knots[0], knots[1])
            for i in range(1, 9):
                knots[i], knots[i+1] = response(knots[i], knots[i+1])

            visited2.add(knots[-1])

    elif dir == 'D':
        for _ in range(int(num)):
            knots[0], knots[1] = go_down(knots[0], knots[1])
            for i in range(1, 9):
                knots[i], knots[i+1] = response(knots[i], knots[i+1])

            visited2.add(knots[-1])

    elif dir == 'L':
        for _ in range(int(num)):
            knots[0], knots[1] = go_left(knots[0], knots[1])
            for i in range(1, 9):
                knots[i], knots[i+1] = response(knots[i], knots[i+1])

            visited2.add(knots[-1])

    elif dir == 'R':
        for _ in range(int(num)):
            knots[0], knots[1] = go_right(knots[0], knots[1])
            for i in range(1, 9):
                knots[i], knots[i+1] = response(knots[i], knots[i+1])

            visited2.add(knots[-1])

print(len(visited2))
# 2384
