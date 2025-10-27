def solution(phone_book):
    answer = True
    
    """
    한 번호가 다른 번호의 접두어 인 경우 -> flase
    접두어인 경우가 하나도 없으면 True
    """
    
    phone_book.sort(reverse=False) # 문자열들 정렬 -> 접두어가 같으면 연속한 인덱스에 위치
    
    for i, phone in enumerate(phone_book):
        length = len(phone)
        
        
        if i != 0 and phone_book[i-1].startswith(phone): # startswith -> 해당 문자열로 시작하면 True-> 접두어이면
            answer = False
            return answer
            
        elif i != len(phone_book)-1 and phone_book[i+1].startswith(phone):
            answer = False
            return answer
    
    return answer