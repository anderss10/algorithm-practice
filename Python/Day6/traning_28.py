# 수 조작하기 2

def solution(numLog):
    answer = ''
    c = {1:'w', -1:'s', 10:'d', -10:'a'}

    for idx,val in enumerate(numLog):
        if idx == 0: continue

        diff = val - numLog[idx-1]
        answer += c[diff]

    return answer