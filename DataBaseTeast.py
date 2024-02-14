# import sqlite3
# db = sqlite3.connect("app.db")

# cr = db.cursor()

# craete the table 
# cr.execute(
#     "CREATE TABLE IF NOT EXISTS users(user_id intager, name text) "
#     )
# cr.execute(
#     "CREATE TABLE IF NOT EXISTS skills (name text, progress integer, user_id)"
# )

#inesrting Date 
"""
cr.execute("insert into users(user_id, name)values(1, 'Ahmed')")
cr.execute("insert into users(user_id, name)values(2, 'Sayed')")
cr.execute("insert into users(user_id, name)values(3, 'Osama')")
"""
#input_users= ["Ahmed","Mahmoud","Ebrahim","Sayed","Salah"]
"""
for key ,user in enumerate(input_users):
    cr.execute(f"INSERT INTO users(user_id,name) values({key+1},'{user}')")
"""
#Update
# cr.execute("update users set name = 'Gamal' where user_id=1")
#Delete
# cr.execute("delete from users where user_id=4")
# cr.execute("delete from users where user_id=3")
# #fetch(Display)
# cr.execute("select * from users")
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())

#save (commit) Changes
# db.commit()
# db.close()

import sqlite3

def get_all_data():
    try:
        # Connect To Database
        db = sqlite3.connect("app.db")

        # Setting Up The Cursor
        cr = db.cursor()


        # Commit Changes
        db.commit()

        # Fetch Data
        cr.execute("select * from users")
        results = cr.fetchall()

        # Print Number Of Rows
        print(f"Database Has {len(results)} Rows.")

        # Loop On Results
        for row in results:
            print(f"UserId => {row[0]}" ,end=" ")
            print(f"UserName => {row[1]}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the database connection
        db.close()

# Call the function
# get_all_data()
 
