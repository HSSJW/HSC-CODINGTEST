"""
<힌트>
- 근무 태도, 동료 평가
- 두 점수가 모두 다른 사원보다 낮은 경우가 '한 번이라도' -> 완전탐색
    -> 인센 못받음
- 인센 받는 사원들을 (근태, 동평) 높은 순으로 차등 지급
    - 동일하면 동석차
    - 그다음은 건너뜀


<조건>
- [0]이 완호의 점수

<목표>
- 완호의 석차 구하기

<접근>
- 등수 세우기 -> 초기 데이터 순서 무의미하다 + 각 원소들 대소비교 -> 정렬 해버리자 -> 단방향 패턴 분석
- 찾아야 하는 특이 조건이 a, b모두 다른 것들보다 작은 경우 -> '작은' 것이 특이점이므로 큰쪽부터 검사
    -> [4,3][4,3][3,3][2,5][1,4]
    -> a, b둘다 이전보다 작은 경우를 검사한다.
    -> a를 기준으로 정렬해버렸으므로 이제 b에 대해서만 고려하면된다.

"""

from collections import Counter

def solution(scores):
    answer = 0
    
    if len(scores) == 1:
        return 1
    
    whan = scores[0] # 완호 점수 기록
    whan_s = scores[0][0] + scores[0][1]
    line = [] # 합격자들 점수 기록
    
    scores.sort(key=lambda x: (-x[0], x[1])) # 동점자 처리 -> 0번 인덱스는 내림차순, 2번은 오름
    
    
    
    # a, b가 모두 a_max, b_max보다 작은 경우를 찾아서 pop
    a_max = 0
    b_max = 0
    
    for i, score in enumerate(scores.copy()):
        a, b = score
        
        if a_max > a and b_max > b: # 과락
            

            
            if whan == score: # 완호가 과락
                print('완호 과락')
                return -1
            pass
        else: # 합격
            line.append(a+b) # 인센 대상자에 점수 합 추가
            
        
        if a_max < a:
            a_max = a
        if b_max < b:
            b_max = b
    line.sort(reverse = True)

    
    counter = Counter(line) # 점수별 명수
    
    for s, p in counter.items():
        if s > whan_s:
            answer += p
    
    
    
    return answer+1 #