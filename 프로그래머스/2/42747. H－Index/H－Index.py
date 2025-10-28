from collections import Counter

def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    
    
    for i, citation in enumerate(citations):
        if citation < i+1:
            answer = i
            return answer
    
    answer = len(citations)
    
    return answer