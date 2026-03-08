# 수열과 구간 쿼리 3

def solution(arr, queries):
    answer = []

    for i,j in queries:
        arr[i], arr[j] = arr[j], arr[i]
    answer = arr

    return answer