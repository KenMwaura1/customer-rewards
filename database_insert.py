from sqlalchemy import Column, Integer, String, Unicode, ForeignKey, DateTime
import sqlalchemy as sa
from sqlalchemy_utils import PhoneNumber
import datetime as dt
import os
from dotenv import load_dotenv
from config import engine, Base, session

load_dotenv()
# get the environment values from the .env file
phone_number = os.getenv('phone_number')


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
c1 = Customers(customer_id=2, customer_first_name='ken',
               customer_last_name='mwaura', _phonenumber=temp.phone_number.e164)
c2 = Customers(customer_id=3, customer_first_name='zoo',
               customer_last_name='mwaura',
               _phonenumber=temp.phone_number.e164)
s2 = Sales_Transaction(customer_id=c1.customer_id,
                       transaction_price=5000, transaction_date=dt.date(2021, 4, 10))
s3 = Sales_Transaction(customer_id=c2.customer_id, transaction_price=2500,
                       transaction_date=dt.date(2021, 4, 10))
""" 
s.add(c1)
s.add(c2)
s.add(s2)
s.commit()
s.close()
"""

session.add_all([s2, s3])
session.commit()
session.close()
