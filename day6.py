# Part 1
with open('day 6 input.txt', 'r') as file:
    s = file.read().strip()

for i in range(len(s)-3):
    if len(set([s[i], s[i+1], s[i+2], s[i+3]])) == 4:
        print(
            f'Start of packet marker begins at index {i}, detected after character {i+4}')
        break
# answer = 1042

# Part 2
for i in range(len(s)-13):
    unique = 0
    for j in range(i, i+14):
        if s[i:i+14].count(s[j]) == 1:
            unique += 1
        else:
            break
    if unique == 14:
        print(
            f'Start of message marker begins at index {i}, detected after character {i+14}')
        break
# 2980
