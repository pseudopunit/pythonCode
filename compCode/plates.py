t = int(input())
en = 1
while t:
    n, k, p = input().split()
    n = int(n)
    k = int(k)
    p = int(p)
    a = []
    for i in range(n):
        a.insert(i, [int(i) for i in input().split()])
    sumx = 0
    dp = [[0 for i in range(p + 1)] for i in range(n + 1)]
    prf = [[0 for i in range(k + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            prf[i][j] = prf[i][j - 1] + a[i - 1][j - 1]
    #print(prf)
    for i in range(1, n + 1):
        for j in range(1, p + 1):
            dp[i][j] = 0
            for x in range(min(j, k) + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j - x] + prf[i][x])

        sumx += max(sumx, dp[i][j])

    opt = 'Case #' + str(en) + ':'
    print(opt, dp[n][p])
    en += 1
    t -= 1
