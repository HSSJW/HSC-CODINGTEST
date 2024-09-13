import sys
input = sys.stdin.readline


text = input().strip()
find_word = input().strip()
word_len = len(find_word)

next_index = 0 #검색 시작위치
result = 0

while next_index  <= len(text):

   if text[next_index:next_index + word_len] == find_word: #검색하는 단어의 위치까지만 검색
       result += 1
       next_index += word_len
   else:
       next_index += 1



print(result)