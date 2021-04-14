from config import session
from database_insert import Customers, Sales_Transaction
from datetime import date


class CustomerQuery:
    def customer_query():
        start_dt = date(2021, 4, 12)
        end_dt = date(2021, 4, 19)
        print(start_dt)
        sq = session.query(
            Sales_Transaction.transaction_price, Customers.customer_first_name,
            Customers.customer_last_name, Customers.phone_number). \
            join(Customers)
        customer_data = []
        for a, b, c, d in sq.filter(Sales_Transaction.transaction_price > 3000) \
                .filter(Sales_Transaction.transaction_date >= start_dt) \
                .filter(Sales_Transaction.transaction_date <= end_dt):
            cl = [a, b, c, d.e164]

            customer_data.extend([cl])
            # print(cl)
        # print(customer_data)

        return customer_data

print(CustomerQuery.customer_query())
