def solution(number):
    answer = 0
    for i in range(len(number)-1):
        for j in range(i+1,len(number)):
            f_num=-(number[i]+number[j])            
            for k in range(j+1,len(number)):
                if number[k] == f_num:
                    answer +=1
            print(number[i],number[j],f_num,answer)        
                    
    return answer