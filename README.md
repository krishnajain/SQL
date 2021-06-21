# SQL

PIP to install "MySQL Connector"



>>Create Connection


Start by creating a connection to the database.

Use the username and password from your MySQL database:

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

print(mydb)
