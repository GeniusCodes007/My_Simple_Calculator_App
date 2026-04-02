from in_app_database.create_database import app_conn, app_conn_cursor
#from actions_files.non_numeric_operations.non_numeric_operations_buttons_actions import Answer



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