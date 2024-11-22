def solution(X, Y):
    answer = ''

    x=[0 for _ in range(10)]
    y=[0 for _ in range(10)]

    for i in range(max(len(X),len(Y))):
        if len(X) > i :
            x[int(X[i])] += 1
        if len(Y) > i :
            y[int(Y[i])] += 1
            
    for j in range(10):
        answer += str(j)*min(x[j],y[j])
    
    if answer == '':
        return '-1'
    
    elif answer != '' and answer.count('0') == len(answer):
        return '0'

    return ''.join(sorted(answer,reverse=True)) 

