import pymysql

conn = None

def connect():
global conn
conn = pymysql.connect(host=”localhost”, user=”root”, password=”root”, db=”school”, cursorclass = pymysql.cursors.DictCursor)

def option1(number):
print(“In function”, number)

