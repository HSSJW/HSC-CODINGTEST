def solution(brown, yellow):
    answer = []
    
    """
    노란색의 블럭이 서로 맞닿은 면이 많아야한다 -> 최대한 정사각형에 가까운 모습
    
    -> 특정 숫자n(height)으로 나누어 떨어질 때(yellow%n == 0) n과 yellow/n 사이의 차이가 최소가 되어야한다.
    
    [가로, 세로] -> 가로가 세로보다 길어야한다
    """
    """
    1. 갈색을 넣을 수 있는 모든 박스 만든다
    - 갈색 네모의 모퉁이 제거 -> brown - 4
    - 남은 brown으로 만들수 있는 속이 비어있는 사각형 (한쪽 길이 1이상)
    - 사각형 개수를 길이 1로 취급한다
    2. yellow의 개수가 (brown의 가로 - 2) * (brown의 세로 - 2) 와 같은지 검사
    """
            
    brown -= 4
    brown /= 2 # 양쪽을 구성하는 박스이므로 나눠주기
    
    width = brown - 1
    height = 1
    
    while width >= height:
        
        area = width * height
        
        if area == yellow:
            answer.append(width+2) # 노란색에 직접 닿는 면 길이만 포함한게 width이므로 모서리 추가
            answer.append(height+2)
            return answer
        
        width -= 1
        height += 1
    
    
    return answer