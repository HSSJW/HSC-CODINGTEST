#         데이터    기준  정보의 기준값   정렬할 기준이 되는 문자열
def solution(data, ext, val_ext, sort_by): 
    
    size = len(data) # 데이터셋의 개수
    
    
    target = None # 기준의 배열 번호
    
    if ext == "code":
        target = 0
    elif ext == "date":
        target = 1
    elif ext == "maximum":
        target = 2
    else:
        target = 3
        
    order_by = None  # 정렬기준 데이터 index
    
    if sort_by == "code":
        order_by = 0
    elif sort_by == "date":
        order_by = 1
    elif sort_by == "maximum":
        order_by = 2
    else:
        order_by = 3
        
        
    c_index = [] # 기준값 검사를 통화한 데이터셋의 index
    
    for i in range(size):   # 데이터 셋 순회하며 기준값 검사
        
        if int(data[i][target]) < val_ext: # 기준값을 통과한 경우
            c_index.append(i) # 통과한 데이터 index

    result = []
            
    for i in c_index:
        result.append(data[i])   # 검증된 값의 데이터만 들어있는 리스트
    
    result = sorted(result, key=lambda x: x[order_by])
    
    answer = result
    return answer