"""
<힌트>
B A C D
- 추월한 선수의 이름을 부른다.
    -> A를 부르면 -> A의 등수 -= 1 / B 의 등수 += 1  A B C D
    
    
<조건>
players : 현재 등수 리스트
callings : 불리는 순서

<접근>
- A의 인덱스를 찾아서 index() -> 인덱스 - 1 이 B의 인덱스 
    -> index함수 O(n)
    -> callings -> 1000000
    -> 50,000 * 1,000,000 = 50,000,000,000 불가능

<접근 2>
n번 인덱스에 NAME 선수가 있다는 것만 기록
-> 딕셔너리

"""

def solution(players, callings):
    answer = []
    name = dict()
    num = dict()
    
    
    for i, player in enumerate(players):
        name[player] = i # 이름 : 등수
        num[i] = player # 이름 : 등수
    
    for count, call in enumerate(callings):
        # call = 추월할 선수 이름
        # print(num)
        
        a_now = name[call] # 추월할 선수 등수
        
        b_name = num[a_now - 1] # 추월당할 선수 이름
        b_now = name[b_name] # 추월당할 선수 등수
        
        name[call] -= 1 # 추월하기
        num[a_now] = b_name
        
        name[b_name] += 1 # 추월 당하기
        num[b_now] = call
        
        # print(f'{count} => {call}선수가 {a_now}등 에서 {b_now}등으로 앞서간다. / {b_name}선수가 {b_now}등 에서 {a_now}등으로 내려간다.')
        # print(num)
    sorted_num = sorted(num.items())
    
    for n, p in sorted_num:
        answer.append(p)
    
    
    return answer