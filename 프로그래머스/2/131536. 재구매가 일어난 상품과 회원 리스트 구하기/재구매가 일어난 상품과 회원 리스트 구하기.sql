-- 코드를 입력하세요
-- 재구매 -> 같은 사람 / 같은 제품 -> GROUP BY 하고


SELECT 
    USER_ID,
    PRODUCT_ID
FROM
    ONLINE_SALE
GROUP BY
    USER_ID,
    PRODUCT_ID
HAVING COUNT(*) >= 2 # 같은(USER_ID, PRODUCT_ID) 조합이 2개 이상
ORDER BY USER_ID ASC, PRODUCT_ID DESC;

