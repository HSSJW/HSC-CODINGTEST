from collections import Counter
def solution(nums):
    answer = 0
    
    """
    n/2마리 가져가야한다 -> nCn-1
    가질 수 있는 포켓몬 종류의 최대값 : 2 최소값(같은거 2개) : 1
    
    최대한 다양한 종류의 포켓못 원함 -> 가장 많은 종류의 포켓몬을 선택하는 방법을 찾아 (종류 번호의 개수) 리턴
    """
    
    counter = Counter(nums)
    
    answer = len(counter) if len(counter) <= len(nums)/2 else len(nums)//2
    
    return answer