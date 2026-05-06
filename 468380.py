from bisect import *

# arr	l	r	result
# [3, 2, 3, 1, 1],	5,	7

# [16952, 70276, 16771, 37992, 87549, 54906, 36718, 20478, 57088, 27916, 51509, 83422, 51707, 18807, 80859, 2673, 37734, 93380],149845,228204
# [2, 2, 2], 2, 2
# [8, 8, 6, 5, 2, 9, 8, 4, 3, 10], 25, 27
# [70195, 25471, 7389, 58187, 18454, 90532, 97667, 17148, 91636, 2810],	126058,	462933
# [49134, 86806, 94548, 88849, 95022, 28334, 16637, 79487, 23773, 7314, 47370, 50269, 36573, 9415, 44674, 28096],61242,88535

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

        if left_loc is right_loc :
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
    
    # print(f"arr : {arr}")
    # print(f"arr_sum : {arr_sum}")
    # print(f"find_loc : {l} = {bisect_left(arr_sum, l)}, {r} = {bisect_left(arr_sum, r)}")

    answer = [final_K, 1]
    return answer

if __name__ == "__main__" :
    print(solution([49134, 86806, 94548, 88849, 95022, 28334, 16637, 79487, 23773, 7314, 47370, 50269, 36573, 9415, 44674, 28096],61242,88535))