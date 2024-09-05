n = int(input())

nNum = n # 새로운 수
save = n
result = 0 #싸이클


while True:


    nNum = int(nNum / 10) + (nNum % 10)
  
    nNum = (save % 10) * 10 + nNum % 10
    save = nNum

    result += 1

    if(n == nNum):
        break

    


print(result)
