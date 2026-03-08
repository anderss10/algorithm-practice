#flag에 따라 다른 값 반환하기

def solution(a, b, flag):
    answer = a+b if flag else a-b
    return answer