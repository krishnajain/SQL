import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='DATABASE',
                                         user='USER',
                                         password='PASS')

    sql_select_Query = "select * from add1"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[2])
        print("Address  = ", row[3])
        print("City  = ", row[4], "\n")

except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")
