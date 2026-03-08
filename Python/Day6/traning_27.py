# 수 조작하기 1

def solution(n, control):
    answer = n

    new_control = {'w' : 1, 's' : -1, 'd' : 10, 'a' : -10}

    for t in control :
        answer += new_control[t]

    return answer