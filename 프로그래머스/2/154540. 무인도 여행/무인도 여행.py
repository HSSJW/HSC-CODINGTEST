"""
<힌트>
- 격자 칸 / 각 칸에는 1~9 자연수 들어있음
- 섬 찾기 -> dfs / 모든 좌표 확인하면서 visited가 아닌 칸이 나오면 해당 칸에서 dfs 시작한다.
    -> visited는 1개만 운용한다.

<조건>
x : ㅂ다ㅏ
1~9 : 무인도 (숫자는 식량) -> 숫자를 모두 합친 값 : 해당 무인도에서 머무를 수 있는 기간
상, 하, 좌, 우 로 연결되는 땅들 -> 하나의 무인도를 이룸

"X591X",
"X1X5X",
"X231X", 
"1XXX1"

<목표>
- 각 섬에 최대 며칠씩 머무를 수 있는지? 모두 기록해서 오름차순으로 return
    -> 섬을 찾고
    -> 섬을 찾는 과정에서 그 안에있는 숫자 합(식량 총합)도 구해주기
    
<접근>
- dfs : 스택,

"""



def solution(maps):
    answer = []
    row_n = len(maps)    # 지도의 세로 길이
    col_n = len(maps[0]) # 지도의 가로 길이
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 이동할 때 더해주기
    
    
    # 미방문 상태면 False
    visited = [[False] * (col_n) for _ in range(row_n)]
    
    
    for r in range(row_n):
        for c in range(col_n):
            #  섬 발견                    미방문 
            if maps[r][c] != 'X' and not visited[r][c]: # 미방문 상태 섬 발견
                
                stack = [(r, c)] # 스택에 추가
                foods = 0 # 이번 섬의 식량을 누적한다.
                
                while stack:
                    
                    row, col = stack.pop()
                    visited[row][col] = True
                    print(f'maps[{row}][{col}]에서 {maps[row][col]}를 더하기')
                    foods += int(maps[row][col])
                    
                    
                    
                    for move_r, move_c in moves: # 상/하/좌/우 시도
                        
                        # 이 move로 맵을 벗어나지 않고
                        if 0 <= row+move_r < row_n and 0 <= col+move_c < col_n:
                            if maps[row+move_r][col+move_c] != 'X' and not visited[row+move_r][col+move_c]: # 미방문 상태라면
                                visited[row+move_r][col+move_c] = True
                                stack.append((row+move_r, col+move_c)) # 스택에 추가
                
                
                answer.append(foods)
    
    if not answer: # 비어있으면 -> 섬이 없으면 -> -1
        return [-1]
    else:
        return sorted(answer)
    
    return answer

