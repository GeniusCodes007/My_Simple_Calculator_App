
from in_app_database.create_database import app_conn_cursor, app_conn




app_conn_cursor.execute("""
CREATE TABLE IF NOT EXISTS calc_history (
statement TEXT NOT NULL,
result TEXT NOT NULL
)"""
                        )

#app_conn_cursor.execute("""
#                        CREATE TABLE IF NOT EXISTS ui_satate (

app_conn.commit()
