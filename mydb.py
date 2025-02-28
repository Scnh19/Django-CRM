import mysql.connector

dataBase = mysql.connector.connect(
  host = '192.168.50.32',
  user = 'remoteroot',
  passwd = 'password'
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE perry")

print("All Done!")
