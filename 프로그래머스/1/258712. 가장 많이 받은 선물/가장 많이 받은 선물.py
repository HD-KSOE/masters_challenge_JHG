def solution(friends, gifts):
    answer = 0
    dic_f = dict()
    history = []
    #실제 선물 개수
    score = [0 for _ in range(len(friends))]
    #딕셔너리 생성
    for i in range(len(friends)):
        dic_f[friends[i]] = i
    #상대 선물 지표    
    f_score = [[0 for _ in range(len(friends))]  for _ in range(len(friends))]
    #선물점수
    gift_score = [0 for _ in range(len(friends))]
    
    for gift in gifts:
        history = gift.split(' ')  
        print(dic_f[history[0]])
        sender = dic_f[history[0]]
        reciver = dic_f[history[1]]
        f_score[sender][reciver] += 1
        gift_score[sender] += 1
        gift_score[reciver] -= 1
    print(f_score)
    print(gift_score)
             
    
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i != j:
                if f_score[i][j] > f_score[j][i]:
                    score[i] += 1
                elif f_score[i][j] == f_score[j][i]:
                    if gift_score[i] > gift_score[j]:
                        score[i] += 1
    answer = max(score)                    
    return answer