# Part 1
with open('day 5 input.txt') as file:
    data = file.read().strip().split('\n')

stacks = {}

i = 0

while data[i][0] == '[':
    line = data[i]
    s = 1
    while 4*s - 3 < len(line):
        crate = line[4*s - 3]
        if crate != ' ':
            if s in stacks:
                stacks[s] += [crate]
            else:
                stacks[s] = [crate]
        s += 1
    i += 1

for j in range(1, len(stacks)+1):
    stacks[j] = list(reversed(stacks[j]))

start = i + 2
stacks2 = dict(stacks)

for k in range(start, len(data)):
    step = data[k].split(' ')
    move, fromm, to = int(step[1]), int(step[3]), int(step[5])
    for _ in range(move):
        stacks[to].append(stacks[fromm].pop())

result = ''

for l in range(1, len(stacks)+1):
    result += stacks[l][-1]

print(result)
# FWNSHLDNZ

# Part 2
for k in range(start, len(data)):
    step = data[k].split(' ')
    move, fromm, to = int(step[1]), int(step[3]), int(step[5])
    temp = []
    for _ in range(move):
        temp.append(stacks2[fromm].pop())

    for _ in range(move):
        stacks2[to].append(temp.pop())

result2 = ''

for l in range(1, len(stacks2)+1):
    result2 += stacks2[l][-1]

print(result2)
# RNRGDNFQG
