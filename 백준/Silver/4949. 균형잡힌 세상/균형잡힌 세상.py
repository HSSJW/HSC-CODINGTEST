import sys
input = sys.stdin.readline

line = ""

left_parent = ['(', '{', '[']
right_parent = [')', '}', ']']



while True: # .만 입력하면 종료
    stack = list()
    is_valid = True

    line = input().rstrip("\n")

    if line == ".":
        break


    for char in enumerate(line): #문자열을 한 인덱스씩 순회
        # print(char[0])
        if char[1] == ".": # 이 문장의 끝
            break
            
        if char[1] in left_parent:
            stack.append(char[1])




        elif char[1] in right_parent:
            if len(stack) == 0:  # 오른쪽괄호가 나왔는데 왼쪽 괄호가 없는 경우
                is_valid = False
                break
            else:                # 오른쪽 괄호가 나왔는데 짝이 안맞는 경우 필터링
                popped = stack.pop()  # pop한 결과를 저장
                if left_parent.index(popped) != right_parent.index(char[1]):
                    is_valid = False
                    break


    if is_valid and len(stack) == 0:
        print('yes')
    else:
        print("no")