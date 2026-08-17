"""
<힌트>
- 사진이 대놓고 트리구조 -> 그래프?
- 

<조건>
- 발생 이익 10% -> 추천인 (직접 부모 노드)에게 전달.
- 발생 이익 = 판매 이익 + 자식 노드 발생이익의 10%

- 분배하는 이익을 계산할 때에는 0.1을 곱해주고 소수점 첫째자리에서 버림
- 10% 계산했을 때 1원 미만이면 배분하지 않는다.

enroll : 판매원 이름
referral[i] : enroll[i]를 소개한 사람 이름 => enroll[i]의 부모 노드
seller[i] / amount[i] : amount[i]는 seller[i]가 판매한 개수
칫솔 1개 : 100원

<목표>
- 판매원에게 배분된 이익금의 총합을 계산하여(정수형으로)
- enroll 순서대로 리스트로 반환


<접근>
- 그래프를 역방향으로 타고 올라가야한다. -> 단방향으로 만들면 된다. (자식 -> 부모 방향)

<그래프 연결 방법>
1. 부모 노드부터 -> referral[i]가 '-'인 경우 center 노드에 연결
2. graph 딕셔너리에 key 순서대로 referral에서 일치하는 이름을 연결
3. enroll 개수와 딕셔너리 key개수가 같아질 때 까지 반복
"""

from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = []
    
    graph = defaultdict(list)
    money_sum = defaultdict(int) # 특정 노드의 누적 수익 
    
    
    for en in enroll:
        money_sum[en] = 0
    
    # 자식 -> 부모 방향 단방향 그래프 생성
    for i, ref in enumerate(referral):
        
        if ref == '-': # 깊이 1 그래프 연결
            graph[enroll[i]].append('center') # 자식 -> 부모

    
        else:
            graph[enroll[i]].append(ref) # enroll이 ref의 소개로 들어왔다.

    
    # 그래프를 타고 올라가면서 더해주는 함수
    def cal(se, am):
        
        if se == 'center':
            return
        

        divide = am // 10 # 10% == 1/10로 줄인다 == 10으로 나눈다.
        
        
        if divide < 1: # 분배하지 않는다
            money_sum[se] += am
            
        else: # 10% 분배 진행
            money_sum[se] += am - divide # 90%를 내가 갖고
            
            cal(graph[se][0], divide)  # 10%는 부모 노드로 올려보내기
        
        
        
            
            
    # 판매 한 사람 볼 때 마다 그래프 타고 올라가면서 더해주기
    for se, am in zip(seller, amount):
        
        cal(se, am * 100)
        
    
    
    
    return list(money_sum.values())





