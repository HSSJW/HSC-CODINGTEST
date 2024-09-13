import sys
from calendar import firstweekday
from datetime import datetime

input = sys.stdin.readline

month, d, y, time = input().split() #띄어쓰기 기준으로 자동으로 분리
# May / 10, / 1981 / 00:31

d = d.rstrip(',')  # , 제거
h, m = time.split(':') # :기준으로 좌우 분리  h=시간 m=분

month = datetime.strptime(month, '%B').strftime('%m')  #문자로된 '월'을 datetime형으로 바꾸고 다시 문자열 형태로 변환

month, d, y, h, m = int(month), int(d), int(y), int(h), int(m)

first_day = datetime(y, 1, 1) #그 해의 첫 날
last_day = datetime(y+1, 1, 1) #다음 해의 첫 날
today = datetime(y, month, d, h, m)
today_long = today - first_day #올해의 며칠이 흘렀는지
year_long = last_day - first_day # 올해의 길이

print((today_long/year_long)*100)




