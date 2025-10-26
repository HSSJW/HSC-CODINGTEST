def solution(sizes):
    answer = 0
    
    set_count = len(sizes)
    
    for i in range(set_count):
        temp = 0
        
        if sizes[i][0] < sizes[i][1]: # 더 긴쪽길이를 0번인덱스 자리에 위치시킨다
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
        
    max_width, max_height = 0, 0
    
    for i in range(set_count):
        if max_width < sizes[i][0]:
            max_width = sizes[i][0]
            
    for i in range(set_count):
        if max_height < sizes[i][1]:
            max_height = sizes[i][1]
            
    answer = max_width * max_height
    
    return answer