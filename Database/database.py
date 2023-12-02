import mysql.connector

from dotenv import dotenv_values

__config =  dotenv_values(".env")


MYSQL_HOSTNAME = __config["MYSQL_HOSTNAME"]
MYSQL_USERNAME = __config["MYSQL_USERNAME"]
MYSQL_PASSWORD = __config["MYSQL_PASSWORD"]


def execute_query(query: str):
    connection = mysql.connector.connect(host=MYSQL_HOSTNAME, 
        user=MYSQL_USERNAME, 
        password=MYSQL_PASSWORD, 
        database="socially")
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return data


def create_database():
    connection = mysql.connector.connect(host=MYSQL_HOSTNAME, user=MYSQL_USERNAME, password=MYSQL_PASSWORD)
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS socially")
    cursor.close()
    connection.close()

def init():
    create_database()
    querys = [
        "CREATE TABLE IF NOT EXISTS posts (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255) NOT NULL, description VARCHAR(500))",
    ]
    for query in querys:
        execute_query(query)
