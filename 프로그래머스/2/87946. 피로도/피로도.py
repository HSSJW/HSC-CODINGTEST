from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    """
    [시작전 요구 필요도, 끝날후 사용될 피로도]
    dungeons의 가로(열) 길이는 2 입니다.
    dungeons의 각 행은 각 던전의 ["최소 필요 피로도", "소모 피로도"] 입니다.
    "최소 필요 피로도"는 항상 "소모 피로도"보다 크거나 같습니다. -> 최소피로도 <= 소모 피로도
    "최소 필요 피로도"와 "소모 피로도"는 1 이상 1,000 이하인 자연수입니다. -> 
    서로 다른 던전의 ["최소 필요 피로도", "소모 피로도"]가 서로 같을 수 있습니다. -> 중복가능하다
    
    1. 현재 피로도 >= 최소 필요 피로도인가?
     1.1 True -> 현재 피로도 -= 소모 피로도
     1.2 False -> 다음 순회로
     
    모든 경우의수에 대한 결과를 리스트에 저장하고 max() -> 8개의 조합이니까 괜찮음
    """
    
    every_comb = list(permutations(dungeons)) # 모든 순서에 대한 경우를 가진 리스트
    
    answer_list = []
    
    for comb in every_comb:
        count = 0 # 현재 조합에 대한 탐험한 던전의 수
        k_save = k
        
        for dungeon in comb:  # 특정 조합에 대한 결과 탐색
            
            if k_save >= dungeon[0]: # 탐험 가능
                k_save -= dungeon[1]
                count += 1
            
        if answer < count:  # 이전까지 찾은 조합보다 더 많은 던전을 탐험한 경우을 찾으면
            answer = count
    
    
    return answer