def solution(s):
    answer = 0 # 더 큰 팰린드롬이 발견되면 초기화
    n = len(s)
    
    # 고정된 데이터에 대해 `구간`에 대한 검사 -> 투포인터
    # 좌우 대칭 검사 -> 중앙 확장형 투포인터
    # 투포인터로 대칭검사 할 때는 i에서 a, b모두 출발하는 경우와
    # a : i b : i+1인 경우를 모두 수행해야한다.
    # 투포인터는 고정된 데이터의 `모든 구간`에 대해서 수행한다.
    # 구간의 너비는 right - left + 1
    
    for i in range(n):
        # 한점에서 출발
        left = i
        right = i
        
        count = 0
        while left >= 0 and right < n: #구간을 벗어나지 않는 동안
            
            if s[left] == s[right]: # 대칭 성립
                
                count = right - left + 1
                
                left -= 1
                right += 1
                
                
            else: # 대칭 깨짐
                break
                
        if answer < count:
            answer = count
    
    # 중앙 확장형 대칭검상에서는 i i+1에서 출발하는 것도 따로 검사한다.
    

    for k in range(n-1):

        # 한점에서 출발
        left = k
        right = k+1
        
        count = 0
        while left >= 0 and right < n: #구간을 벗어나지 않는 동안
            
            if s[left] == s[right]: # 대칭 성립
                count = right - left + 1

                left -= 1
                right += 1
            else: # 대칭 깨짐
                break

        if answer < count:
            answer = count

    return answer