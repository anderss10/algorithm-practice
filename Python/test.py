def solution(l, r):
    answer = []

    for i in range(l, r+1):
        if check(str(i)):
            answer.append(i)

    return answer if answer else [-1]

def check(char):
    result = False

    for c in char:
        if c == '0' or c == '5':
            result = True
        else:
            result = False
            break

    return result

print(solution(5, 555))
print(solution(10, 20))