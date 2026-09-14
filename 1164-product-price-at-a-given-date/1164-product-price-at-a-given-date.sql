select t.product_id, coalesce(p.new_price,10) as price from 
(select distinct product_id from Products) t left join Products p
on t.product_id = p.product_id and p.change_date = (select max(change_date) from Products where change_date<= '2019-08-16' and product_id = p.product_id);
