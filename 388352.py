from itertools import combinations 

def solution(n, q, ans):
    # combination의 재료가 될 것을 생성해야 한다.
    cnt = 0
    m = len(q)
    tmp_set_add = {}
    tmp_set_discard = {}
    for i in range(m) :
        if ans[i] == 0 :
            tmp_set_discard.update(q[i])
        else :
            tmp_set_add.update(q[i])

    # tmp_set_discard를 이용해서 확실하게 아닌것들 먼저 쳐내고
    for i in tmp_set_discard :
        q.remove(i)

    for i in set(combinations(q, 5)) :
        flag = True
        for j in range(m) :
            if q[j]&i == ans[j] :
                break
        if(flag) :
            cnt += 1

    # 그런데 tmp_set_add에 한번도 안들어갔다고 해서 무조건 아니라고 할 수 있나?

    answer = cnt
    return answer



if __name__ == "__main__" :
    print(solution(10, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3]))

    # 10, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3]