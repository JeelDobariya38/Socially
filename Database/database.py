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
    queries = [
    "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255) UNIQUE, password VARCHAR(500), bio TEXT, location VARCHAR(255), other_details TEXT)",
    
    "CREATE TABLE IF NOT EXISTS posts (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255) NOT NULL, description VARCHAR(500), published_by INT, FOREIGN KEY (published_by) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE)",
    
    "CREATE TABLE IF NOT EXISTS comments (id INT AUTO_INCREMENT PRIMARY KEY, post_id INT, user_id INT, comment_text VARCHAR(500), FOREIGN KEY (post_id) REFERENCES posts(id) ON UPDATE CASCADE ON DELETE CASCADE, FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE)",
    
    "CREATE TABLE IF NOT EXISTS likes (id INT AUTO_INCREMENT PRIMARY KEY, post_id INT, user_id INT, FOREIGN KEY (post_id) REFERENCES posts(id) ON UPDATE CASCADE ON DELETE CASCADE, FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE)",
    
    "CREATE TABLE IF NOT EXISTS followers (id INT AUTO_INCREMENT PRIMARY KEY, follower_id INT, following_id INT, FOREIGN KEY (follower_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE, FOREIGN KEY (following_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE)",
    
    "CREATE TABLE IF NOT EXISTS media (media_id INT AUTO_INCREMENT PRIMARY KEY, post_id INT, media_type ENUM('image', 'video'), media_data LONGBLOB, FOREIGN KEY (post_id) REFERENCES posts(id) ON UPDATE CASCADE ON DELETE CASCADE)",
    
    "CREATE TABLE IF NOT EXISTS messages (message_id INT AUTO_INCREMENT PRIMARY KEY, sender_id INT, receiver_id INT, message_text TEXT, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (sender_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE, FOREIGN KEY (receiver_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE)"
    ]

    for query in querys:
        execute_query(query)
