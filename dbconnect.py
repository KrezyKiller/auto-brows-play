import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              auth_plugin='mysql_native_password',
                              database='employee')
print(cnx)
cnx.close()
