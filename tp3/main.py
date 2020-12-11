from Todo import Todo

def main():
    todoDAO = TodoDAO()
    todo = Todo(title="Le titre",completed=False,dueDate=1231456)
    print(todo) # "Todo : title="Le titre",completed=False,dueDate=1231456"

    todoDAO.save(todo) # => 
    todos = todoDAO.findAll()


if __name__ == "__main__":
    main()


