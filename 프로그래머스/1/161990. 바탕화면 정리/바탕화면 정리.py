"""
<힌트>
- 프로그래머스에서 작성한 코드는 전부 삭제
- 정사각형 격자판 -> 좌표계 주의 -> 왼쪽 가장위가 0, 0 (행, 열)
- 드래그해서 파일들을 선택해서 삭제


<조건>
. : 빈칸
# : 파일

<목표>
- 최소한의 이동거리로 모든 파일을 선택해서 지운다. -> 왼쪽 맨위에서 오른쪽 맨 아래까지

<접근>
- #이 있는 좌표 중 가장 작은 lux, luy / 가장 큰 rdx, rdy
"""

def solution(wallpaper):
    answer = []
    lux, luy= 50, 50 # 인덱스가 0~49 이므로 무조건 50보다 작다
    rux, ruy = -1, -1 #
    
    row = len(wallpaper)
    col = len(wallpaper[0])
    
    for r in range(row):
        for c in range(col):
            
            if wallpaper[r][c] == '#':
                
                if lux > r:
                    lux = r
                if luy > c:
                    luy = c
                
                if rux < r:
                    rux = r
                if ruy < c:
                    ruy = c
    
    
    return [lux, luy, rux+1, ruy+1]