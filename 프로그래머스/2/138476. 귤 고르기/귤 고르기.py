from collections import Counter

def solution(k, tangerine):
    answer = 0
    target = 0
    
    counter = Counter(tangerine)
    
    counter_list = counter.most_common() # 개수가 많은 순서대로 내림차순
    
    for fruit in counter_list:
        
        target += fruit[1] # 현재 과일의 개수 더하기
        answer += 1
        
        if target >= k:
            break
    
    return answer