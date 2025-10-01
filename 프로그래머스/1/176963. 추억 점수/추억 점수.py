def solution(name, yearning, photo):
    
    answer = [] # 사진별로 합산점수저장
    
    match = dict(zip(name, yearning)) # {이름 : 점수}
    
    for one_photo in photo:    # 각 사진을 순회
        sum = 0
        
        for name in one_photo: # 특정 사진의 합산 점수를 저장
            sum += match.get(name, 0)
        
        answer.append(sum)
        
    
    
    return answer