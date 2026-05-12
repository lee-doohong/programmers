from collections import deque

def solution(m, n, h, w, drops):
    INF = float('inf')
    map_desert = [[INF]*n for _ in range(m)]
    map_fastest = []
    map_fastest2 = []
    
    for i in range(1, len(drops) + 1) :
        x, y = drops[i - 1]             
        map_desert[x][y] = i

    latest_p = None
    latest_t = 0

    def window_slide(arr, width) :
        dq = deque()
        result = []
        
        for i in range(len(arr)) :
            while dq and arr[dq[-1]] > arr[i] :
                dq.pop()

            dq.append(i)

            if dq[0] <= i - width :
                dq.popleft()
            
            if (i >= width - 1) :
                result.append(arr[dq[0]])

        return(result)

    for i in map_desert :
        map_fastest.append(window_slide(i, w))

    for i in range(len(map_fastest[0])) :
        map_fastest2.append(window_slide([row[i] for row in map_fastest], h))
    
    final_map_fastest = list(zip(*map_fastest2))

    for i in range(len(final_map_fastest)) :
        for j in range(len(final_map_fastest[i])) :
            if final_map_fastest[i][j] == 0 :
                return[i, j]
            else :
                if latest_t < final_map_fastest[i][j] :
                    latest_t = final_map_fastest[i][j]
                    latest_p = [i, j]
                
    return latest_p 

if __name__ == "__main__" :
    print(solution(3,3,1,1,[[0, 0], [0, 1], [0, 2], [1, 0]]))