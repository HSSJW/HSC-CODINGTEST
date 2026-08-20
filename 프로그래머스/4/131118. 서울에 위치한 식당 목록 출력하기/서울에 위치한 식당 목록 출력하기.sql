-- 코드를 입력하세요

/*
<REST_INFO>
REST_ID : 식당 ID
REST_NAME : 식당 이름
FOOD_TYPE : 음식 종류
VIEWS : 조회수
FAVORITES : 즐찾수
PARKING_LOT : 주차장 유무 (N/Y)
ADDRESS : 주소
TEL : 전화번호

<REST_REVIEW>
REVIEW_ID : 리뷰 ID
REST_ID : 식당 ID FK
MEMBER_ID : 회원 ID FK
REVIEW_SCORE : 점수
REVIEW_TEXT : 리뷰 텍스트
REVIEW_DATE : 리뷰 작성일


식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 

리뷰 평균 점수
- 리뷰 평균점수 소수점 두번째 까지 출력
- 평균점수 DESC
- 즐찾수 DESC
*/


SELECT 
    I.REST_ID, 
    I.REST_NAME, 
    I.FOOD_TYPE, 
    I.FAVORITES, 
    I.ADDRESS, 
    ROUND(AVG(R.REVIEW_SCORE), 2) AS SCORE
FROM
    REST_INFO I
JOIN
    REST_REVIEW R ON I.REST_ID = R.REST_ID
WHERE
    I.ADDRESS LIKE '서울%'
GROUP BY
    I.REST_ID
ORDER BY
    SCORE DESC,
    FAVORITES DESC;
    



    