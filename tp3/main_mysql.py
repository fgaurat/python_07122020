from urllib.request import urlopen
import requests
from pprint import pprint
import mysql.connector
import configparser
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('conf')
    args = parser.parse_args()
    print(args.conf)
    
    conf = configparser.ConfigParser()
    conf.read(args.conf)
   
    rest_url = conf['API']['url']
    response = requests.get(rest_url)
    d = response.json()

    mysql_dict = conf['MYSQL']
    
    cnx = mysql.connector.connect(**mysql_dict)
    cursor = cnx.cursor()
    
    insert_todo = 'INSERT INTO todos (title,dueDate,completed) VALUES (%s,%s,%s)'
    
    # REST
    # for todo in d['records']:
    #     data = todo['fields']
    #     completed = True if "completed" in data else False
    #     values_todo = (data['title'],data['dueDate'],completed)
    #     cursor.execute(insert_todo, values_todo)

    # CSV
    with open('todos.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile,delimiter=';')
        for row in reader:
            pprint(row)

            
    cnx.commit()
    cursor.close()
    cnx.close()

if __name__ == "__main__":
    main()


