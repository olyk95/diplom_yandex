select c.login, count(o.id) as "orders in delivery"
from "Couriers" c
join "Orders" o on o."courierId" = c.id
where o."inDelivery" is True
group by c.login;
