from collections import deque

def solution(bandage, health, attacks):
    answer = 0
    
    """
    [키워드]
    - t초 -> 시뮬레이션?
    
    
    [조건]
    - 붕대감기 -> 1. t초동안 1초마다 x 회복 2. t == 연속 수행시간일 때 (추가회복 + 초당 회복)만큼 추가회복
    - 최대체력 제한있음
    
    - 공격당하면 중단 (공격당하는 초에도 회복 안됨)
    - 공격당하면 체력 감소 -> 0보다 낮아지면 사망
    
    
    [매개변수 및 리턴]
    bandage = [시전 시간, 초당 회복량, 추가 회복량]
    health(int) = 최대체력
    attacks[i] = [공격 시각, 피해량] - 시간기준 오름차순 정렬
    
    return : 남은체력 (죽었다면 -1)
    """
    
    queue = deque(attacks)
    time = 0
    squence_time = 0
    max_health = health

    while queue: # 공격이 모두 끝날 때 까지
        
        squence_time += 1
        
        if queue[0][0] == time: # 공격시간
            attack = queue.popleft() # 공격 실행
            health -= attack[1] #  체력 감소
            squence_time = 0 # 연속 수행시간 초기화
        
        elif squence_time == bandage[0]: # 회복시간 충족
            
            health += bandage[2] + bandage[1] # 추가회복
            squence_time = 0
        
        else: #1초 흐름
            health += bandage[1]  # 초당회복량 회복
            
        
        if health <= 0:
            answer = -1
            return answer
        elif health > max_health:
            health = max_health
        
        time += 1
        
    answer = health
    
    
    return answer