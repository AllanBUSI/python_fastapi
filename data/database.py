import mysql.connector
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools import hash




def connect():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="tests",
        password=""
    )

    if mydb.is_connected():
        return mydb
    else:
        print("Échec de la connexion à la base de données.")

def select(mydb, champs, table, where, param):
    sql = 'SELECT '+champs+' FROM '+table+" "
    if (where != ''):
        sql += "WHERE "+where
        print(sql)
        mydb = mydb.cursor()
        mydb.execute(sql, param)
        myresult = mydb.fetchall()
        return myresult
    
    mydb = mydb.cursor()
    mydb.execute(sql, param)
    myresult = mydb.fetchall()
    return myresult

def insert(mydb,tables,  champs,params, values):
    sql = "INSERT INTO "+tables+" ("+champs+") VALUES "+params+";"
    mydbs = mydb.cursor()
    mydbs.execute(sql, values)
    mydb.commit()
    return
    
def disconnect(mydb):
    return mydb.close()



