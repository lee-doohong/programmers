# [[1, 2], [2, 3], [2, 1]],4,4
# [[1, 2], [2, 3], [2, 1]],1,7

def solution(info, n, m):
    INF = float('inf')
    #일단 dp배열 생성
    dp = [[INF] * (m + 1) for _ in range(len(info))]
    
    #dp초기화
    dp[0][0] = info[0][0]
    dp[0][info[0][1]] = 0

    target = []
    target.append(0)
    target.append(info[0][1])

    #dp알고리즘 돌리기, 일단 target에있는거 하나씩 꺼낸다.
    for i in range(1, len(info)) :
        nxt_target = []

        # A가 훔치는 경우, dp[][] 값 수정, 여기서는 최소값 비교가 의미가 없다. 
        for j in target :
            if dp[i - 1][j] + info[i][0] >= n :
                continue
            else : 
               dp[i][j] = dp[i - 1][j]  + info[i][0]
               nxt_target.append(j)

        # B가 훔치는 경우
        for j in target :
            if j + info[i][1] >= m :
                continue
            else : 
                dp[i][j + info[i][1]] = min(dp[i - 1][j], dp[i][j + info[i][1]])
                nxt_target.append(j)

        target = list(set(nxt_target))[:]


    #answer리턴
    answer = min(dp[len(info) - 1])

    if answer == INF :
        answer = -1

    for i in dp :
        print(i)
    
    return answer

if __name__ == "__main__" :
    print(solution([[1, 2], [2, 3], [2, 1]],1 ,7))