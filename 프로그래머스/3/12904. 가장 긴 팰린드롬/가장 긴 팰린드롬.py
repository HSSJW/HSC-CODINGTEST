"""
뒤집어도 똑같은 문자열

<목표>
- 부분 문자열 중 가장 긴 '팰린드롬'의 길이
-> 조건을 만족하는 최소 길이 검사 -> 파나메트릭 서치?

"""

def solution(s):
    answer = 1 # 1글자는 무조건 팰린드롬 이므로 기본값 1로 초기화
    n = len(s)
    
    
    
    
    # 좌우 대칭 검사이므로 중심 확장형 구조 사용할 수 있다.
    # 중심 확장형은 투포인터 알고리즘의 파생형이므로 체크하는 메서드의 매개변수는 2개이다.
    def check(left, right): 
        
        
        while left >= 0 and right < n:
            
            if s[left] != s[right]: # 한번이라도 다르면 실패이다.
                return right - left - 1
            else:
                left -= 1 # 왼쪽으로 한칸 이동
                right += 1 # 오른쪽으로 한칸 이동
        
        return right - left - 1 # ‼️마지막 확장은 실패한 상태이므로 되돌려야한다.‼️
        
    for i in range(n):
        
        answer = max(answer, check(i, i)) # 글자가 홀수개일 때
        answer = max(answer, check(i, i+1))
    

    return answer









