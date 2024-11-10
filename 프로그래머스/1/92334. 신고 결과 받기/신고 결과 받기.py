def solution(id_list, report, k): 
    n = len(report)
    z = len(id_list)
    answer = [0 for i in range(z)]
    chk = [[0 for i in range(z)] for j in range(z)] 
    result = [0 for i in range(z)]
    
    id = dict()
    for i in range(z):
        id[id_list[i]] = i 

    for i in range(n):
        bug=report[i].split(' ')

        sender = id[bug[0]]
        trol = id[bug[1]]
            
        if chk[sender][trol] == 0:
            chk[sender][trol] = 1
            result[trol] += 1
            
    for i in range(len(result)):
        if result[i] >= k:
            for j in range(len(result)):
                if chk[j][i] == 1:
                    answer[j] += 1
    return answer