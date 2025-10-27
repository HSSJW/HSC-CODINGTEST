from collections import deque

def solution(answers):
    answer = []
    
    """
    1, 2, 3, 4, 5
    2-1, 2-3, 2-4, 2-5, 2-1, 2-3  
    3-3, 1-1, 2-2, 4-4, 5-5, 3-3, 1-1, 2-2 (3->1->2->4->5-> ...)
    
    """
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    scores = [0, 0, 0]
    
    for i, num in enumerate(answers):
        for j, pattern in enumerate(patterns): # n번째 문제에 대해 세 명의 답을 채점
            
            if num == pattern[i % len(pattern)]:
                scores[j] += 1
    
    max_score = max(scores)
    
    for i, score in enumerate(scores):
        if max_score == score:
            answer.append(i+1)
    
    
    
    
    return answer