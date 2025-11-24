def solution(people, limit):
    answer = 0
    
    """
    - 한 번에 최대 2명 탑승
    - 무게제한 limit
    
    [매개변수]
    people : 몸무게를 담은 배열 : [70, 50, 80, 50]
    limit : 무게 제한
    
    return : 모든 사람을 구할 수 있는 구명보트의 '최솟값'
    """
    
    n = len(people)  #사람의 수
    survive = 0 # 구출 완료한 사람의 수
    
    people.sort(reverse = False) # 오름차순으로 정렬 [50, 50, 70, 80]
    
    front = 0              
    rear = len(people) - 1
    
    
    while survive != n and front <= rear: # 모든 사람이 구출될 때까지 반복
            
            front_value = people[front]
            rear_value = people[rear]
            
            if front_value + rear_value > limit: # 두명을 태울 수 없다 -> 가장 무거운 사람 태워 보내기
                survive += 1 # 가장 무거운 사람 구출
                rear -= 1 # rear인덱스 하나 당기기
                answer += 1
            
            
            else: # 가장 가벼운사람, 무거운사람을 함께 태워서 내보내기 
                
                survive += 2
                front += 1
                rear -= 1
                answer += 1         
                                     
                    # [50, 70, 80]
            
    
    return answer

