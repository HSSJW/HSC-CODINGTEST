from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    """
    장르별 -> 종류가 존재 -> 해시?
    두개씩 모아 -> 조합? -> 해시?
    
    수록하는 기준 -> 우선순위? -> 힙?
    1. 속한 노래가 ✅많이 재생된 장르✅를 먼저 수록합니다. -> 해당 장르별로 최대 두개
    2. 장르 내에서 ✅많이 재생된 노래✅를 먼저 수록합니다. 
    3. 장르 내에서 재생 횟수가 같은 노래 중에서는 ✅고유 번호가 낮은✅ 노래를 먼저 수록합니다.

    genres : 노래의 장르 -> [str]
    plays : 노래별 재생횟수 -> [int]
    고유번호 : 인덱스
    
    여러 종류로 정렬 -> 리스트 인덱스 순서 맞춰서 sorted
    
    <return>
    베스트 앨범에 들어갈 노래를 고유번호 순서대로 -> key = lambda x : 리스트[고유번호가 있는 인덱스]
    """
    
    music_dict = defaultdict(list)
    
    
    
    for i, genre in enumerate(genres): # 인덱스 순서대로 검사하므로 자동으로 뒤에 고유번호가 높은 것들이 들어감

        
        music_dict[genre].append([i, plays[i]])
            
    """
    music_dict = [
        classic : [[0, 500], [3, 800]]
        
    ]
    """
            
    genre_total_play = [] # [[장르명, 장르별 재생횟수]] -> 재생횟수 기준으로 정렬
    
    for genre, item in music_dict.items():
        
        genre_total_play.append([genre,sum([song[1] for song in item])])
        
    
    genre_total_play.sort(reverse=True, key = lambda x: x[1])   # 재생횟수 기준으로 정렬 -> 정렬된 genre_total_play[0]을 순회하면서 노래 answer에 인풋
    
    
    for genre in genre_total_play:
        
        music_dict[genre[0]].sort(reverse=True, key=lambda x: x[1])
        genre_list = music_dict[genre[0]]
        
        music_index = [item[0] for item in genre_list] # 특정 장르의 인덱스만 저장
        
        answer.extend(music_index[:2])
    
    
    
    
    return answer