import psycopg2

try:
   conn = psycopg2.connect("dbname='arts' user='black_eryque' password='CADEnsicloop60'")
except:
   print("CONNECTION FAILED")

#creates a cursor that enables psycopg2 to execute SQL commands
#below i stored my cursor to a cur variabel
#conn is a variable for psycopg2.connect() above
cur = conn.cursor()

try:
   cur.execute("""
   CREATE TABLE Transactions(
      NO SERIAL,
      NAME VARCHAR (20),
      ACCOUNTED INTEGER
   );
   """)

   conn.commit();

   print("Transactions Table created")

except:
   print("PROCESS FAILED")
#cur.execute executes the SQL command
#conn.commit writes to the database

