"""
<힌트>

<의사 코드>
1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화 -> 딕셔너리에 모든 알파벳 초기화
반복 ---
2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다
    - 1글자 존재 -> 2글자 검사 -> 3글자 검사
3. w에 해당하는 사전의 '색인 번호'를 출력하고 입력에서 w를 제거한다.
4. 입력에서 처리되지 않은 다음 글자 c가 남아있다면
    - w+c에 해당하는 단어를 사전에 등록한다.  ('KA'를 다음 번호로 등록한다.)
---



"""

def solution(msg):
    answer = []
    n = len(msg)+1 # 최초 msg의 마지막 글자 인덱스
    
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    dic = dict()
    # (1번 과정) 길이가 1인 모든 단어 초기화
    for i, al in enumerate(alpha):
        dic[i+1] = al # dic[색인번호] = 글자 / 색인번호 기준으로 정렬되어있다.
    
    values_set = set(dic.values()) # 값이 추가될 때마다 여기에 단어를 add
    # print(values_set)
    

    front = 0
    i = 1
    w = msg[front:i] #  처음엔 한글자 슬라이싱
    while i < len(msg)+1:

        #같은 인덱스가 매칭된다.
        keys= (dic.keys()) # 색인번호 keys[0] => 딕셔너리 dic[1]
        values = list(dic.values()) # 단어 
        
        
        
        while True:
            
            
            # 가장 긴 검색되는 글자 찾기 (front ~ i)
            if w in values_set and i != n: # 검색 성공이고 뒤에 글자 남음 -> 더 긴글자 시도
                i += 1 #한글자 더
                w = msg[front:i]
            
            else: # 한글자 더 했는데 검색 실패 -> 한글자 줄이고
                if i == n:
                    pass
                else:
                    i -= 1
                w = msg[front:i]
                break
                    
        answer.append(values.index(w) + 1) # 색인 번호 출력
            
            
        if i != n: # (4번 과정) 처리되지 않은 글자가 남아 있다면
            wc = msg[front:i+1]
            dic[len(values) + 2] = wc # 사전에 wc 등록
            values_set.add(wc)    # 딕셔너리의 글자 목록에 추가
            print(f'w에 해당하는 {w}를 {values.index(w) + 1}을 사전에 추가하고 {wc}를 색인번호 {len(values) + 1}로 추가')



        front = i #이제 wc 다음 글자부터 진행
        i = front + 1
            
    
    return answer


