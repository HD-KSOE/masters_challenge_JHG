def solution(board, moves):
    answer = 0
    boom = 0
    case = []
    for j in range(len(moves)):
        for i in range(len(board)):
            if board[i][moves[j]-1] != 0:
                case.append(board[i][moves[j]-1])
                board[i][moves[j]-1] = 0
                break
        if len(case) > 1:
            print(case[-1], case[-2])
            if case[-1] == case[-2]:
                answer += 2
                del case[-2]
                del case[-1]

    return answer
