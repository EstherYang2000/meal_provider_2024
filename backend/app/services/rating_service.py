from datetime import datetime, timezone
import psycopg2
from dotenv import load_dotenv
import os

def get_rating_service(data):
    # data = {"item_id": 'item001'}

    host = os.getenv("DB_HOST")
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    sslmode = "require"
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string)
    print("Connection established")
    cursor = conn.cursor()

    try:
        item_id = data['item_id']

        cursor.execute("SELECT meals_ratings.star_rating FROM meals_ratings WHERE item_id = %s", (item_id,))
        ratings = cursor.fetchall()

        rating = 0.0
        for r in ratings:
            rating += float(r[0])
        
        rating /= len(ratings)

        cursor.close()
        conn.close()
        return ({"item_id": item_id, "rating": str(rating)})
    except Exception as e:
        return ({"error": str(e)}), 500
    
def update_rating_service(data):

    # data= {"user_id": "A0001", "item_id": 'item001', "rating": "4.5"}

    host = os.getenv("DB_HOST")
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    sslmode = "require"
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string)
    print("Connection established")
    cursor = conn.cursor()

    try:
        user_id = data['user_id']
        item_id = data['item_id']
        rating = data['rating']

        current_time = datetime.now(timezone.utc)
        formatted_date = current_time.strftime('%a, %d %b %Y %H:%M:%S GMT')

        cursor.execute("INSERT INTO meals_ratings (user_id, item_id, star_rating, created_at, updated_at) VALUES(%s, %s, %s, %s, %s)", (user_id, item_id, rating, formatted_date, formatted_date))

        cursor.close()
        conn.close()
        return ({"message" : "successfully inserted rating"})
    except Exception as e:
        return ({"error": str(e)}), 500