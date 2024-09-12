import sys
input = sys.stdin.readline

def isGroup(word):
    seen = set() # set() 집합
    prev_char = ''    #이전에 저장한 문자를 저장

    for char in word: #단어를 char단위로 순회
        if char != prev_char: #바로 앞에 있는 글자가 아닌데
            if char in seen:  #이전에 봤던 문자가 다시 나오면
                return False
            seen.add(char) #처음나온 글자일 때 >> set seen에 추가
        prev_char = char


    return True #그룹단어인 경우


n = int(input())

result = 0


for i in range(n):
    word = input()
    if(isGroup(word)):
        result += 1

print(result)
    
