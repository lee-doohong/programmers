from collections import deque

# 4,5,2,2,[[0, 0], [3, 1], [1, 3], [2, 4], [1, 1], [2, 2], [2, 3], [0, 4]]
# 3,3,1,1,[[0, 0], [0, 1], [0, 2], [1, 0]]

def solution(m, n, h, w, drops):
    INF = float('inf')
    # 최초 맵 생성
    map_desert = [[INF]*n for _ in range(m)]
    map_fastest = []
    map_fastest2 = []
    
    # 떨어지는 순서대로 입력한다
    for i in range(1, len(drops) + 1) :
        x, y = drops[i - 1]             
        map_desert[x][y] = i

#    map 디버깅
    print("first map")
    for i in map_desert :
        print(i)

    latest_p = None
    latest_t = 0

    # 가장 빠른시간 뱉는다
    def window_slide(arr, width) :
        dq = deque()
        result = []
        
        for i in range(len(arr)) :
            while dq and arr[dq[-1]] > arr[i] :
                dq.pop()

            dq.append(i)

            #dq[0]가 윈도우 밖이면 지워버려야 됨
            if dq[0] <= i - width :
                dq.popleft()
            
            if (i >= width - 1) :
                result.append(arr[dq[0]])

        return(result)

    for i in map_desert :
        map_fastest.append(window_slide(i, w))

    print("map_fastest")
    for r in map_fastest :
        print(r)

    for i in range(len(map_fastest[0])) :
        # 지금 이게 열 순으로 바껴 있는거아닌가..?
        map_fastest2.append(window_slide([row[i] for row in map_fastest], h))
    
    final_map_fastest = list(zip(*map_fastest2))
    print("final_map_fastest")
    for r in final_map_fastest :
        print(r)

    for i in range(len(final_map_fastest)) :
        for j in range(len(final_map_fastest[i])) :
            if final_map_fastest[i][j] == 0 :
                return[i, j]
            else :
                if latest_t < final_map_fastest[i][j] :
                    latest_p = [i, j]
                
    # print(f"latest_t : {latest_t}")
    return latest_p 

if __name__ == "__main__" :
    print(solution(4,5,2,2,[[0, 0], [3, 1], [1, 3], [2, 4], [1, 1], [2, 2], [2, 3], [0, 4]]))