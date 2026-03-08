#두 수의 연산값 비교하기

def solution(a, b):
    answer = 0

    r1 = int(str(a) + str(b))
    r2 = 2 * a * b

    answer = max(r1, r2)

    return answer