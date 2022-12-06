# Part 1

with open('day 4 input.txt') as file:
    data = [i for i in file.read().strip().split('\n')]

count = 0
count2 = 0

for pair in data:
    pair = pair.split(',')
    elf1, elf2 = [int(num) for num in pair[0].split('-')], [int(num)
                                                            for num in pair[1].split('-')]
    minn, maxx = min(elf1+elf2), max(elf1 + elf2)

    if (elf1[0] == minn and elf1[1] == maxx) or (elf2[0] == minn and elf2[1] == maxx):
        count += 1

    s1, s2 = set(range(elf1[0], elf1[1]+1)), set(range(elf2[0], elf2[1]+1))

    if s1 & s2:
        count2 += 1

print(count)
# 448

# Part 2

print(count2)
# 794
