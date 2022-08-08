from sys import stdin


stdin = open("text/DP_금광.txt")

t = int(stdin.readline())


dp = []


for z in range(t):
    n, m = map(int, (stdin.readline().split()))
    array = list(map(int, stdin.readline().split()))

    max_value = 0
    index = 0

    for k in range(n):
        dp.append(array[index : index + m])
        index = index + m

    for j in range(1, m):
        for i in range(n):
            left_up = 0 if i == 0 else dp[i - 1][j - 1]
            left_down = 0 if i == n - 1 else dp[i + 1][j - 1]
            left = dp[i][j - 1]

            dp[i][j] = dp[i][j] + max(left_down, left_up, left)

    result = 0

    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)
