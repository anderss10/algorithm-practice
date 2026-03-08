# 코드 처리하기

def solution(code):
    answer = ''
    mode = 0

    for idx in range(len(code)):
        if mode == 0:
            if code[idx] == "1":
                mode = 1
            else:
                answer += code[idx] if idx % 2 == 0 else ""
        else:
            if code[idx] == "1":
                mode = 0
            else:
                answer += code[idx] if idx % 2 == 1 else ""

    if answer == "": return "EMPTY"

    return answer