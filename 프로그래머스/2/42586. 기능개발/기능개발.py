"""
<힌트>
- 각 기능의 개발 속도가 다르기 때문에 늦게 들어온 기능이 앞에있는 기능보다 먼저 개발될 수 있다.


<조건>
- 진도가 100% 일 때만 반영 가능
- 뒤에있는 기능이 먼저 개발되면 대기하다가 앞에있는 기능이 배포될 때 함께 배포된다.

progresses : 배포되는 순서대로 현재 작업 진도가 적인 정수 list
speeds : i번 작업의 하루 개발 속도

<접근>
- 하루에 speeds[i]를 더해서 100이 넘어가면 days에 며칠걸리는지 저장한다.
- 그리고 리스트 days를 만들어서 front -> back 검사하면서 days[i+1]가 days[i]보다 크면 앞에 개수를 세서 answer에 append 한다.
    - 이후 개수를 초기화 한다.
"""
import math

def solution(progresses, speeds):
    answer = []
    n = len(speeds)
    days = [] # i번째 기능완료가 되는데 걸리는 일수를 기록한다.
    
    for prog, speed in zip(progresses, speeds):
        
        
        
        remain = 100 - prog # 남은 작업량
        
        tmp_day = math.ceil(remain / speed) # i번째 일을 하는데 남은 일 수
        
        days.append(tmp_day)
        
    
    count = 0
    max_day = days[0]
    # days -> 0 1 2
    # n = 3
    
    # print(days)
    for i in range(n): # 0 1 2
        
        
        
        # 앞에 작업끝 날때 까지 아직 안끝남 -> 일단 앞에것들 배포
        if days[i] > max_day: 
            # print(f'{count} 넣어주기')
            answer.append(count)
            count = 1
            max_day = days[i]

            
        else:
            count += 1
        # print(f'i = {i} days[{i}] = {days[i]} count = {count} max_day = {max_day}')
            
    answer.append(count)
    return answer




