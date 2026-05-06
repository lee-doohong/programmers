from bisect import *

# arr	l	r	result
# [3, 2, 3, 1, 1],	5,	7

# [16952, 70276, 16771, 37992, 87549, 54906, 36718, 20478, 57088, 27916, 51509, 83422, 51707, 18807, 80859, 2673, 37734, 93380],149845,228204
# [2, 2, 2], 2, 2
# [8, 8, 6, 5, 2, 9, 8, 4, 3, 10], 25, 27
# [70195, 25471, 7389, 58187, 18454, 90532, 97667, 17148, 91636, 2810,	126058,	462933
# [49134, 86806, 94548, 88849, 95022, 28334, 16637, 79487, 23773, 7314, 47370, 50269, 36573, 9415, 44674, 28096],61242,88535

def solution(arr, l, r):
    
    arr_sum = []
    sum = 0
    
    # bisect는 해당하는 값을 뱉는게 아니라 위치를 뱉는 것임
    # arr은 0부터 시작한다
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
            # 여기서 i는 left_loc에서 right_loc까지 가는 동안임...
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

        # print(f"first_v : {first_v} / left_p : {left_p} / right_p : {right_p} / final_K : {final_K} / final_C : {final_C}")

        now_left = bisect_left(arr_sum, left_p) 
        now_right = bisect_left(arr_sum, right_p)

        # print(f"now_left : {now_left} / now_right : {now_right}")

        left_gap = arr_sum[now_left] - left_p
        right_gap = arr_sum[now_right] - right_p

        min_gap = min(left_gap, right_gap)
        temp_gap = arr[now_right] - arr[now_left]

        #left_p와 right_p가 가르키는 값이 같다면
        if temp_gap == 0 and (first_v == final_K):
            final_C += min_gap

        # print(f"min_gap : {min_gap}")
        #left_p와 right_p가 가르키는 값이 다르다면 한번 겹치는 값이 있는지 없는지만 확인해주면 된다
        else : 
            # 같은 방향인 경우에만
            final_gap = final_K - first_v
            if (final_gap * temp_gap > 0) and (final_gap % temp_gap == 0) and final_gap / temp_gap <= min_gap :
                final_C += 1
            # for _ in range(min_gap) :
            #     first_v += arr[now_right] - arr[now_left]
            #     if first_v == final_K :
            #         final_C += 1
            #         break

        #탈출조건을 하나 만들어줘야 함.
        if (right_p + min_gap + 1 > arr_sum[-1]) :
            break
    
        left_p = left_p + min_gap + 1
        right_p = right_p + min_gap + 1

        # first_v += min_gap * temp_gap 
        # first_v += arr[right_p + min_gap + 1]
        # first_v -= arr[left_p + min_gap]  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    print(f"arr : {arr}")
    print(f"arr_sum : {arr_sum}")
    print(f"find_loc : {l} = {bisect_left(arr_sum, l)}, {r} = {bisect_left(arr_sum, r)}")

    answer = [final_K, final_C]
    return answer

if __name__ == "__main__" :
    print(solution([3, 2, 3, 1, 1],	5,	7))