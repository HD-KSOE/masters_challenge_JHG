def solution(cards1, cards2, goal):
    chk_1 = 0 
    chk_2 = 0
    for goal_each in goal:
        print(chk_1,chk_2,goal_each)
        if len(cards1) > chk_1 and cards1[chk_1] == goal_each:
            chk_1 += 1
            print(chk_1,chk_2,goal_each)
        elif len (cards2) > chk_2 and cards2[chk_2] == goal_each:
            chk_2 += 1
            print(chk_1,chk_2,goal_each)
        else:
            return "No"     
        print(chk_1,chk_2,goal_each)
    return "Yes"