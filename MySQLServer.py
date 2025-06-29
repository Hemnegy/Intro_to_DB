import mysql.connector
from mysql.connector import Error

def create_database():
    """Creates the alxbookstore database if it doesn't exist"""
    try:
        # Connect to MySQL server without specifying a database
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',  # Replace with your actual username
            password='your_password'  # Replace with your actual password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database with exact name 'alxbookstore' (no underscore)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
            print("Database 'alxbookstore' created successfully!")

    except Error as e:
        print(f"Error: Could not connect to the MySQL server.\n{e}")
    
    finally:
        # Clean up resources
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()