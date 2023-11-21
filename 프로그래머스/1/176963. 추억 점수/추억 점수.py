def solution(name, yearning, photo):
    answer = []
    dict_name = {name[i] : yearning[i] for i in range(len(name))}
    for i in range(len(photo)):
        cnt = 0
        for j in range(len(photo[i])):
            print(i,j)
            if photo[i][j] in name:
                cnt += dict_name[photo[i][j]]
        answer.append(cnt) 
    return answer