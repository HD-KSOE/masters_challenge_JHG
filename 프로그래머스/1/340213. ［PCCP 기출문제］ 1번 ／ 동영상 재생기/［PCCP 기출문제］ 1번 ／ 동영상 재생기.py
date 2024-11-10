def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    n = len(commands)


    for i in range(n):
        #오프닝 위치 체크  
        if pos >= op_start and pos <= op_end:
            pos = op_end
            print(i,pos)
        if commands[i] == "prev":
            pos = cal_time(pos,-10)
            if pos < "00:00":
                pos = "00:00"
            print(i,pos)
        elif commands[i] == "next":
            pos = cal_time(pos,10)
            if pos > video_len:
                pos = video_len
            print(i,pos) 
            
        #오프닝 위치 체크  
        if pos >= op_start and pos <= op_end:
            pos = op_end
            print(i,pos)    
    return pos

def cal_time(pos,obj):
    s_min = pos[0]+pos[1]
    s_sec = str(int(pos[3]+pos[4]) + obj)
    print('s_sec=',s_sec)
    print('s_min=',s_min)
    if int(s_sec) >= 60:
        s_sec = str(int(s_sec) - 60)
        s_min = str(int(s_min) + 1)
    elif int(s_sec) < 0 and int(s_min) > 0:
        s_sec = str( 60 + int(s_sec))
        s_min = str(int(s_min) - 1)
    elif int(s_sec) < 0 and int(s_min) <= 0:
        s_sec = "00"
        s_min = "00"
    
    if len(s_min) < 2:
        s_min = s_min.zfill(2)

    if len(s_sec) < 2:
        s_sec = s_sec.zfill(2)

    print(s_min + ':' + s_sec)
    return s_min + ':' + s_sec
