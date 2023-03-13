import pyodbc  #To Install "pyodbc" run command pip install pyodbc on pycharm terminal

server = 'LAPTOP-MBL9B7IP\SQLEXPRESS'  #Define the SQL Server connection parameters just copy from your ssms server
database = 'Testing_43'  #It is the name of the database where you created in your ssms


# Create a connection string
conn_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database}'

# Establish a connection to the database
conn = pyodbc.connect(conn_string)


cursor = conn.cursor()  #Creating a cursor object

cursor.execute('Select * From Employee') #Executing

for i in cursor: # Fetching or retriving the results and print them
    print(i)

# Close the cursor and the connection
cursor.close()
conn.close()
