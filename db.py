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

def delete_task(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (id ,))
    conn.commit()
    cursor.close()
    conn.close()

def change_status_tasks(status, id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks set done = %s where id=%s", (status, id ))
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