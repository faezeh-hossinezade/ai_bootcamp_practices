
-- Section1

update staff set password = 'dd8017260fe27d5900c150cae019650932' where password is null;

-- Section2

select 
    concat(c.first_name, ' ', c.last_name) as name, 
    count(r.rental_id) as count 
from customer c
join rental r on r.customer_id = c.customer_id 
join inventory i on r.inventory_id = i.inventory_id 
join film f on i.film_id = f.film_id 
where
    (
        (datediff(r.return_date, r.rental_date) > f.rental_duration)
        and
        (r.rental_date is not null)
        and
        (r.return_date is not null)
    )
group by c.customer_id
order by count desc, name asc 
limit 10;

-- Section3

select 
    concat(a1.first_name, ' ', a1.last_name) as actor1,
    concat(a2.first_name, ' ', a2.last_name) as actor2,
    count(*) as film_count
from film_actor fa1
join film_actor fa2 on fa1.film_id = fa2.film_id and fa1.actor_id < fa2.actor_id
join actor a1 on a1.actor_id = fa1.actor_id
join actor a2 on a2.actor_id = fa2.actor_id
group by a1.actor_id, a2.actor_id
order by film_count desc, actor1 asc
limit 10;

-- Section4

select
    concat(c.first_name, ' ', c.last_name) as customer_name,
    min(r.rental_date) as first_rental_date,
    max(r.rental_date) as last_rental_date,
    (count(r.rental_id) / (datediff(max(r.rental_date), min(r.rental_date)) + 1)) as loyalty_score
from customer c
join rental r on r.customer_id = c.customer_id
where r.rental_date is not null
group by c.customer_id
order by loyalty_score desc, customer_name asc
limit 50;

-- Section5

select * from (select
    concat(a.first_name, ' ', a.last_name) as name,
    count(fa.film_id) as count
from actor a
join film_actor fa on a.actor_id = fa.actor_id
group by a.actor_id) as most_actors
where count > 10
order by count desc, name asc;

-- Section6

select
    store_id,
    title,
    total_sales,
    rank_in_store
from (
    select
        s.store_id,
        f.title,
        sum(p.amount) as total_sales,
        dense_rank() over (partition by s.store_id order by sum(p.amount) desc, f.title) as rank_in_store
    from store s
    join inventory i on i.store_id = s.store_id
    join rental r on i.inventory_id = r.inventory_id
    join payment p on p.rental_id = r.rental_id
    join film f on f.film_id = i.film_id
    group by s.store_id, f.title
) as store_film_sales
where rank_in_store < 11
order by store_id, total_sales desc;
