from functools import cmp_to_key

def compare(x, y):
    if x + y > y + x: # xy순서로 이어붙인게 더 클 때
        return -1
    elif x + y < y + x: # y의 우선순위가 더 크다
        return 1
    else:
        return 0
    

def solution(numbers):
    answer = ''
    
    """
    정수를 이어 붙여 만들 수 있는 가장큰 수 
    -> 맨앞자리수가 가장 큰게 앞으로 와야한다
    
    """
    
    # str_num = list(map(str, numbers))
    str_num = [str(num) for num in numbers]
    
    
    temp_list = sorted(str_num, key = cmp_to_key(compare)) # 모든 숫자 조합에 대해 자동으로 compare함수를 실행해준다
    
    for number in temp_list:
        answer += number
                         
            
    if answer[0] == '0':
        answer = '0'
    
    return answer



"""
리스트를 형변환한 새로운 리스트 만들기 -> 1. map(자료형, 리스트), 2. 컴프리헨션

from functools import cmp_to_key() -> sorted(정렬대상, key=cmp_to_key(실행할 함수명)) 📌 sorted가 자동으로 모든 값에 대해 함수를 실행해준다


"""