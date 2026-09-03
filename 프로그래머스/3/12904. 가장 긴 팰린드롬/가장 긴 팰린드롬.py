"""
<힌트>
- 팰린드롬 : 앞뒤를 뒤집어도 똑같은 문자열
- s의 부분문자열 중에서 가장 긴 팰린드롬의 길이
    -> 대칭성 확인


"""
def solution(s):
    answer = 0
    
    n = len(s)
    
    for flag in [True, False]:
    
        left = 0
        right = 0
    
        for i in range(n):

            if flag:
                left = i
                right = i+1
            else:
                left = i
                right = i
            

            while left >= 0 and right < n: # 문자열 범위 안쪽
                
                if s[left] == s[right]: # 대칭
                    if right - left + 1 > answer:
                        answer = right - left + 1 # 길이 기록
                    # print(f'left = {s[left]} right = {s[right]}로 {right - left + 1}글자 대칭 answer = {answer}')

                    left -= 1
                    right += 1


                else: # 이번부터 대칭이 아님

                    break
        

    return answer


