# Part 1
with open('day 1 input.txt') as input:
    lines = input.readlines()

elves = []
calories = 0

for item in lines:
    if item.strip():
        calories += int(item)
    else:
        elves.append(calories)
        calories = 0

sol1 = max(elves)
# solution 1 = 70,720 calories

# Part 2
elves = sorted(elves, reverse=True)
sol2 = elves[0] + elves[1] + elves[2]
# solution 2 = 207,148 calories

if __name__ == "__main__":
    print(sol1, sol2)
