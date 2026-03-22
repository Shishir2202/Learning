from db import engine
from Tables_c import users
from sqlalchemy import insert

def create_user(input_name,input_email):
    with engine.connect() as conn:
        query2 = insert(users).values(name=input_name,email=input_email)
        conn.execute(query2)
        conn.commit()

 