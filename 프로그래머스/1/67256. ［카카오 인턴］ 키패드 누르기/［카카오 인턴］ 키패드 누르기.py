def solution(numbers, hand):
    answer = ''
    left = [4,3,2,1]
    right = [4,3,2,1]
    n = len(numbers)
    for i in range(n):
        if numbers[i] == 1:
            left = [1,2,3,4]
            answer += 'L'
        elif numbers[i] == 4:
            left = [2,1,2,3]
            answer += 'L'
        elif numbers[i] == 7:
            left = [3,2,1,2]
            answer += 'L'
        elif numbers[i] == 3:
            right = [1,2,3,4]
            answer += 'R'
        elif numbers[i] == 6:
            right = [2,1,2,3]
            answer += 'R'
        elif numbers[i] == 9:
            right = [3,2,1,2]
            answer += 'R'
        else:
            if numbers[i] == 2:
                if left[0] < right[0]:
                    answer += 'L'
                    left = [0,1,2,3]
                elif left[0] > right[0]:
                    answer += 'R'
                    right = [0,1,2,3]
                else:
                    if hand == "right":
                        answer += 'R'
                        right = [0,1,2,3]
                    else:
                        answer += 'L'
                        left = [0,1,2,3]          
            elif numbers[i] == 5:
                if left[1] < right[1]:
                    answer += 'L'
                    left = [1,0,1,2]
                elif left[1] > right[1]:
                    answer += 'R'
                    right = [1,0,1,2]
                else:
                    if hand == "right":
                        answer += 'R'
                        right = [1,0,1,2]
                    else:
                        answer += 'L' 
                        left = [1,0,1,2]
            elif numbers[i] == 8:
                if left[2] < right[2]:
                    answer += 'L'
                    left = [2,1,0,1]
                elif left[2] > right[2]:
                    answer += 'R'
                    right = [2,1,0,1]
                else:
                    if hand == "right":
                        answer += 'R'
                        right = [2,1,0,1]
                    else:
                        answer += 'L'
                        left = [2,1,0,1]
            elif numbers[i] == 0:
                if left[3] < right[3]:
                    answer += 'L'
                    left = [3,2,1,0]
                elif left[3] > right[3]:
                    answer += 'R'
                    right = [3,2,1,0]
                else:
                    if hand == "right":
                        answer += 'R'
                        right = [3,2,1,0]
                    else:
                        answer += 'L'    
                        left = [3,2,1,0]
    return answer