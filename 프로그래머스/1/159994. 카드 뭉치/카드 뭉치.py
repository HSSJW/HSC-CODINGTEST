from collections import deque

def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    # goal 단어를 순회하면서 cards1 2각각의 맨앞 값중 일치하는게 있으면 -> 순회
    #                                                     없다면 -> NO
    card1, card2 = deque(cards1), deque(cards2)
    
    
    for target in goal:
        if card1:
            if target == card1[0]:
                card1.popleft()
                continue
                
        if card2:
            if target == card2[0]:
                card2.popleft()
                continue
        
        
        answer = "No"
    
    
    
    return answer