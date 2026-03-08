# 원소들의 곱과 합

def solution(num_list):
    answer = 0

    sum_val = sum(num_list)
    prod_val = 1
    for n in num_list:
        prod_val *= n

    answer = 1 if prod_val < sum_val ** 2 else 0

    return answer