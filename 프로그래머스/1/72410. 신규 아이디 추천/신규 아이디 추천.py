
import re

def solution(new_id):
    answer = ''
    n = len(new_id)
    #1단계 소문자
    new_id = new_id.lower() 
    #2단계 문자 제거
    new_id = re.sub(r'[^a-z0-9._-]','',new_id)
    #3단계
    new_id = re.sub(r'\.{2,}','.',new_id)
    #4단계
    new_id = re.sub(r'^\.','',new_id)
    new_id = re.sub(r'\.$','',new_id)
    #5단계
    if len(new_id) == 0:
        new_id = 'a'
    #6단계
    if len(new_id) >= 16:
        new_id = new_id[0:15]
    new_id = re.sub(r'\.$','',new_id)
    #7단계
    if len(new_id) <= 2:
        while len(new_id) < 3:
            print(new_id)
            new_id = new_id + (new_id[-1])
    return new_id