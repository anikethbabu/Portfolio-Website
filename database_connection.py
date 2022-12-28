import mysql.connector
def connect_to_data():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="RESTAURANT",
    port = 3307
    )

    mycursor = mydb.cursor()

    

    mycursor.execute("SELECT * FROM FOOD_CATEGORY")

    myresult = mycursor.fetchall()
    
    return myresult

def connect_to_data2(categoryid):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="RESTAURANT",
    port = 3307
    )

    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT * FROM DISH WHERE category_id = {};".format(categoryid))

    myresult = mycursor.fetchall()
    
    return myresult
    