from cmath import pi
from sys import stdin

# n, c = map(int, (stdin.readline().split()))

# array = [int(stdin.readline()) for x in range(n)]

n, c = 5, 3

array = [1, 2, 4, 8, 9]


array.sort()

result = 0


min_gap = 1
max_gap = array[-1] - array[0]


while min_gap <= max_gap:

    middle_gap = (max_gap + min_gap) // 2
    count = 1
    pivot = array[0]

    for d in range(1, n):
        if array[d] >= middle_gap + pivot:
            pivot = array[d]
            count += 1

    if count >= c:
        min_gap = middle_gap + 1
        result = middle_gap
    else:
        max_gap = middle_gap - 1


print(result)
