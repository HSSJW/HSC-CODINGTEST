"""
<힌트>
- 과락 : (근태 점수) (동료 평가 점수) 둘다 다른 사람보다 낮은 경우가 한번이라도 존재하는 경우
- 한번이라도 존재 -> 모두 검사해야함 -> 완탐인데 이중 반복문 불가능
    👉 이중 반복문이 필요하다는 것은 두개의 축이 있다는 것이다. -> 하나의 축을 먼저 정렬해버리면 1중 반복문으로 테스트 가능 -> 각 축을 각각 다른 기준으로 정렬해버리고 1순위 정렬을 그대로 두고 2순위 정렬 축을 기준으로 비교하면된다.


<접근>
1. 근태 점수를 먼저 내림차순 정렬 -> index가 증가할수록 근태점수는 같거나 같다 
2. 

[3,2] [3,2] [2,1] [2,2] [1,4]
[내림, 오름] -> 0번 인덱스가 같은 경우에는 scores[i]와 scores[i+1]을 비교했을 때 
            - b의 1번 인덱스가 a의 1번 인덱스보다 작은 경우는 무조건 둘다 더 작은 과락이다 -> 1번 인덱스는 오름차순 이므로 오른쪽으로 갈 수록 커지고 때문에 [0]이 같은데 [1]은 더 작은 경우가 존재할 수 없다. 
"""


def solution(scores):
    answer = 0
    
    whanho = scores[0]
    whan_s = scores[0][0] + scores[0][1]

    
    scores.sort(key=lambda x :(-x[0], x[1])) # 0번 : 근태 점수 -> 내림차순 1번 : 동료 점수 -> 오름 차순
    
    
    sum_scores = [scores[0][0] + scores[0][1]] # 가장 큰 사람
    
    max_y = scores[0][1]
    
    for i in range(1, len(scores)):
        
        if max_y < scores[i][1]: # [0]은 오른쪽이 무조건 같거나 작다 -> 앞족에 [1]이더 큰 경우가 있었으면 과락 
            max_y = scores[i][1]
        
        if scores[i][1] < max_y: # 과락 -> 추가하지 않는다.
            
            if scores[i] == whanho: # 완호가 과락인 경우
                return -1
            pass
        
        else:
            sum_scores.append(scores[i][0] + scores[i][1])
            
    sum_scores.sort(reverse=True) # 내림차순 정렬
    bigger_list = [] # 완호 점수보다 높은 것들 넣기
    
    for sum_score in sum_scores:
        answer += 1
        
        if sum_score <= whan_s:
            return answer
        
            
    
    
    return answer