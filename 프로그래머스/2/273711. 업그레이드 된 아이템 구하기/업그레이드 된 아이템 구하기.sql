-- 코드를 작성해주세요
/*
ROOT 아이템 : PARENT 아이템이 없는 아이템

A에서 C가 될 수 있으면 A가 PARENT 아이템

ROOT
 A -> B -> D
        -> E
 A -> C

<목표>
- 희귀도가 'RARE' 인 아이템들의
- 다음 업그레이드 아이템 : ITEM_TREE.PARENT_ITEM_ID에 ITEM_ID가 있어야한다.

ITEM_D ITEM_E는 더이상 업그레이드가 가능하지 않다.
*/

# T.PARENT_ITEM_ID의 RARITY가 RARE인 것


SELECT
    II.ITEM_ID,
    ITEM_NAME,
    RARITY
FROM

((SELECT 
    ITEM_ID
FROM
    ITEM_TREE
WHERE
    PARENT_ITEM_ID IS NOT NULL AND
    PARENT_ITEM_ID IN 
                    (SELECT ITEM_ID FROM ITEM_INFO WHERE RARITY = 'RARE')) II

JOIN
    ITEM_INFO I ON I.ITEM_ID = II.ITEM_ID)
    
ORDER BY
    ITEM_ID DESC;
