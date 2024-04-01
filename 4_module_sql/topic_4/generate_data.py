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
        role_name VARCHAR(30),
        created_at TIMESTAMP
    );
""")

roles = ["admin", "moderator", "web_app_user", "guest"]

for _ in range(100):
    username = fake.user_name()
    # first_name = fake.first_name()
    email = fake.email()
    created_at = fake.date_time_this_decade(before_now=True, after_now=False)
    random_role = random.choice(roles)
    
    cursor.execute("""
        INSERT INTO new_users (username, email, created_at, role_name)
        VALUES (%s, %s, %s, %s);
    """, (username, email, created_at, random_role))

conn.commit()
cursor.close()
conn.close()

