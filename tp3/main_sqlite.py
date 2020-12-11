from urllib.request import urlopen
import requests
from pprint import pprint
import mysql.connector
import configparser
import argparse
import sqlite3
import csv
from bs4 import BeautifulSoup
from pathlib import Path

# pip install requests
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

    sqlite_dict = conf['SQLITE']

    conn = sqlite3.connect(sqlite_dict['file'])
    c = conn.cursor()

    # REST
    # for todo in d['records']:
    #     data = todo['fields']
    #     completed = True if "completed" in data else False
    #     c.execute(f"INSERT INTO todos (title,dueDate,completed) VALUES ('{data['title']}',{data['dueDate']},{completed})")
    #     conn.commit()

    # CSV
    # with open('todos.csv', newline='') as csvfile:
    #     reader = csv.DictReader(csvfile,delimiter=';')
    #     for row in reader:
    #         print(row['title'])
    #         c.execute(f"INSERT INTO todos (title,dueDate,completed) VALUES ('{row['title']}',{row['dueDate']},{completed})")
    #         conn.commit()

    # HTML
    # response = requests.get("http://db.eolem.com/")
    # html = response.text
    from pathlib import Path
    html = Path('index.html').read_text()

    soup = BeautifulSoup(html, 'html.parser')
    print(soup.title.text)
    
    lines = soup.select('body > div > table > tbody > tr')
    # lines = soup.find_all('tr')
    data = []
    for tr in lines:
        cols = tr.find_all('td')
        chk = cols[3].find("input")
        todo = {
            'title': cols[1].text,
            'completed': True if 'checked="true"' in str(chk) else False,
            'dueDate': cols[2].text
        }
        data.append(todo)
    
    pprint(data)

    # for row in c.execute("SELECT * FROM todos"):
    #     print(row)

    conn.close()


if __name__ == "__main__":
    main()
