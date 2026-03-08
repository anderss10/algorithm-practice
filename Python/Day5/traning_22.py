# 등차수열의 특정한 항만 더하기

def solution(a, d, included):
    answer = 0

    numbers = [i for i in range(a, a + len(included) * d, d)]

    for num, bl in zip(numbers, included):
        answer += num if bl else 0

    return answer