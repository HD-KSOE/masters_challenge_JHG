
def solution(mats, park):

    answer = -1
    mats = sorted(mats)
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "-1": 
                answer = chkMats(mats,park,i,j,answer)
                
    return answer

def chkMats(mats,park,i,j,answer):
    for mat in mats:
        if  (i+mat > len(park) or j+mat > len(park[i])):
            print("범위밖",i,j,mat)
            break
        else:
            print("여기",i,j,mat)
            for a in range(mat):
                for b in range(mat):
                    if park[i+a][j+b] != "-1":
                        print("-1아님",i+a,j+b)
                        return answer
            if answer < mat:
                answer = mat
                print("성공",i+a,j+b,answer)
    return answer                
               
                
                