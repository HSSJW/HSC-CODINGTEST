from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque()
    """
    - 진도가 100%일 때 서비스에 반영
    - 뒤에있는 기능이 먼저 개발될 수 있지만 배포는 앞에있는 기능이 배포될 때 함께 배포
    - progresses : 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열
    - speeds : 각 작업의 개발 속도가 적힌 정수 배열
    - 배포는 하루에 한번만 가능
    
    answer = 각 배포마다 (몇개)의 기능이 배포?
    
    """
    
    progresses_days = []
    
    for i in range(len(progresses)):
        rest_job = 100 - progresses[i]
        speed = speeds[i]
        period = 0
        
        if rest_job % speed == 0: # 특정 작업의 남은일이 나누어 떨어지는 경우
            period = rest_job/speed
            
        else: # 나누어 떨어지지 않는 경우
            period = rest_job//speed + 1 # 남은 작업을 끝내는 일 수
            
        progresses_days.append(period)
        
        # [7, 3, 9]

        
    for i in range(len(progresses_days)):
        now_pro = progresses_days[i]
            
            
        if len(queue) == 0:
            queue.append(now_pro)
                
            continue
                
            
        if queue[0] >= now_pro: # 현재 작업이 다음 배포되야할 작업보다 먼저 끝나는 경우 -> 다음 배포때 함께 진행
            queue.append(now_pro)
        else:
            answer.append(len(queue))  # 다음 배포 때 배포될 작업 개수 저장하고
            queue.clear() # 큐 비우기
            queue.append(now_pro)
            
            
    answer.append(len(queue))

    
    return answer