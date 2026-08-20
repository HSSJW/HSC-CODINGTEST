"""
- 09:00 ~ t분 간격으로 n회 운행
- 한번에 m명 탑승 가능
- 딱맞춰 도착해도 탈 수 있다.
- 자리가 없으면 '줄'을 서서 기다린다. -> fifo -> deque


<목표>
- 셔틀을 타고 사무실에 갈 수 있는 '가장 늦은 도착 시간'

<조건>
- 같은 시간에 도착한 크루 중에 가장 마지막에 append

- 탈 수 있는가? -> 특정 시간에 와서 탈 수 있는가를 찾아야함 -> 파라메트릭 서치?
- 최대한 늦은 시간 찾는 것이므로 k시간에 성공하면 더 일찍은 볼 필요도 없다 -> 파라서치


<접근>
- 줄 : deque
- 탈 수 있는가? -> 버스가 왔을 때 deque에서 m만큼 popleft
    - 중간에 콘(mid)가 popleft되면 True -> lo = mid+1
- 시간 : 분단위로 계산

"""

from collections import deque

def solution(n, t, m, timetable):
    answer = 540
    
    m_time = []
    
    # 분단위 시간으로 변환
    # 09:00 -> 540 23:59 -> 1439
    for time in timetable:
        hour, minute = time.split(":")
        m_time.append(int(hour) * 60 + int(minute))

    m_time.sort()
    
    line = deque()
    last = 540 + t * (n-1)

    
    # mid시간에 도착했을 때 가능하다 -> True
    # k분까지 출근 가능한 인원 = 0900 ~ k시 사이 횟수 * m = ((mid - 540) // t) * m
    # 'k분까지 출근 가능한 인원'보다 ('m_time의 원소중 mid 이하인 것' + 1) 이하여야한다.
    # 막차 시간 >= mid 이어야 한다.
    def check(mid):
        if last < mid:             # 막차보다 늦게 왔다
            return False

        # 콘보다 늦게 온 크루는 콘 뒤에 선다 → 자리를 뺏을 수 없으므로 제외
        #    (동시각이면 콘이 맨 뒤이므로 <= 로 포함)
        line = deque(x for x in m_time if x <= mid)

        for i in range(n):
            bus = 540 + t * i
            seat = m               # 버스마다 정원 리셋 (m*n 통짜 풀이 아님)

            # 앞사람부터 태운다
            while seat > 0 and line and line[0] <= bus:
                line.popleft()
                seat -= 1

            # 앞사람 다 태우고도 자리가 남았고, 콘이 이 버스를 탈 수 있는 시각에 왔다면
            if seat > 0 and mid <= bus:
                return True

        return False
    
    
    lo, hi = 0, 1439
    
    while lo <= hi:
                
        mid = (lo + hi) // 2 # 719

        
        success = check(mid)
        
        if success: # 성공 -> 더 늦은 시간 시도
            
            answer = mid
            
            lo = mid + 1
        else:
            
            hi = mid - 1
    
    
    
    hour = answer // 60
    minute = answer % 60
    
    if hour < 10:
        hour = '0' + str(hour)
    else:
        hour = str(hour)
        
    if minute < 10:
        minute = '0' + str(minute)
    else:
        minute = str(minute)
        
    answer = hour + ":" + minute
    
    return answer


