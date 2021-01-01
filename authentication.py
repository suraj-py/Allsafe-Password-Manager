import psycopg2
import os
from hash_maker import hash_password, get_hash_password, convertTuple

# Creating connection to the database
# change password to env variable
def connect():
    try:
        conn = psycopg2.connect(
            host = 'localhost',
            database = 'authentication',
            user = os.environ.get('DB_USER'),
            password = os.environ.get('DB_PASS')
        )
        return conn
    except (Exception, psycopg2.Error) as error:
        print(error)


# Adding user details to the database
def addMasterPassword(email_id, allsafe_username, master_password):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_insert_qurey = """INSERT INTO authenticate_user (email_id, user_name, master_password) VALUES (%s, %s, %s)"""
        record_to_insert = (email_id, allsafe_username, hash_password(master_password))
        cursor.execute(postgres_insert_qurey, record_to_insert)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)

#Authenticating User
def getHash(email_id, plaintext):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_insert_qurey = """ SELECT master_password FROM authenticate_user WHERE email_id = '""" + email_id + "'"
        record_to_insert = (email_id)
        cursor.execute(postgres_insert_qurey, record_to_insert)
        connection.commit()
        db_passwd = cursor.fetchone() # Retrieving hash password from the database
        hpass = convertTuple(db_passwd) # converting hash password from tuple to string
        if get_hash_password(plaintext, hpass):
            return True
        else:
            return False

    except (Exception, psycopg2.Error) as error:
        print(error)

# Retrieving Allsafe Username
def getAllsafeUsername(user_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_insert_qurey = """ SELECT user_name FROM authenticate_user WHERE user_name = '""" + user_name + "'"
        record_to_insert = (user_name)
        cursor.execute(postgres_insert_qurey, record_to_insert)
        connection.commit()
        result = cursor.fetchall()
        return result

    except (Exception, psycopg2.Error) as error:
        print(error)
