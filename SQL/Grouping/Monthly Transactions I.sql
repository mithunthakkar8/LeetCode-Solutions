-- Write your PostgreSQL query statement below
with monthwise_transaction_details as (
select TO_CHAR(trans_date, 'YYYY-MM') as month
    , country
    , count(*) as trans_count
    , sum(amount) as trans_total_amount
from transactions
group by TO_CHAR(trans_date, 'YYYY-MM'), country),
approved_transactions as (
select TO_CHAR(trans_date, 'YYYY-MM') as month
    , country
    , count(*) as approved_count
    , sum(amount) as approved_total_amount
from transactions
where state = 'approved'
group by TO_CHAR(trans_date, 'YYYY-MM'), country
)
select mtd.month
    , mtd.country
    , trans_count
    , coalesce(approved_count,0) as approved_count
    , trans_total_amount
    , coalesce(approved_total_amount,0) as approved_total_amount
from monthwise_transaction_details mtd
left join approved_transactions at_
on mtd.month = at_.month 
and (mtd.country = at_.country or mtd.country is null and at_.country is null)
