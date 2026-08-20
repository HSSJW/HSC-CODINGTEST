-- 코드를 입력하세요
/*
<USED_GOODS_BOARD> B
BOARD_ID, : 게시글 ID
WRITER_ID,  : 작성자 ID
TITLE,      : 게시글 제목
CONTENTS,   : 게시글 내용
PRICE,      : 가격
CREATED_DATE,  : 작성일
STATUS,      : 거래상태
VIEWS        : 조회수

<USED_GOODS_REPLY> R
REPLY_ID  : 댓글 ID
BOARD_ID  : 게시글 ID - FK
WRITER_ID : 작성자 ID   FK
CONTENTS  : 댓글 내용
CREATED_DATE : 작성일


게시글 제목 / 게시글 ID / 댓글 ID / 댓글 작성자 ID /댓글 내용 / 댓글 작성일

- 댓글 작성일 / 게시글 제목 기준 오름차순
*/

SELECT B.TITLE,
    B.BOARD_ID,
    R.REPLY_ID,
    R.WRITER_ID,
    R.CONTENTS,
    R.CREATED_DATE
FROM USED_GOODS_BOARD B
JOIN USED_GOODS_REPLY R ON B.BOARD_ID = R.BOARD_ID
WHERE YEAR(B.CREATED_DATE) = 2022 AND MONTH(B.CREATED_DATE) = 10
ORDER BY R.CREATED_DATE, B.TITLE;
