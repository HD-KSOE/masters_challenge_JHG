def solution(s):
    answer = ''
    arr_list = s.split()
    
    max_v = int(arr_list[0])
    min_v = int(arr_list[0])
    for list_each in arr_list:
        if max_v < int(list_each):
            max_v = int(list_each)
        if min_v > int(list_each):
            min_v = int(list_each)
        answer = str(min_v)+" "+str(max_v)
    return answer