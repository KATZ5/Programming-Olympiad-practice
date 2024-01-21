no_of_towers = input()
heights = input().split()
can_communicate = 0
for l in heights:
    if int(l) - int(heights[heights.index(l)+1]) < 10:
        can_communicate += 1
print(can_communicate)