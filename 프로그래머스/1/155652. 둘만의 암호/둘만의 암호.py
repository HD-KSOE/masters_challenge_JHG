def solution(s, skip, index):
    result = []
    dic_alp = dict()
    alp = "abcdefghijklmnopqrstuwxyz"
    print(len(alp))
    """
    for i in range(len(alp)):
        if alp[i] in skip:
            i -= 1
        else:
            dic_alp[alp[i]] = i
            
    for s_each in s:
        result.append(dic_alp[s_each +  index])  
        
    return result