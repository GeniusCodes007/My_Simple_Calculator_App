from in_app_database.create_database import app_conn, app_conn_cursor

# ADD TO HISTORY
def add_to_history(statement:str, result:str):
    app_conn_cursor.execute("""
    INSERT INTO calc_history (statement, result) VALUES (?, ?)""",
                            (statement, result))
    app_conn.commit()

# DELETE ALL HISTORY
def delete_all_history():
    app_conn_cursor.execute("""
    DELETE FROM calc_history""")
    app_conn.commit()

# GET ALL HISTORY
def get_all_history():
    all_data =app_conn_cursor.execute("""
    SELECT * FROM calc_history
    """)
    return all_data.fetchall()