# Write your MySQL query statement below
select round(avg(order_date = Customer_pref_delivery_date)* 100, 2) as immediate_percentage
from Delivery
where (customer_id, order_date) in (
    Select Customer_id, min(order_date)
    from Delivery
    group by customer_id
);