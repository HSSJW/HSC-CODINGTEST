from collections import Counter

def solution(participant, completion):
    answer = ''
    
    """
    
    """
    
    p_counter = Counter(participant)
    c_counter = Counter(completion)
    
    tmp_counter = p_counter - c_counter
    
    answer = list(tmp_counter.keys())[0]
    
    return answer