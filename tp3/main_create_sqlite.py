import sqlite3
conn = sqlite3.connect('todos.db')
c = conn.cursor()
c.execute('''
                CREATE TABLE todos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    title varchar(20) NOT NULL,
                    dueDate INTEGER,
                    completed BOOLEAN
                    )
                    ''')

# Insert a row of data
# c.execute("INSERT INTO todos VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

insert_todo = 'INSERT INTO todos (title,dueDate,completed) VALUES ("une todo",1582620058000,1)'
c.execute(insert_todo)

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()