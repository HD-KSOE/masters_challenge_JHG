def solution(ingredient):
    answer = 0
    stack = []
    
    for i in ingredient: # O(n)
        stack.append(i) # O(1)
        if stack[-4:] == [1,2,3,1] : answer += 1; del stack[-4:] # O(1)
    
    return answer