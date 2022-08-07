from sys import stdin


stdin = open("text/DP_금광.txt")

t = int(stdin.readline())

print(t)


for x in range(t):
    x, y = map(int, (stdin.readline().split()))

    array = list(map(int, stdin.readline().split()))

    print(x, y)
    print(array)
