import sqlite3

# Connect to Database
db = sqlite3.connect("app2.db")
cr = db.cursor()

# User Id
uid = 2


# Commit and Close Connection
def commit_and_close():
    db.commit()
    db.close()
    print("Connection to Database is Closed")

# List Message
input_message = """
What do you want to do?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option:
"""

# Input Option Choose
user_input = input(input_message).strip().lower()

# Command List
command_list = ["s", "a", "d", "u", "q"]

# Define The Methods
def show_skills():
    cr.execute(f"SELECT * FROM skills  WHERE user_id='{uid}'")
    results = cr.fetchall()
    print(f"You Have {len(results)}  Skills In Your Profile:\n")
    for row in results:
        print(f"Skills: '{row[0]}'\t Progress: '{row[1]}%'")
    commit_and_close()

def add_skills():
    
    #If Table Not Exists
    cr.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")
    
    skill_name = input("Write Skill Name: ").strip().capitalize()
    prog = input("Write Skill Progress: ").strip()

 # Use parameterized query to prevent SQL injection
    cr.execute("INSERT INTO skills (name, progress, user_id) VALUES (?, ?, ?)", (skill_name, prog, uid))
    commit_and_close()

def delete_skills():
    skill_name = input("Write Skill Name: ").strip().capitalize()
    cr.execute(f"DELETE FROM skills where name = '{skill_name}' and user_id = '{uid}'")
    commit_and_close()

def update_skills():
    skill_name = input("Write Skill Name: ").strip().capitalize()
    prog = input("Write Skill Progress: ").strip()

    cr.execute(
        f"update skills set progress = '{prog}' where name = '{skill_name}' and user_id = '{uid}'")
    commit_and_close()

def quit_app():
    print("Goodbye!")
    commit_and_close()
    exit()

# Check If Command Is Exists
if user_input in command_list:
    if user_input == "s":
        show_skills()
    elif user_input == "a":
        add_skills()
    elif user_input == "u":
        update_skills()
    elif user_input == "d":
        delete_skills()
    else:
        quit_app()
else:
    print(f"This Command \"{user_input}\" Not Found")
