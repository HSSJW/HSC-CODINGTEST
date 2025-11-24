def solution(n, lost, reserve):
    answer = 0
    
    """
    [조건]
    - 학생수 2~30 -> 3중 for문 가능
    - 여벌옷이 있는 학생만 빌려줄 수 있음
    
    [매개변수]
    학생들의 번호 : 체격순서 -> 순서가 정렬되어있음
    n : 학생수
    lost : 도난당한 학생들의 번호 배열 (오름차순 정렬되어있음어있음)
    reserve : 여벌옷이 있는 학생들의 번호
    
    return : 여벌옷 학생들이 앞뒤로 체육복을 빌려줘서 체육수업을 들을 수 있는 최대 학생 수
    """
    lost.sort()
    reserve.sort()
    
    student = [i+1 for i in range(n)]  #[1, 2, 3, 4, 5]
    
    
    #[x for x in list_a if x in list_b]
    
    temp = [x for x in reserve if x in lost]  #공통원소
    
    lost = [x for x in lost if x not in temp]
    reserve = [x for x in reserve if x not in temp]
    
    
    temp_lost = [lo for lo in lost]
    
    for lost_n in temp_lost:
        
        front_student = lost_n - 1
        rear_student = lost_n + 1
        
        if lost_n == 1: # 맨앞 학생이 잃어버림 -> i-1학생한테는 못빌림
            if reserve.count(rear_student) != 0: # 뒤에 학생이 여벌 옷이 있다면
                reserve.remove(rear_student) # 해당 학생의 여벌옷 제거
                lost.remove(lost_n)
                
        elif lost_n == n: # 잃어버린 학생이 맨 마지막 학생일 때
            if reserve.count(front_student) != 0: # 앞에 학생이 여벌 옷이 있다면
                reserve.remove(front_student) # 해당 학생의 여벌옷 제거
                lost.remove(lost_n)
                
        else: # 잃어버린 학생이 중간학생
            
            # 앞에 학생부터 검사
            if reserve.count(front_student) != 0: # 앞에 학생이 여벌 옷이 있다면
                reserve.remove(front_student) # 앞에 학생의 여벌옷 제거
                lost.remove(lost_n)
                
            # 뒤에 학생 검사
            elif reserve.count(rear_student) != 0:
                reserve.remove(rear_student)
                lost.remove(lost_n)
        
        
        
        answer = n - len(lost)
    
    
    
    
    
    return answer