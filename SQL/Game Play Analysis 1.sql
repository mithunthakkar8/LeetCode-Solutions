with login_dates as (
select player_id
    , event_date
    , row_number() over (partition by player_id order by event_date) rnk
from activity)
select player_id
    , event_date first_login
from login_dates
where rnk = 1
