def solution(n):
    answer = 0
    
    n_str = str(n)
    
    n_list = [int(i) for i in list(n_str)]
    
    n_list.sort(reverse = True)
    
    answer_str = ""
    
    n_list = [str(c) for c in n_list]
    
    for char in n_list:
        answer_str += char

    answer = int(answer_str)
    
    return answer