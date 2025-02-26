-- Write your PostgreSQL query statement below
select product_id
    , product_name
    , description
from products
where description ~ 'SN\d{4}-\d{4}(?=\s|$)'
order by product_id 
