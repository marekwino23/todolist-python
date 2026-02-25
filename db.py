# db.py
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

def get_connection():
    return mysql.connector.connect(**db_config)

def add_task(name: str):
     with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO tasks (name) VALUES (%s)", (name,))
        conn.commit()
        return cursor.lastrowid

def delete_task(id: int):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM tasks where id=%s", (id, ))
        conn.commit()

def change_status_tasks(status: int, id: int):
   with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE tasks set done = %s where id=%s", (status, id ))
        conn.commit()

def get_tasks():
     with get_connection() as conn:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM tasks")
            tasks = cursor.fetchall()
        conn.commit()
        return tasks