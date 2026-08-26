select 
    t.request_at as Day,
    ROUND(
        SUM(case
                when t.status <> 'completed' THEN 1
                ELSE 0
                END) / count(*),
            2
    ) AS `Cancellation Rate`
FROM Trips t
join Users c
    on t.client_id = c.users_id
join Users d
    on t.driver_id = d.users_id
where c.banned = 'No'
    and d.banned = 'No'
    and t.request_at between '2013-10-01' and '2013-10-03'
group by t.request_at;