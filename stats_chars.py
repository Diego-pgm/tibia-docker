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

def insert_stats(stats):
   values = []
   for stat in stats:
      res = input('Insert {}: '.format(stat))
      values.append(res)
   return values 

def insert_char(stats, values, mydb, cursor):
   stat = ''
   val = ''
   val = ', '.join(['%s'] * len(values))
   stat = ', '.join(stat)
   insert_query = ''' INSERT INTO characters (%s) values (%s)'''%(stat, val)
   cursor.execute(insert_query, values)
   mydb.commit()
   print('[+] Char stats added correctly!')

def get_chars(mydb, cursor):
   cursor.execute('select * from characters')
   result = cursor.fetchall()
   return result

stats = ["first_name", "shielding", "magic_level", "sword", "axe", "distance"]
values = insert_stats(stats)
print(values)
mydb, cursor = connection('localhost', 'tibia', 'tibia123', 'tibia', '3309')
insert_char(stats, values, mydb, cursor)
result = get_chars(mydb, cursor)
print(result)

#cursor.execute('show create table characters')
#resultado = cursor.fetchall()
#print(resultado)
