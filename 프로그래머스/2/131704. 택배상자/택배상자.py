"""
<힌트>
- 상자가 1~n까지 순서대로 벨트에 '일렬'로 놓여 전달된다.
- 벨트는 한 방향으로만 진행 -> deque
- 택배 기사님이 미리 알려준 순서대로 실어야한다.

- 보조 컨테이너는 마지막에 넣은 것부터 빼야함 -> 스택

<조건>
- 기사님이 원하는 순서에 맞게 못하게 되면 중단

[1 2 3 4 5]
[4 3 1 2 5]

<접근>
- 메인의 left와 보조의 꼭대기 중에 기사[0]이 없으면 중단.
    - 기사[0]과 같은게 발견되면 둘다 각각 제거

"""

from collections import deque

def solution(order):
    answer = 0
    n = len(order)
    main = deque([(i+1) for i in range(n)]) # 메인 벨트 -> deque

    sub = [0] # 보조벨트 -> stack

    for box in order:
        
        if main and main[0] == box: # 메인 벨트에서 싣기
            # print(f'{box}번 상자 메인에서 싣기')
            main.popleft()
            answer += 1
            
        elif sub and sub[len(sub)-1] == box:
            # print(f'{box}번 상자 sub에서 싣기')
            sub.pop()
            answer += 1
        
        else: # 둘다 없음
            
            while True:
                
                if main: # main이 비어있지 않다면 sub로 옮기면서 찾아보기
                    sub.append(main.popleft())
                
                if main:
                    if main[0] == box: # 메인벨트에서 찾아서 꺼내기
                        # print(f'{box}번 상자 main에서 뒤져서 싣기')
                        main.popleft()
                        answer += 1
                        break
                        
                else: # 못찾고 메인 벨트가 비어버렸다.
                    return answer # 실패

    
    return answer



