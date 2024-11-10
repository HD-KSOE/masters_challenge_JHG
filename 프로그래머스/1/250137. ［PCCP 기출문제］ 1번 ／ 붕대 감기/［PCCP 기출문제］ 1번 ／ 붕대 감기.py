def solution(bandage, health, attacks):
    answer = 0
    t = attacks[len(attacks)-1][0] + 1
    a_chk = 0
    h_time = 0
    c_heal = health
    
    for i in range(t):
        if attacks[a_chk][0] == i:
            c_heal -= attacks[a_chk][1]
            if c_heal <= 0:
                answer = -1
                return answer
            h_time = 0
            a_chk += 1
        else:
            h_time += 1
            if health != c_heal:
                c_heal += bandage[1]
                if h_time == bandage[0]:
                    c_heal += bandage[2]
                    h_time = 0
                if c_heal > health:
                    c_heal = health
                    
        answer = c_heal

    return answer