def solution(t, p):
    answer = 0
    
    t_list = []
    for i in range(len(t)-len(p)+1):        #한자리씩 뒤로 이동하면서
        t_list.append(int(t[i:i+len(p)]))    # p의 길이만큼 잘라서 t_list에 저장
                      
    num_p = int(p)
                      
    for num in t_list:
        if num <= num_p:
            answer += 1
                      
        
    return answer