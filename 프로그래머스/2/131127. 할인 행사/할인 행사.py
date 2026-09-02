"""
<힌트>
- 일정 금액 이상 지불 -> 10일동안 회원 자격
- 매일 회원대상 한 가지 제품 할인행사
    - 할인 제품은 하루에 하나만 구매 가능

- 원하는 제품과 수량이 할인하는 날짜와 '10일 연속' 일치하도록 회원가입

- a~b 기간동안 할인하는 종류가 원하는 종류, 개수가 같아야함
    -> 종류, 개수 동시에 고려 -> Counter
    
<목표>
- 조건을 만족하는 날짜의 수

<접근>
- want를 Counter로
- 특정 구간을 슬라이스 해서 Counter

- 두가지가 같으면 만족

- 원하는 물건의 개수가 10개보다 적을 수도 있다.
    -> d_counter[key] >= w_counter[key] 이면 통과

"""

from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    w_counter = Counter()
    
    for w, n in zip(want, number):
        w_counter[w] = n
    
    for i in range(len(discount)):
        flag = True
        
        slicing = discount[i:i+10] # i일부터 10일간을 뽑기
        d_counter = Counter(slicing) # Counter로 변환
        
        # counter는 없는걸 조회해도 0 리턴
        
        
        for w in want:

            if w_counter[w] > d_counter[w]: # 이 기간에는 실패다
                flag = False
                break
        
        if flag: # 이 구간 성공
            answer += 1

    
    return answer



