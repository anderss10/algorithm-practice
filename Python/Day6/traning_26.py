# 마지막 두 원소

def solution(num_list):
    answer = []

    l_num = num_list[-1]
    p_num = num_list[-2]

    if l_num > p_num:
        num_list.append(l_num - p_num)
    else:
        num_list.append(l_num * 2)

    answer = num_list

    return answer