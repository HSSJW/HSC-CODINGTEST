"""
<힌트>
- 관련있는 기사 묶기
- 자카드 유사도 J(A, B)
    - `교집합의 크기` / `합집합의 크기`
    
<조건>
- J(A, B) = `교집합의 크기` / `합집합의 크기`
- A, B 모두 공집합 -> 유사도 1


- 중복 원소가 포함된 다중집합
- 다중집합의 특정 원소의 교집합 -> min
-                     합집합 -> max

- 두 글자씩 끊어서 다중집합을 만든다.
- 특수문자가 들어있는 경우는 그 글자 쌍을 버린다./ 대소문자 구분 안한다 -> 모두 대문자

"""
from collections import Counter

def solution(str1, str2):
    answer = 0
    
    
    # 대소문자 차이 무시 -> 모두 대문자로 전환
    str1 = str1.upper() 
    str2 = str2.upper()
    
    
    # 두글자씩 끊기, 종류의 개수이므로 Counter
    
    counter1 = Counter()
    counter2 = Counter()
    
    for i in range(0, len(str1)-1):
        
        if str1[i:i+2].isalpha():
            counter1[str1[i:i+2]] += 1
        
    for i in range(0, len(str2)-1):
        if str2[i:i+2].isalpha():
            counter2[str2[i:i+2]] += 1
    
    union = counter1 | counter2 # 합집합
    inter = counter1 & counter2 # 교집합
    
    # print(f'counter1 = {counter1}')
    # print(f'counter2 = {counter2}')
    # print(f'union = {union} len(union) = {len(union)}')
    # print(f'inter = {inter} len(inter) = {len(inter)}')
    # 교집 / 합집
    
    if len(union) == 0:
        return 65536
    else:
        answer = int(sum(inter.values()) / sum(union.values()) * 65536)
    
    
    return answer




