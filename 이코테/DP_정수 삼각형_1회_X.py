from sys import stdin


stdin = open("text/DP_정수 삼각형.txt")

size = int(stdin.readline())

dp = []

max_value = 0

for s in range(0, size):
    array = list(map(int, (stdin.readline().split())))
    dp.append(array)

# 0, 0 -> 1, 0, 1, 1
for i in range(1, size):
    for j in range(i + 1):
        # print(i, j)
        up_left = 0 if j == 0 else dp[i - 1][j - 1]
        up = 0 if j == i else dp[i - 1][j]

        dp[i][j] = dp[i][j] + max(up_left, up)

# dp[i][j] = array[i][j] + max(dp[i - 1][j], dp[i - 1][j - 1])
print(max(dp[size - 1]))
