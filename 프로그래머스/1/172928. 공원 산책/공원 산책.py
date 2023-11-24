def solution(park, routes):
    dd = {"N":0,"S":1,"W":2,"E":3}
    #park = ["OOO", "OSO", "OOO", "OOO"]
    #routes =  ["N 2", "S 2"]
    answer = []

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    bef_answer = []
    for k in range(len(park)):
        if 'S' in park[k]:
            answer = [k,park[k].index('S')]
            bef_answer = [k,park[k].index('S')]           
    for i in range(len(routes)):        
        bp = 0
        for j in range(int(routes[i][2])):
            if 0 <= answer[0] + dx[dd[routes[i][0]]] and  answer[0] + dx[dd[routes[i][0]]] < len(park) and 0 <= answer[1] + dy[dd[routes[i][0]]]  and answer[1] + dy[dd[routes[i][0]]] < len(park[0]) and park[answer[0] + dx[dd[routes[i][0]]]][answer[1] + dy[dd[routes[i][0]]]] != 'X' and bp < 1 :
                print("befor",i,j,answer)
                answer[0] += dx[dd[routes[i][0]]]
                answer[1] += dy[dd[routes[i][0]]]
                print("after",i,j,answer)
            else:               
                bp += 1                
        if bp > 0:
            answer[0],answer[1] = bef_answer[0],bef_answer[1]
        else:
            bef_answer[0],bef_answer[1] = answer[0],answer[1]
    return answer