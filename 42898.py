def solution(m, n, puddles) :
    dp = [[0] * m for _ in range(n)]
    
    for x, y in puddles :
        dp[y - 1][x - 1] = -1
    # 초기화
    dp[0][0] = 1

    # 왔던 방향으로만 <- 문제 해결
    # def dps(a, b) :
    #     # 동서남북
    #     direction = {'R' : [0, 1], 'D' : [-1, 0]}
        
    #     for d in direction :
    #         if dp(a, b) + 1 < a + d[0] 

    for i in range(n) :
        for j in range(m) :
            if dp[i][j] == -1 or (i == 0 and j == 0) : continue

            north_v = dp[i - 1][j] if i - 1 >= 0 and dp[i - 1][j] != -1  else 0
            west_v = dp[i][j - 1] if j - 1 >= 0 and dp[i][j - 1] != -1 else 0
            dp[i][j] = (north_v + west_v) % 1_000_000_007
            
            #디버깅
            # print(f"dp[{i}][{j}] = {dp[i][j]}, north_v = {north_v}, west_v = {west_v}")

    # print(dp)
    return dp[n-1][m-1]

if __name__ == "__main__" :
    print(solution(4, 3, [[2, 2]]))