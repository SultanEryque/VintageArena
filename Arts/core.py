import psycopg2
#imports the psycopg2 module for connecting to database

#initiates the connection and prints if successfull
try:
   conn = psycopg2.connect("dbname='arts' user='black_eryque' password='CADEnsicloop60'")
   print("ACCESS GRANTED, HELLO ERYQUE")

except:
   print("ACCESS DENIED")
#incase the connection fails
