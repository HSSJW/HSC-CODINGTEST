def solution(X, Y):
    answer = ''
    
    # 짝꿍이 존재하지않으면 -1
    # 짝꿍이 0만 있으면 0
    
    # 정수형으로 리스트 값으로 저장
    x_list = [int(c) for c in X]
    y_list = [int(c) for c in Y]
    
    pair_list = []
    
    for num in set(x_list): # x의 숫자들 set -> 중복제거된 리스트 -> 수정불가
        x_count = 0
        y_count = 0
        law_count = 0
        
        if num not in pair_list: # 새로운 숫자가 나올 때 마다전체에 몇개인지 검사해서 넣기 때문에 이미 있는 숫자면 건너뛰어야함
            
            if y_list.count(num) > 0:  # x에 있는 숫자가 y에도 존재
                x_count = x_list.count(num)
                y_count = y_list.count(num)
            
                law_count = min(x_count, y_count) # 특정 숫자가 일치하는 개수
        
            for i in range(law_count): # 짝꿍숫자의 순서는 상관 없으므로 append로 추가
                pair_list.append(num) 
        
    if len(pair_list) == 0: # 짝꿍이 존재하지 않는 경우
        return "-1"
    elif pair_list.count(0) == len(pair_list): #짝꿍이 0밖에 없는 경우
        return "0"
            
    # 앞쪽에 큰수가 오는게 큰수이므로 내림차수으로 정렬 후 이어 붙이기
    # pair_list = sorted(pair_list, reverse=True)  -> sorted는 정렬한 리스트를 리턴
    pair_list.sort(reverse=True) # 리스트.sort(reverse=옵션)은 해당 리스트 자체를 정렬
        
        
    for num in pair_list:
        answer += str(num)
        
        
        
            
    return answer