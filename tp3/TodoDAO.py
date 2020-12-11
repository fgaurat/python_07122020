import sqlite3
from Todo import Todo
class TodoDAO:

    def __init__(self,db):
        self._conn = sqlite3.connect(db)

    def save(self,todo):
        c = self._conn.cursor()
        c.execute(f"INSERT INTO todos (title,dueDate,completed) VALUES ('{todo.title}',{todo.dueDate},{todo.completed})")
        self._conn.commit()


    def findAll(self):
        todos = []
        c = self._conn.cursor()
        for row in c.execute("SELECT * FROM todos"):
            todo = Todo(title=row[1],completed=row[3],dueDate=row[2])
            todos.append(todo)

        return todos


    def __del__(self):
        self._conn.close()

