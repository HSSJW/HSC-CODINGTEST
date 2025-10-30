from collections import Counter

def solution(clothes):
    answer = 1
    
    """
    <조건>
    - 종류별로 하나만 착용
    - 착용한 것이 하나라도 바뀌거나 추가로 입으면 새로운 착장
    - 최소한 한개는 입어야함
    
    face / headgear / eyewear
    
    (a 카테고리 옷 개수 + 1) * b (b 카테고리 옷 개수 + 1) *.... -1(모두 안입는 경우는 없다)
    
    <리턴>
    옷 조합의 수 -> itertools?
    """
    
    cloth_type = [c[1] for c in clothes]  # 옷의 종류만 저장하는 리스트 생성
    
    counter = Counter(cloth_type) # {'headgear':2, 'face':1} 이런식으로 저장
    
    for item in list(counter.items()):
        
        answer *= item[1] + 1 # (옷 개수 + 1)을 곱하기
    
    
    answer -= 1
        
        
    
    return answer