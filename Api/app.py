from Database import execute_query

def get_posts():
    query = "SELECT * FROM posts"
    return execute_query(query)

def create_post(title: str, description: str):
    query = f"INSERT INTO posts(title, description) VALUES ('{title}', '{description}')"
    print(execute_query(query))

def get_post_with_id(id: int):
    query = f"SELECT * FROM posts WHERE id={id}"
    return execute_query(query)
