# Part 1
with open('day 2 input.txt') as input:
    lines = input.readlines()

outcome = {('A', 'X'): 3+1, ('B', 'Y'): 3+2, ('C', 'Z'): 3+3,  # ties
           ('A', 'Y'): 6+2, ('B', 'Z'): 6+3, ('C', 'X'): 6+1,  # wins
           ('A', 'Z'): 0+3, ('B', 'X'): 0+1, ('C', 'Y'): 0+2}  # losses

total = 0

for line in lines:
    opp, me = line[0], line[2]
    score = outcome[(opp, me)]
    total += score

print(total)
# 12,156

# Part 2

outcome = {('A', 'Y'): 3+1, ('B', 'Y'): 3+2, ('C', 'Y'): 3+3,  # ties
           ('A', 'Z'): 6+2, ('B', 'Z'): 6+3, ('C', 'Z'): 6+1,  # wins
           ('A', 'X'): 0+3, ('B', 'X'): 0+1, ('C', 'X'): 0+2}  # losses

total2 = 0

for line in lines:
    opp, result = line[0], line[2]
    score = outcome[(opp, result)]
    total2 += score

print(total2)
# 10,835
