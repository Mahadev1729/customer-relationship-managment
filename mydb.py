

import mysql.connector 


dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    
)

## prepare cursor

cursorObject=dataBase.cursor()

## create database

cursorObject.execute("CREATE DATABASE elderco")

print("ALL DONE")
