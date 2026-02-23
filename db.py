# db.py
import mysql.connector

db_config = {
    "host": "mn14.webd.pl",
    "user": "vidad_todolist",
    "password": "Todo2026@",
    "database": "vidad_todolist"
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