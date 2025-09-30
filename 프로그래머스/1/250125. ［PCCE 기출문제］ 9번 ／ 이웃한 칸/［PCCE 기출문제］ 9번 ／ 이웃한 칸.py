def solution(board, h, w):
    
    n = len(board) # n * n 배열
    
    count = 0
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        
        if h_check > n-1 or w_check > n-1 or h_check < 0 or w_check < 0: # 
            continue
        
        color_check = board[h_check][w_check] # 검사 대상 샛
        
        if (0 <= h_check < n) and (0 <= w_check < n):
        
            if board[h][w] == color_check:
                count += 1
    
    answer = count
    
    
    return answer