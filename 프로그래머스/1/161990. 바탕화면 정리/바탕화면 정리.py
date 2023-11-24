def solution(wallpaper):
    answer = []
    rd = [0,0]
    lu = [len(wallpaper), len(wallpaper[0])]
    
    for i in range(len(wallpaper)) : 
        for j in range(len(wallpaper[i])) :
            if wallpaper[i][j] == '#':
                if i > rd[0] :
                    rd[0] = i
                if j > rd[1]:
                    rd[1] = j
                if i < lu[0]:
                    lu[0] = i
                if j < lu[1]:
                    lu[1] = j
            print(i,j)
            print(lu[0],lu[1],rd[0],rd[1])
    
    answer.append(lu[0])
    answer.append(lu[1])
    answer.append(rd[0]+1)
    answer.append(rd[1]+1)

    return answer