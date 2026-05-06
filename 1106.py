from math import gcd
from functools import reduce

# test_case : [[2, 1, 2], [5, 1, 1]]
# answer : 13

def solution(signal) :
    # signal_arr = list(map(lambda x : list(map(int, x.split(', '))), [i for i in signal.strip()[2:-2].split('], [')]))
    signal_arr = signal   
    signal_arr_sum = []
    #lcm 도출
    for i in signal_arr :
        signal_arr_sum.append(sum(i))
    
    # print(f"signal_arr_sum = {signal_arr_sum}")

    def get_lcm(a, b) :
        return int(a*b/gcd(a, b))

    signal_lcm = reduce(get_lcm, signal_arr_sum)

    # print(f"signal_lcm = {signal_lcm}")

    for t in range(1, signal_lcm + 1) :
        flag = True
        for traffic_light in signal_arr : #여기서 만약 틀리면 flag를 false로 변경, 아니면 flag를 그대로 둔다.
            before_y = traffic_light[0]
            y_time = traffic_light[1]
            circle = sum(traffic_light)
            # print(f"t : {t}, before_y = {before_y}, y_time = {y_time}, circle = {circle}")

            if t <= before_y :
                flag = False
                break
            else :
                if not(1 <= (t - before_y) % circle <= y_time) :
                    flag = False        
                    break

        if t == signal_lcm and not flag :
            return -1
        elif not flag :
            continue
        else : 
            return t

    

if __name__ == "__main__" :
    print(solution([[2, 1, 2], [5, 1, 1]]))