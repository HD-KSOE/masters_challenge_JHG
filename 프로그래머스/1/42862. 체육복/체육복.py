def solution(n, lost, reserve):

    lost.sort()
    reserve.sort()
    answer = n-len(lost)
    chk_los = [0 for _ in range(len(lost))]
    chk_res = [0 for _ in range(len(reserve))]
    for k in range(len(lost)):
        for i in range(len(reserve)):
            if reserve[i] == lost[k]:
                chk_los[k] = 1
                chk_res[i] = 1
                answer += 1

    for z in range(len(lost)):
        if chk_los[z] == 0:
            for j in range(len(reserve)):
                if chk_res[j] == 0 and (lost[z]-1 == reserve[j] or lost[z] +1 == reserve[j]):
                    chk_res[j] = 1
                    answer += 1
                    break

    return answer