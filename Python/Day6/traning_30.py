# 수열과 구간 쿼리 2

def solution(arr, queries):
    answer = []

    for s,e,k in queries:
        # 조건(lamda식)에 맞는 요소 filter 후(iterator 타입) list 변환
        new_arr = list(filter(lambda x: x>k, arr[s:e+1]))

        # list에서 최소값 구하기, 비어있으면 -1 return
        min_val = min(new_arr, default=-1)
        answer.append(min_val)

    return answer


