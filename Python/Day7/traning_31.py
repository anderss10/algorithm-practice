# 수열과 구간 쿼리 4

def solution(arr, queries):
    answer = []

    # 2중 반복문 및 분기문 사용
    for s,e,k in queries:
        for i, v in enumerate(arr):
            if i >= s and i <= e and i%k == 0:
                arr[i] += 1

    answer = arr
    return answer