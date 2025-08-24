import mysql.connector
try: 
   mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "27oCt2004.",
)
   my_cursor = mydb.cursor()
   sql = "CREATE DATABASE IF NOT EXISTS alx_book_store;"
   my_cursor.execute(sql)
   print("Database 'alx_book_store' created successfully!")
   mydb.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")

