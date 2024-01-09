import mysql.connector

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

def disconnect(mydb):
    return mydb.close()


mydb = connect()
select = select(mydb, '*', 'user', 'username = %s', ('JeanDamequirie',))

for x in select:
    print(x[1])

disconnect(mydb)


