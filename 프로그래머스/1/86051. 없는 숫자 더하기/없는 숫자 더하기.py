def solution(numbers):
    answer = 0
    

    
    answer_list = [i for i in range(10) if i not in numbers]
    
    for n in answer_list:
        answer += n
    
    return answer