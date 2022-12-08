# Part 1
with open('day 8 input.txt') as file:
    forest = [row.replace('\n', '') for row in file.readlines()]

n = len(forest)
count = 4*n - 4

for i in range(1, n-1):
    for j in range(1, n-1):
        height = int(forest[i][j])
        vis = []
        taller = 0
        # up
        for k in range(i):
            if int(forest[k][j]) >= height:
                taller += 1
        vis.append(taller)
        taller = 0
        # down
        for k in range(i+1, n):
            if int(forest[k][j]) >= height:
                taller += 1
        vis.append(taller)
        taller = 0
        # left
        for k in range(j):
            if int(forest[i][k]) >= height:
                taller += 1
        vis.append(taller)
        taller = 0
        # right
        for k in range(j+1, n):
            if int(forest[i][k]) >= height:
                taller += 1
        vis.append(taller)

        if 0 in vis:
            count += 1


print(count)
# 1703 trees

# Part 2
scenic_score = 0

for i in range(1, n-1):
    for j in range(1, n-1):
        height = int(forest[i][j])
        vis = []
        visible = 0
        # up
        for k in range(i-1, -1, -1):
            visible += 1
            if int(forest[k][j]) < height:
                continue
            else:
                break
        vis.append(visible)
        visible = 0
        # down
        for k in range(i+1, n):
            visible += 1
            if int(forest[k][j]) < height:
                continue
            else:
                break
        vis.append(visible)
        visible = 0
        # left
        for k in range(j-1, -1, -1):
            visible += 1
            if int(forest[i][k]) < height:
                continue
            else:
                break
        vis.append(visible)
        visible = 0
        # right
        for k in range(j+1, n):
            visible += 1
            if int(forest[i][k]) < height:
                continue
            else:
                break
        vis.append(visible)

        score = 1
        for val in vis:
            score *= val

        scenic_score = max(scenic_score, score)

print(scenic_score)
