def solution(n):
    answer = []
    
    n = str(n)
    n_list = list(n)
    
    # n_list = [int(num) for num in n_list] - 리스트 컴프리헨션 방법보다
    n_list = list(map(int, n_list))         # map을 사용하는 것이 조금 더 빠르다
    
    n_list.reverse()
    answer = n_list
    
    return answer