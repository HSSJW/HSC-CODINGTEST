"""
1. 선물을 주고받은 기록을 바탕으로 다음 달에 누가 선물을 많이 받을지 예측


<규칙>
1. 이번 달 까지 누적이 더 많은 사람이 다음 달에 하나 받는다.
2. 동률이면 선물 지수가 더 큰 사람이 하나 받는다.
    - 선물 지수 = 준 선물 - 받은 선물

3. 선물 지수도 같다면 다음 달에 변화가 없다.


<목적>
- 다음 달에 가장 많은 선물을 받는 친구가 받을 선물의 개수
- [A B] : A가 B에게 선물을 준다.


<접근>
1. 종류의 개수 -> Counter?
2. I가 나머지 들과 주고받은 선물 상태를 종류별로 기록해야한다. -> defaultdict

<관리>
1. 선물 지수
2. A와 B 사이의 주고받은 선물 개수
"""

from collections import Counter, defaultdict

def solution(friends, gifts):
    answer = [0 for _ in range(len(friends))]
    
    dic = defaultdict(Counter)
    
    p_score = defaultdict(int)
    
    for i, name in enumerate(friends):
        for j in range(i+1, len(friends)):
            dic[name][friends[j]] = 0
            dic[friends[j]][name] = 0
        
    
    # 두 사람이 선물 주고받은 기록 생성
    for gift in gifts:

        A, B = gift.split(" ") # A B로 분리

        dic[A][B] += 1 # 선물을 받은 쪽에만 더해주기
        
        # 선물 지수는 준 사람한테는 더해주고 받은 사람한테는 빼준다.
        p_score[A] += 1
        p_score[B] -= 1     
    
        # print(f'gift = {gift}, p_score[A] - 1 = {p_score[A]} / p_score[B] + 1 = {p_score[B]}')
    
    # A가 다음날 몇개 받는지를 기록해야한다. -> dic를 돌아서 0보다 큰 values의 개수 + 0인 것 중에서 선물 지수(p_score)를 비교해서 자기가 더 큰 것의 개수
    # 이름을 순회하면서 dic[이름]인 Counter를 하나씩 순회하면서 value를 검사해야한다.
    
    # print(dic)
    # print(p_score)
    for i, name in enumerate(friends):
        
        for B_name, value in dic[name].items():
            
            
            if  value > dic[B_name][name]: # A가 준 선물이 더 많으면
                # print(f' A : {name} B : {B_name}')
                # print(f'{value} > {dic[B_name][name]}')
                answer[i] += 1
                
            elif value == dic[B_name][name]:  # 주고 받은 선물이 동률이면 선물 지수를 검사한다.
                # print('선물지수')
                if p_score[name] > p_score[B_name]: # 더 큰 사람이 하나 받기
                    
                    answer[i] += 1
                
                else:
                    pass
                
            else: # A가 B한테 받은 선물이 더 많으면
                pass
           
        # print(answer)
    
    
    return max(answer)