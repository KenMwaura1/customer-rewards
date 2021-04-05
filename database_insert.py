from sqlalchemy import Column, Integer, String, Unicode, ForeignKey, DateTime
import sqlalchemy as sa
from sqlalchemy.orm import Session
import datetime as dt
from sqlalchemy_utils import PhoneNumber

import os
from dotenv import load_dotenv
from config import engine, meta, Base
load_dotenv()
# get the environment values from the .env file

at_username = os.getenv('at_username')
at_api_key = os.getenv('at_api_key')
)


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

s = Session(engine, future=True)

temp = Customers(phone_number=PhoneNumber('0719702373', 'KE'))
c1 = Customers(customer_id=9, customer_first_name='amos',
               customer_last_name='mwaura', _phonenumber=temp.phone_number.e164)
c2 = Customers(customer_id=10, customer_first_name='amy',
               customer_last_name='mwaura',
               _phonenumber=temp.phone_number.e164)
s2 = Sales_Transaction(customer_id=c1.customer_id,
                       transaction_price=2700, transaction_date=dt.datetime.utcnow())
s.add(c1)
s.add(c2)
s.add(s2)
s.commit()
s.close()
