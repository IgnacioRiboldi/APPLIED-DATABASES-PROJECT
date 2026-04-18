import pymysql

conn = None

def connect():
    global conn
    conn = pymysql.connect(host=”localhost”, user=”root”, password=”root”, db=”school”, cursorclass = pymysql.cursors.DictCursor)

def option1(number):
    if (not conn):
        connect();
        
        query = " SELECT * FROM teacher where experience < %s"
        
    with conn:
        
    
