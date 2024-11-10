def solution(survey, choices):
    answer = ''
    n = len(survey)
    d_sur = dict()
    d_sur = {'R':0 , 'T':1 , 'C':2 , 'F':3 , 'J':4 , 'M':5 , 'A':6 , 'N':7}
    r_sur = dict()
    r_sur = {0:'R' , 1:'T' , 2:'C' , 3:'F' , 4:'J' , 5:'M' , 6:'A' , 7:'N'}
    score = [0 for i in range(8)]

    for i in range(n):  
        if choices[i] < 4:
            score[d_sur[survey[i][0]]] += abs(choices[i]-4)    
        elif choices[i] > 4:
            score[d_sur[survey[i][1]]] += choices[i]-4
            
    for i in range(0,7,2):
        if score[i] >= score[i+1]:
            answer += r_sur[i]
        elif score[i] < score[i+1]:
            answer += r_sur[i+1]
        

    return answer