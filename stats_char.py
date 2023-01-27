import mysql.connector
import subprocess

m = '''
   ======================== Tibia Char Stats =======================\n\
   1) Get Chars
   2) Insert Characters
   x) Exit
'''

def menu(m, flag):
   print(m)
   option = str(input('> '))
   if option == 'x':
      print('[-] Goodbye!')
      flag = False
   subprocess.call('clear')
   return option, flag

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

def insert_char(stats, mydb, cursor):
   values = insert_stats(stats)
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

mydb, cursor = connection('192.168.0.10', 'tibia', 'tibia123', 'tibia', '3309')
stats = ["first_name", "shielding", "magic_level", "sword", "axe", "distance"]

flag = True
while flag:
   opt, flag = menu(m, flag)
   if opt == '1':
      result = get_chars(mydb, cursor)
      print(result)
   elif opt == '2':   
      insert_char(stats, mydb, cursor)


#cursor.execute('show create table characters')
#print(resultado)
