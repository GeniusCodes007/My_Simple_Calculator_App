import sqlite3 as sql3

app_conn = sql3.connect("history_database.db")

app_conn_cursor= app_conn.cursor()

