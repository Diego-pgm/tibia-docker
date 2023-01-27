import subprocess
import mysql.connector

def connection(host, user, password, database, port):
   mydb = mysql.connector.connect(
      host=host,
      user=user,
      password=password,
      database=database,
      port=port
   )
   cursor = mydb.cursor()
   if cursor:
      print('[+] Connected to the database!')
   return mydb,cursor

"""
def insert_stats(stats):
   char = {}
   for stat in stats:
      res = input('Insert {}: '.format(stat))
      char[stat] = res
   return char 
"""

stats = ["name", "magic_level", "sword", "axe", "distance", "shielding"]
#char = insert_stats(stats)
#for key,value in char.items():
#   print('{} : {}'.format(key,value))

mydb, cursor = connection('localhost', 'tibia', 'tibia123', 'tibia', '3309')
cursor.execute('show create table characters')
resultado = cursor.fetchall()
print(resultado)
