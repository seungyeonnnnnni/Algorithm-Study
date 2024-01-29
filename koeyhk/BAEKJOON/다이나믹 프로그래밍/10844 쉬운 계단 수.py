# 0 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 - 2 (1, 1)
# 0 1 1 1 2 2 2  7 7 7 7 8 8 8 9 9 - 3 (1, 2)
# 0 0 0 1 1 1 1 8 8 8 8 8 8 9 9 9 - 6 (3, 3)
# 0 0 0 0 9 9 9 9 9 9 - 10

# 잘못 생각한 부분
# 한 번에 묶어서 전체의 규칙을 찾으려 함!
# -> 이 문제는 0~9의 개수 각각으로 나눠서 생각했어야 함

N = int(input())
dp = [[1]*10 for _ in range(N+1)]
dp[1][0] = 0
for i in range(2, N+1):
    dp[i][0] = dp[i-1][1]
    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    dp[i][9] = dp[i-1][8]
print(sum(dp[N])%1000000000)
