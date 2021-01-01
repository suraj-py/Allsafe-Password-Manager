import psycopg2
import os

# Create connection to the database
def connect():
    try:
        conn = psycopg2.connect(
            host = 'localhost',
            database = 'password_manager',
            user = os.environ.get('DB_USER'),
            password = os.environ.get('DB_PASS')
        )
        return conn
    except (Exception, psycopg2.Error) as error:
        print(error)

# Adding user details to the database
def storePassword(allsafe_username, app_name, email, username, password):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_insert_qurey = """INSERT INTO allpasswords (allsafe_username, app_name, email, username, password) VALUES (%s, %s, %s, %s, %s)"""
        record_to_insert = (allsafe_username, app_name, email, username, password)
        cursor.execute(postgres_insert_qurey, record_to_insert)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)

# Retrieving password
def getPassword(app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_insert_qurey = """ SELECT password FROM allpasswords WHERE app_name = '""" + app_name + "'" #"""SELECT password FROM allpasswords WHERE app_name=(%s)"""
        record_to_insert = (app_name)
        cursor.execute(postgres_insert_qurey, record_to_insert)
        connection.commit()
        result = cursor.fetchone()[0]
        return result

    except (Exception, psycopg2.Error) as error:
        print(error)

# Retrieving all app detail's of a specific user
def getUserDetails(allsafe_username):

    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_insert_qurey = """ SELECT * FROM allpasswords WHERE allsafe_username = '""" + allsafe_username + "'" #"""SELECT password FROM allpasswords WHERE app_name=(%s)"""
        record_to_insert = (allsafe_username)
        cursor.execute(postgres_insert_qurey, record_to_insert)
        connection.commit()
        details = cursor.fetchall()
        return details

    except (Exception, psycopg2.Error) as error:
        print(error)

