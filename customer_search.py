from database_insert import engine, Customers
from sqlalchemy import select
from sqlalchemy.orm import Session
session = Session(engine, future=True)
test = select(Customers).all()
new = session.execute(test).all()
print(new)