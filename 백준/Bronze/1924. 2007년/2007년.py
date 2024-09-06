import sys, datetime

input = sys.stdin.readline


x, y = map(int, input().split())


days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

print(days[datetime.date(2007, x, y).weekday()])

