from config import engine
from database_insert import Customers, Sales_Transaction
from sqlalchemy import select
from sqlalchemy.orm import Session
from datetime import date

session = Session(engine, future=True)
test = select(Customers)
new = session.execute(test).all()
t2 = session.query(Customers.customer_id, Customers.customer_first_name).all()
for x, y in t2:
    print(x, y)
dt = date(2021, 4, 4)
print(dt)
sq = session.query(Sales_Transaction.transaction_id, Sales_Transaction.customer_id,
                   Sales_Transaction.transaction_price, Sales_Transaction.transaction_date)
for a, b, c, d in sq.filter(Sales_Transaction.transaction_price > 1200)\
        .filter(Sales_Transaction.transaction_date > dt ):
    print(a, b, c, d)
