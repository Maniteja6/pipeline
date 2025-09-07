import pandas as pd
from datetime import datetime, timedelta
import random

# Generating Orders
Orders = pd.DataFrame({
    'order_id': [f'O{i}' for i in range(1,21)],
    'customer_id': [f'C{random.randint(1,5)}' for _ in range(20)],
    'order_date': pd.date_range(start='2024-01-01', periods=20, freq='D')
})
Orders.to_csv('orders.csv', index=False)

#Generating Customers

Customers = pd.DataFrame({
    'customer_id': [f'C{i}' for i in range(1,6)],
    'name': ['Raju', 'Raghu', 'Prabhas', 'Johnson', 'Kalyan'],
    'email': [f'user{i}@example.com' for i in range(1,6)]
})
Customers.to_csv('customers.csv', index=False)


# Generating Shipments

