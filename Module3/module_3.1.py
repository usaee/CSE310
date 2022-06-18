

import ibm_db
import pandas
import ibm_db_dbi


# This file contains my database access credentials
creds = []
with open('creds.txt', 'r') as f:
    creds = f.read().splitlines()

dsn_security = "SSL"
dsn_database = "BLUDB"
dsn_protocol = "TCPIP"
dsn_driver = "{IBM DB2 ODBC DRIVER}"

dsn_uid = creds[2]
dsn_pwd = creds[3]
dsn_port = creds[1]
dsn_hostname = creds[0]

# Creates database connection
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security)

try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database.")
except:
    print ("Unable to connect to database.")

# Connection for pandas
pconn = ibm_db_dbi.Connection(conn)

# This drops the MYTABLE table in case it exists from a previous run
dropQuery = "drop table MYTABLE"
dropStmt = ibm_db.exec_immediate(conn, dropQuery)

createQuery = "create table MYTABLE(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2))"
createStmt = ibm_db.exec_immediate(conn,createQuery)

insertQuery = "insert into MYTABLE values (1, 'Jeff', 'Bezos', 'TORONTO', 'CA')"
insertStmt = ibm_db.exec_immediate(conn, insertQuery)

# Query statement to retrieve all rows in the MYTABLE table
selectQuery = "select * from MYTABLE"
# Retrieves the query results into a pandas dataframe
pdf = pandas.read_sql(selectQuery, pconn)
print()
print()
print('Create Data Table Example:')
print(pdf)

input('\nPress ENTER to continue...')

insertQuery2 = "insert into MYTABLE values (2, 'Aaron', 'Caruso', 'BOISE', 'ID'), (3, 'Elon', 'Musk', 'HOUSTON', 'TX')"
insertStmt2 = ibm_db.exec_immediate(conn, insertQuery2)

pdf = pandas.read_sql(selectQuery, pconn)
print()
print()
print('Insert Data Example:')
print(pdf)

input('\nPress ENTER to continue...')

# Modifies Elon's CITY to LUBBOCK
updateQuery = "update MYTABLE set CITY='LUBBOCK' where FNAME='Elon'"
updateStmt = ibm_db.exec_immediate(conn, updateQuery)

pdf = pandas.read_sql(selectQuery, pconn)
print()
print()
print('Modify Data Example:')
print(pdf)

input('\nPress ENTER to continue...')

# Deletes Jeffs's row from the table
deleteQuery = "delete from MYTABLE where CITY in ('TORONTO')"
updateStmt = ibm_db.exec_immediate(conn, deleteQuery)

pdf = pandas.read_sql(selectQuery, pconn)
print()
print()
print('Deleting Data Example:')
print(pdf)

input('\nPress ENTER to continue...')

# Closes the connection
ibm_db.close(conn)






