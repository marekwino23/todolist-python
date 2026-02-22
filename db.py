# db.py
import mysql.connector

db_config = {
    "host": "mn14.webd.pl",
    "user": "vidad_todolist",
    "password": "Todo2026@",
    "database": "vidad_todolist"
}

def add_task(name):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = "INSERT INTO tasks (name) VALUES (%s)"
    cursor.execute(sql, (name, ))
    conn.commit()
    cursor.close()
    conn.close()

def get_tasks():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return tasks