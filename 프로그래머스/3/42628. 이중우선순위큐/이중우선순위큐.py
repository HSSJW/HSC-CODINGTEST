import heapq

def solution(operations):
    answer = []
    
    """
    모두 끝난 후 큐가 비어있으면 [0, 0]
    
    비지 않았으면 [최댓값, 최소값]
    """
    min_heap = []
    max_heap = []
    
    for oper in operations:
        if oper == 'D 1': # 최대값 삭제
            if max_heap:
                max_num = heapq.heappop(max_heap)
                min_heap.remove(-max_num) # 최소힙 리스트에서도 최대값 삭제
            
        elif oper == 'D -1': # 최솟값 삭제
            if min_heap:
                min_num = heapq.heappop(min_heap)
                max_heap.remove(-min_num) # 최대힙 리스트에서도 최소값 삭제
        
        else: # 숫자 삽입
            num = int(oper.split(' ')[1]) # 삽입할 숫자
            
            heapq.heappush(min_heap, num) #  최소힙에 삽입
            heapq.heappush(max_heap, -num) # 최대힙에 삽입 -> 꺼낼때도 부호 바꿔줘야함
    
    
    
    if  len(min_heap) == 0: # 비어있는 경우
        answer = [0, 0]
    else:
        answer = [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    
    
    return answer