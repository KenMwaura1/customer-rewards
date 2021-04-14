from sqlalchemy import Column, Integer, String, Unicode, ForeignKey, DateTime
import sqlalchemy as sa
from sqlalchemy_utils import PhoneNumber
import datetime as dt

from config import engine, Base, session

phone_number = '0729450130'


class Customers(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True)
    customer_first_name = Column(String)
    customer_last_name = Column(String)
    _phonenumber = Column(Unicode(20))
    country_code = Column(Unicode(8))
    phone_number = sa.orm.composite(
        PhoneNumber, _phonenumber, country_code
    )


class Sales_Transaction(Base):
    __tablename__ = 'sales_transaction'
    transaction_id = Column(Integer, autoincrement=True, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    transaction_price = Column(Integer)
    transaction_date = Column(DateTime(timezone='EAT'))


Base.metadata.create_all(engine)

temp = Customers(phone_number=PhoneNumber(f'{phone_number}', 'KE'))
c1 = Customers(customer_id=43, customer_first_name='ken',
               customer_last_name='mwaura', _phonenumber=temp.phone_number.e164)
c2 = Customers(customer_id=37, customer_first_name='babygirl',
               customer_last_name='nyambura',
               _phonenumber=temp.phone_number.e164)
s2 = Sales_Transaction(customer_id=c1.customer_id,
                       transaction_price=3850, transaction_date=dt.date(2021, 4, 10))
s3 = Sales_Transaction(customer_id=c2.customer_id, transaction_price=7000,
                       transaction_date=dt.date(2021, 4, 18))
try:
    session.add_all([c1, c2,])
    session.add_all([s2, s3])
    session.commit()
    session.close()
except Exception as e:
    print(f"Exception occurred: {e}")
