"""
<힌트>
- 상하좌우 움직임 -> moves 사용
- 격자판 -> 경로탐색?
- 격자판 -> 행열 좌표계? / 데카르트 좌표계? -> 데카르트 -> 왼쪽이 x증가, 위쪽이 y증가



<목표>
- 처음 걸어본 길의 길이 : 이미 방문한 곳을 재방문 허용하면서 길이 추가는 하지않기
- 방문한 노드가 아니고 걸어본 길 -> 양방향을 모두 고려해야한다.
    -> (a, b)를 튜플로 정렬해서 set에 기록해서 지나가본 길인지 아닌지 판단

- 박스가 아니라 점으로 이동하므로 각 점을 칸으로 생각해야함
    -> -5 ~ 5이면 11 * 11 이어야한다.

"""


def solution(dirs):
    answer = 0 # 처음 가는 길 횟수 누적
    x1, y1 = 0, 0 # 시작위치
    
    # 상 하 좌 우
    # moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    moves = {"U":(0, 1), "D":(0, -1), "L":(-1, 0), "R":(1, 0)} # moves[커맨드]
    visited = set() # 이 안에 ((x1, y1) (x2, y2))를 기록한다. -> 이미 지나간 길
    
    
    
    for d in dirs:
        dx, dy = moves[d] # 이동 방향
        x2, y2 = x1+dx, y1+dy
        
        if x2 < -5 or x2 > 5 or y2 < -5 or y2 > 5:
            continue
        
        sort_point = tuple(sorted([(x1, y1), (x2, y2)]))
        
        if sort_point not in visited: # 처음 와본 길일 때 
            answer += 1 # 걸은 길 + 1
            visited.add(sort_point) # 방문했다고 체크하기
        
        x1 = x2 # 이동 하기
        y1 = y2
    
    
    
    return answer



