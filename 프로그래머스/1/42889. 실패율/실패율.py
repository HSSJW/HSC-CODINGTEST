"""
<힌트>
- 동적으로 '게임 시간'을 늘려서 난이도 조절한다.

<조건>
- 실패율 : 스테이지에 도달 and 클리어 못한 사람 수 / 스테이지에 도달한 사람 수
    - i번 스테이지에 도달한 사람 수  = stages를 순회하면서 i보다 높으면 추가한다.
    - i번 스테이지에 도달했는데 클리어 못한 사람 수 = stages에서 값이 i인 개수
- N : 스테이지 개수   
- stages : 게임을 이용하는 사용자가 현재 멈춰있는 스테이지 번호
    - N+1인 사용자는 이미 모두 클리어한 사용자

<목표>
- 실패율이 높은 스테이지의 번호를 내림차순으로 return

<접근>
- 클리어 했다/못했다 -> DP?

100,000,000 -> 2중 반복문 불가능

1. stages에서 종류를 뽑은다음
2. 종류들만 순회하면서 stages에 각각 몇명 있는지 -> 도달했는데 클리어 못한 사람 수
3. counter로 스테이지별 사람 수 생성
    - 2테이지까지 간 사람 수 -> 1스테이지도 도달한 사람 수
        - Counter에서 하나씩 올라가면서 count[N]에 더해주기

"""

from collections import Counter

def solution(N, stages):
    answer = [(0, 0)] # 사용 안되는 0번 인덱스 추가
    
    # 0번 인덱스는 버린다. / (N+1) : 모두 클리어 까지 순회
    arrive = [0] * (N+2) # i번 스테이지에 도달한 사람 수
    stay = [0] * (N+2) # i번 스테이지에 아직 클리어하지 못한 사람 수
    
    counter = Counter(stages) # [스테이지 번호] = 인원 수
    
    for i in range(N+2): # 500
        stay[i] = counter[i]
        
        # 500
        for j in range(i+1): # 0스테이지 ~ i 스테이지 까지 도달한 사람 더해주기
            arrive[j] += counter[i]
        
    for i in range(1, N+1): # 완주자가 있는 N+1은 제외
        if arrive[i] == 0: # 도달한 사람이 없다.
            
            answer.append((i, 0))
        else:
            answer.append((i, stay[i] / arrive[i])) # 실패율
            
    
    answer.pop(0) # 0번 인덱스 제거
    answer.sort(key = lambda x: (-x[1], x[0]))
    result = []
    for ans in answer:
        result.append(ans[0])
    
    
    return result