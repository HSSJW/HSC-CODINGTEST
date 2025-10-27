from itertools import permutations # permutations(대상, 몇개 씩 조합을 만들지)

def is_prime(n): # 소수인지 판별하는 함수
    
    if n < 2:  # 1인 경우 -> 1은 소수 아님
        return False
    
    for i in range(2, int(n**0.5) + 1): # int(n**1)는 소수점을 버리는 것이므로 +1 해준다
        if n % i == 0: # 나누어 떨어짐 -> 소수가 아니다
            return False

    return True # 소수이다


def solution(numbers):
    answer = 0
    """
    1. 숫자를 한글자씩 문자로 분리
    2. 각 조합을 만든다. -> 1, 2 어떤 게 먼저 오는지(12, 21)가 유의미 하므로 combinations가 아니라 permutations를 사용해야겠군 -> 📌다른 인덱스의 같은 값이 리스트는 다른 조합으로 사용되므로 미리 중복되는 숫자 제거해야겠군
        ✅ 리스트 중복 제거 방법 
        1️⃣ 순서 유지 x -> set로 변환했다가 다시 list로 list(set())
        2️⃣ 순서 유지 o -> list(dict.fromkeys(my_list))
    3. 조합이 저장된 데이터를 소수인지 검사 -> 검사하려면 정수형태 -> 변환해야겠군 -> 리스트의 문자열을 하나로 합치는 함수 ''.join(arr)을 사용해야겠군
    4. 소수이면 answer += 1
    """

    comb_list = [] # 모든 숫자 순서 조합 튜플을 저장할 리스트
    
    # 요소의 개수가 i개인 조합을 모두 만들어야한다
    for i in range(1, len(numbers)+1):
        
        perm = permutations(numbers, i) # 1개 2개 3개...를 사용한 조합
        comb_list.extend(perm) # 리스트 이어붙이기
        
    
    
    int_comb_list = [int(''.join(perm)) for perm in comb_list] # perm('1', '2', '3')을 분해해서 숫자로 저장
    
    int_comb_list = list(set(int_comb_list))
    
    for n in int_comb_list:
        
        
        if is_prime(n): # 소수가 맞으면
            answer += 1 # 카운트
        
    
    return answer