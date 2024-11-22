import math

def solution(brown, yellow):
    answer = []
    i_sum = brown + yellow
    floor = 3
    stop = 0
    #if i_sum % 2 !=0:
       # answer = [int(math.sqrt(i_sum)),int(math.sqrt(i_sum))]                      
    #else : 
    while 1:
        if i_sum % floor == 0 and yellow == (floor-2) * ((i_sum // floor)-2):
            answer = [i_sum//floor,floor]
            break    
        else: 
            print(i_sum//floor,floor )
            floor += 1            
    return answer