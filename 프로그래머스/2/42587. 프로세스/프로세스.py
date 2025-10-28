from collections import deque

def solution(priorities, location):
    answer = 0
    
    """
    큐 -> 우선순위가 있으면 힙 사용
    특정 프로세스가 몇번째?
    
    1. [우선순위, 인덱스]를 가지는 이차원 배열의 힙 만든다 -> 1. 우선순위, 2. 인덱스 기준 정렬
    2. location == 인덱스인 리스트가 몇번째로 나오는 찾는다
    """
    temp = [[priority, index] for index, priority in enumerate(priorities)]
    # [[9,2], [1, 0], [1,1], [1, 3], [1, 4], [1, 5]]
    
    que = deque(temp)
    
    while len(que) != 0: # 덱이 빌때까지
        
        # 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
        job = que.popleft()
        priority = job[0]
        index = job[1]
        
        # 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
        if len(que) != 0 and priority < max([item[0] for item in que]):
            que.append(job)
            
        else:
            answer += 1
            if index == location: # 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
                break
        
        # [ [1, 0], [1,1]] ans = 1
    
    return answer