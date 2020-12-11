import tkinter as tk
from tkinter import ttk
from Todo import Todo
from TodoDAO import TodoDAO


class Application(tk.Frame):
    
    def __init__(self, master=None,db=None):
        super().__init__(master)
        self.master = master
        self._dao = TodoDAO(db)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.name = tk.Entry(self)
        self.name.pack(side="top")

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "SayHello"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        
        self.tree = ttk.Treeview(self,column=('title','dueDate','completed'))
        self.tree.heading("title", text="Title")
        self.tree.heading("dueDate", text="dueDate")
        self.tree.heading("completed", text="Completed")
        self.tree.pack(side="top")

        self.btn_load_todos = tk.Button(self)
        self.btn_load_todos["text"] = "Load"
        self.btn_load_todos["command"] = self.load_todos
        self.btn_load_todos.pack(side="top")


        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)
        self.quit.pack(side="bottom")

    def load_todos(self):
        todos = self.dao.findAll()
        for i,todo in enumerate(todos):
            self.tree.insert("", tk.END,values=[todo.title,todo.dueDate,todo.completed])

    def say_hi(self):
        self.tree.insert("", tk.END, values=['1','todo','True'])
        print(f"hi {self.name.get()}")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1024x768")
    app = Application(master=root,db="todos.db")
    app.mainloop()