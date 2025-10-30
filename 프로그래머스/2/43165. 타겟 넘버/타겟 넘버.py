

def solution(numbers, target):
    answer = 0
    
    """
    순서를 바꾸지않고 더하거나 빼서 -> 타겟 넘버 를 ✅만족시키는 방법의 수✅
    
    [a, b, c, d, e]
    [-a, -b, -c, -d, -e]

    """
    
    def dfs(index, current_sum):

        nonlocal answer
        
        if index == len(numbers):     # n개의 수 모두 더했을 때
            if current_sum == target:
                answer += 1            # 결과값 +1
            
            return # 재귀함수 현재 사이클 종료
            
            
        dfs(index+1, current_sum + numbers[index])
        dfs(index+1, current_sum - numbers[index])
    
    dfs(0, 0)
    
    return answer