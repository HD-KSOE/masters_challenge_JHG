def solution(n, m, section):
    answer = 1
    case = section[0]
    for i in range(1,len(section)):
        if section[i] > case+m-1:
            answer += 1
            case = section[i]
    return answer