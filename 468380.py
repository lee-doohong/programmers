from bisect import *

def solution(arr, l, r):
    
    arr_sum = []
    sum = 0
    
    for i in range(len(arr)) :
        sum += arr[i]
        arr_sum.append(sum)

    def find_sum(l_v, r_v) :
        K = 0
        left_loc = bisect_left(arr_sum, l_v)
        right_loc = bisect_left(arr_sum, r_v)

        if left_loc == right_loc :
            K = (r_v - l_v + 1) * arr[left_loc]

        else : 
            for i in range(left_loc, right_loc+1) :
                if i != left_loc and i != right_loc :
                    K += pow(arr[i], 2)
                
                if i == left_loc :
                    K += (arr_sum[i] - l_v + 1) * arr[i]

                if i == right_loc :
                    K += (r_v - arr_sum[i-1]) * arr[i]

        return K

    final_K = find_sum(l, r)
    final_C = 0
    left_p = 1
    right_p = r - l + 1
    first_v = find_sum(left_p, right_p)
    
    while(1) :
        if first_v == final_K :
            final_C += 1

        now_left = bisect_left(arr_sum, left_p) 
        now_right = bisect_left(arr_sum, right_p)

        left_gap = arr_sum[now_left] - left_p
        right_gap = arr_sum[now_right] - right_p

        min_gap = min(left_gap, right_gap)
        temp_gap = arr[now_right] - arr[now_left]

        if temp_gap == 0 and (first_v == final_K):
            final_C += min_gap

        else : 
            final_gap = final_K - first_v
            if (final_gap * temp_gap > 0) and (final_gap % temp_gap == 0) and final_gap / temp_gap <= min_gap :
                final_C += 1

        if (right_p + min_gap + 1 > arr_sum[-1]) :
            break
    
        left_p = left_p + min_gap + 1
        right_p = right_p + min_gap + 1

        first_v += min_gap * temp_gap 
        first_v += (arr[bisect_left(arr_sum, right_p)] - arr[bisect_left(arr_sum, left_p - 1)])
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    answer = [final_K, final_C]
    return answer

if __name__ == "__main__" :
    print(solution([3, 2, 3, 1, 1],	5,	7))