from fastapi import FastAPI
import psycopg2

app = FastAPI()


try:
    connection = psycopg2.connect(user="postgres",
                                  password="1234",
                                  host="localhost",
                                  port="5432",
                                  database="postgres")
    cursor = connection.cursor()

    postgres_insert_query = """ INSERT INTO login_tabel1 (user_id, username,password) VALUES (%s,%s,%s)"""
    record_to_insert = (5,950, 950)
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print(count, "data ok")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into mobile table", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")