def solution(array, commands):
    answer = []
    
    
    
    count = len(commands)
    
    for index in range(count):
        i = commands[index][0]
        j = commands[index][1]
        k = commands[index][2]
        temp_list = []         # 뽑아낸 값들을 넣어서 정렬하기 위한 임시배열
        
        for z in range(i-1, j):
            temp_list.append(array[z])
        temp_list.sort()
        answer.append(temp_list[k-1])
    
    
    return answer