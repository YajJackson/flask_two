import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor() # responsible for executing queries

create_table = "CREATE TABLE users (id int, username text, password text)" # schema
cursor.execute(create_table)

user = (1, 'jay', 'pass', )
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
  (2, 'rolf', 'asdf'),
  (3, 'anne', 'adsf')
]
cursor.executemany(insert_query, users)

connection.commit()
connection.close()
