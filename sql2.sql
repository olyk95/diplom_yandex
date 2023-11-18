
select
    track,
    case
        when finished = True then 2
        when cancelled = True then -1
        when "inDelivery" = True then 1
        else 0
    end as status
from "Orders";
