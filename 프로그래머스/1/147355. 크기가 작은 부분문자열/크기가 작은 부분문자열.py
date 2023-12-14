def solution(t, p):
    cnt = len(p)
    answer = 0
    for i in range(len(t)-cnt+1):
        for j in range(cnt):
            print(t[i+j],p[j])
            if t[i+j] > p[j]:
                break
                
            elif t[i+j] < p[j]:
                print("break",t[i+j],p[j])
                answer += 1
                break
            elif t[i+j] == p[j] and j == cnt -1:
                answer += 1

    return answer