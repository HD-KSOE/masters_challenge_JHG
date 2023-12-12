def solution(s, skip, index):
    result = []
    dic_alp = dict()
    alp = "abcdefghijklmnopqrstuvwxyz"
    idx = 0
    for i in alp: 
        if i not in skip:
            dic_alp[idx] = i
            idx +=1
    print(dic_alp) 
    alp_dic = {v:k for k,v in dic_alp.items()}
    for s_each in s:
        chk = alp_dic[s_each] + index
        chk = chk % (26-len(skip))
        
        result.append(dic_alp[chk]) 
    str_result = ''.join(result)
    return str_result