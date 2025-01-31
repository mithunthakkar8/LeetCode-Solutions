-- Write your PostgreSQL query statement below
WITH login_dates as (
    SELECT player_id
           , event_date
           , LAG(event_date) OVER (PARTITION BY player_id ORDER BY event_date) AS lag_event_date
           , row_number() OVER (PARTITION BY player_id ORDER BY event_date) AS rank
    FROM activity
)
SELECT ROUND(
    CAST(
        COUNT(DISTINCT CASE 
            WHEN lag_event_date+1 = event_date
                and rank=2 THEN player_id 
        END) AS DECIMAL(8,2)
    ) / COUNT(DISTINCT player_id), 2) AS fraction
FROM login_dates

