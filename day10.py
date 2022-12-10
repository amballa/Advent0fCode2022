# Part 1

data = [x.strip('\n') for x in open('day 10 input.txt').readlines()]

X = {0: 1, 1: 1}
cycle = 1
val = 1

for i in range(len(data)):
    if data[i] == 'noop':
        cycle += 1
        X[cycle] = val
    else:
        e = int(data[i][5:])
        cycle += 1
        X[cycle] = val
        cycle += 1
        val += e
        X[cycle] = val

cycle = 20
signals = {}
while cycle <= 220:
    signals[cycle] = cycle * X[cycle]
    cycle += 40

print(sum(signals.values()))
# 12880

# Part 2

image = ''

for i in range(1, len(X)):
    cycle_pos = i % 40
    sprite = [X[i]-1, X[i], X[i]+1]
    pos = cycle_pos - 1
    if pos in sprite:
        image += '#'
    else:
        image += '.'

    if cycle_pos % 40 == 0:
        image += '\n'

print(image)
# FCJAPJRE
