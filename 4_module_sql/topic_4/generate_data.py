from faker import Faker
import psycopg2
import random
from datetime import datetime, timedelta

fake = Faker()

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="internat11",
    database="python17"
)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE new_users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50),
        email VARCHAR(100),
        created_at TIMESTAMP
    );
""")

for _ in range(100):
    username = fake.user_name()
    email = fake.email()
    created_at = fake.date_time_this_decade(before_now=True, after_now=False)
    
    cursor.execute("""
        INSERT INTO new_users (username, email, created_at)
        VALUES (%s, %s, %s);
    """, (username, email, created_at))

conn.commit()
cursor.close()
conn.close()

