import re

with open('day 7 input.txt') as file:
    data = file.read().strip().splitlines()

system = {'1root': {'files': []}}
depth = {1: '1root'}
level, cur_dir = 1, '1root'
current = system['1root']

dir_sizes = {'1root': 0}

for line in data:
    if line[2:4] == 'ls' or line[:3] == 'dir':
        continue
    if line[0] == '$':
        if line[2:4] == 'cd':
            if line[5] == '/':
                # go to root directory
                current = system['1root']
                cur_dir, level = '1root', 1
            elif line[5:7] == '..':
                # go up 1 directory
                current = system
                for i in range(1, level):
                    current = current[depth[i]]
                level -= 1
                cur_dir = depth[level]
            else:
                # go to this directory
                level += 1
                cur_dir += str(level) + line[5:]
                depth[level] = cur_dir
                if cur_dir not in dir_sizes:
                    dir_sizes[cur_dir] = 0
                if cur_dir in current:
                    current = current[cur_dir]
                else:
                    current[cur_dir] = {'files': []}
                    current = current[cur_dir]
    else:
        # add file to current dir if not present
        size, filename = int(line.split()[0]), line.split()[1]
        if (size, filename) not in current['files']:
            current['files'].append((size, filename))
            for i in range(1, level+1):
                dir_sizes[depth[i]] += size

sum_sizes = 0

for dir in dir_sizes:
    if dir_sizes[dir] <= 100000:
        sum_sizes += dir_sizes[dir]

print(sum_sizes)
# answer = 1086293

# Part 2
unused = 70000000 - dir_sizes['1root']
need = 30000000 - unused

candidates = []

for dir, size in dir_sizes.items():
    if size >= need:
        candidates.append(size)

smallest_dir = min(candidates)

print(smallest_dir)
# 366028
