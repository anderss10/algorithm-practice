#문자열 겹쳐쓰기

def solution(my_string, overwrite_string, s):
    answer = my_string

    l = len(overwrite_string)

    answer_first = my_string[:s]
    answer_last = my_string[s+l:]

    answer = answer_first + overwrite_string + answer_last

    return answer