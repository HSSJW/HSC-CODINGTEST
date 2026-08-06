"""

<의사 코드>
1. 대기 큐 : [작업 번호 ,요청 시각, 소요 시간] 저장
2. 현재 작업 중이 아니고, 대기 큐가 비어있지 않다면 -> 우선순위가 높은 걸 꺼내서 실행
    - 우선 순위 판단 : 소요시간 짧은 것, 요청 시각이 빠른 것, 작업의 번호가 작은 것
    
3. 하나의 작업이 끝나가 다음 작업이 가능
4. 작업을 마치는 타이밍에 새로운 작업 들어오면 큐에 넣고 포함한 상태에서 우선순위 기준 

<목표>
- 반환 시간 : i번 작업이 요청된 시각부터 마칠 때 까지 (작업 종료 시각 - 요청 시각)
- 평균 반환 시간의 정수 부분

<접근>
- 큐에서 우선순위가 높은 것을 지속적으로 꺼내야한다.
    - 소요 시간 최소, 요청 시각이 빠른 것, 작업의 번호가 작은 것 
    -> 튜플로 최소힙 사용하면 순서대로 알아서 반영한다.
        -> 우선순위를 구성하는 3가지가 모두 '최소'를 가르키기 때문에 사용 가능
"""

import heapq

def solution(jobs):
    time_sum = 0
    
    que = [] # 튜플로 (소요 시간, 요청 시각, 번호)
    
    # for i, job in enumerate(jobs):
    #     que.append((job[1], job[0], i))
    
    heapq.heapify(que) # 최소힙 선언
    jobs.sort(reverse= True)

    
    sec = 0
    i = 0
    
    while que or jobs: # 큐와 작업 리스트가 모두 빌 때까지 진행
        
        while jobs and jobs[-1][0] <= sec: # jobs의 가장 먼저 요청된 작업
            job = jobs.pop()
            heapq.heappush(que, (job[1], job[0], i))
            i += 1
        
        if que: # 큐가 비어있지 않으면
        
            job = heapq.heappop(que)
            spend = job[0]
            request = job[1]
            
            if request == sec: # 요청 시각보다 현재 시각이 같다

                time_sum += spend # 반환 시간 == 소요 시간
                sec += spend

                print(f'딱맞춰 작업을 진행했고 반환 시간은 {spend}')
            elif request < sec: # 요청시각을 지났다.

                
                # 반환 시간 = 현재시간 + 소요 시간 - 요청 시각
                sec += spend
                time_sum += sec - request
                print(f'대기 중이던 작업을 진행했고 반환 시간은 {sec - request}')
            
        else: # 작업 중이 아니지만 요청시각이 안됐다.
            sec += 1
            
        
    
    return int(time_sum / i)


