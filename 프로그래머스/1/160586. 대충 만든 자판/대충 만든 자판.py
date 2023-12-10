def solution(keymap, targets):
    dic_key = dict()
    result = [0 for _ in range(len(targets))]
    for keymap_arr in keymap:     
        for j,keymap_each in enumerate(keymap_arr):
            if keymap_each in dic_key:
                if dic_key[keymap_each] > j+1:
                    dic_key[keymap_each] = j+1
            else:
                dic_key[keymap_each] = j+1
    
    for i in range(len(targets)):
        for k in range(len(targets[i])):
            if targets[i][k] not in dic_key:
                result[i] = -1
                break
            else:
                result[i] +=dic_key[targets[i][k]]
    
    return result