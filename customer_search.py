from config import engine, session
from database_insert import Customers, Sales_Transaction
from datetime import date

t2 = session.query(Customers.customer_id, Customers.customer_first_name).all()
for x, y in t2:
    print(x, y)
start_dt = date(2021, 4, 4)
end_dt = date(2021, 4, 7)
print(start_dt)
sq = session.query(Sales_Transaction.transaction_id, Sales_Transaction.customer_id,
                   Sales_Transaction.transaction_price,
                   Sales_Transaction.transaction_date,Customers.customer_first_name,
                   Customers.phone_number).\
    join(Customers)

for a, b, c, d, e, f in sq.filter(Sales_Transaction.transaction_price > 1200) \
        .filter(Sales_Transaction.transaction_date >= start_dt) \
        .filter(Sales_Transaction.transaction_date <= end_dt):
    print(a, b, c, d, e, f)
