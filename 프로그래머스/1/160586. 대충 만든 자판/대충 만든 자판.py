def solution(keymap, targets):
    answer = []
    
    #하나의 키에 1~100개 무작위
    # 같은 문자가 다른 자판에 여러번 할당
    # 아예 할당되지않아 작성할 수 없는 문자도 있음
    
    # targets에 저장된 문자열을 입력하는게 목표
    
    # targets의 문자들을 순회하면서 버튼마다 검색하고 인덱스 번호가 작은걸 answer[i] += (인덱스번호 + 1)
    
    answer = [0] * len(targets)
    count = 0
    
    for target in targets:   # 입력할 각 문자열  
        for char in target:
            min_press = 102       # 0번이면 입력할 수 없는 문자열
            
            for key in keymap:
                if key.find(char) == -1: # 해당 키에 없는 문자
                    continue
                else:
                    if key.find(char) + 1 < min_press: 
                        min_press = key.find(char) + 1 #keymap에 있는 키중 가장 작은 횟수값이 저장
                    
            if min_press == 102:
                answer[count] = -1
                break
            else:
                answer[count] += min_press # 특정 문자를 가장 적은 클릭으로 입력가는 한 횟수
        
        count += 1
    
    return answer # 키를 최소 몇 번씩 눌러야 하는지