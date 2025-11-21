def solution(n):
    answer = 0
    
    """
    format(num, bin)
    """
    
    big_num = n
    bin_n = str(format(n, 'b'))
    n_count = bin_n.count('1')
    
    while True:
        big_num += 1
        
        bin_big_num = str(format(big_num, 'b'))
        big_count = bin_big_num.count('1')
        
        if n_count == big_count:
            return big_num
        
    
    return answer