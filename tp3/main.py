from Todo import Todo
from TodoDAO import TodoDAO
import configparser
import argparse

# python main.py conf.ini
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('conf')
    args = parser.parse_args()

    conf = configparser.ConfigParser()
    conf.read(args.conf) # args.conf = conf.ini

    todoDAO = TodoDAO(conf['SQLITE']['file'])
    
    todo = Todo(title="Le titre",completed=False,dueDate=1231456)
    print(todo) # "Todo : title="Le titre",completed=False,dueDate=1231456"

    todoDAO.save(todo) # => 

    todos = todoDAO.findAll()
    
    for todo in todos:
        print(todo)

if __name__ == "__main__":
    main()


