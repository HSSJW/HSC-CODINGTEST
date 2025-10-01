def solution(today, terms, privacies):
    answer = []
    
    # today : 오늘 날짜 문자열 "2020.01.01"
    # terms : 약관의 유효기간 문자열  ["A 6", "B 12", "C 3"]
    # 수집된 개인정보의 정보 배열  ["2021.05.02 A"]
    
    # 28*12 = 336일 => 1년
    #         28일 => 1달
    
    
    
    # 약관 종류를 딕셔너리로 저장
    term_dict = {}
    
    for term in terms:
        term_dict[term.split(" ")[0]] = int(term.split(" ")[1]) * 28  # {A : 6*28, B : 12*28} 형태로 저장
    
    # 개인정보 수집일자 총 일수 + 유효기간(월) * 28 > 오늘까지 총 일수  일 때 => 파기
    
    today = today.split('.')
    year_today = int(today[0])
    month_today = int(today[1])
    day_today = int(today[2])
        
    days_today = year_today * 12 * 28 + month_today * 28 + day_today # 오늘까지의 총 일수
    
    for i in range(len(privacies)):
        date_part, type_part = privacies[i].split(" ") # 날짜 - 약관 타입분리
        
        # privacy_day = privacies[i].split(".")
        # year_privacy = int(privacy_day[0])
        # month_privacy = int(privacy_day[1])
        # day_privacy = int(privacy_day[2])
        year_privacy, month_privacy, day_privacy = map(int, date_part.split(".")) # 📌map 사용법📌
        
         
        days_privacy = year_privacy * 12 * 28 + month_privacy * 28 + day_privacy # 개인정보 수집일자 총 일수
        
        if days_privacy + term_dict.get(privacies[i].split()[1]) <= days_today:
            answer.append(i+1)
    
    return answer