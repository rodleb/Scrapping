# Create a script that will compare the cells the first is from a query in the database and of csv file taken then compare both if they are not similar then output the the cell and location as (column number and row number) in a new csv file on Windows

import csv
import os

#import postgres connector
import psycopg2

##request the user to add the path of file1 CSV file
file1 = input("Please enter the path of file1 CSV file: ")
file2 = file1.replace(".csv", "_query.csv")
##request the user to add the query
#query = input("Please enter the query: ")
#
##request the user to add the Username, password, Ip Address, and Database Name
#username = input("Please enter the Username: ")
#password = input("Please enter the password: ")
#ip = input("Please enter the Ip Address: ")
#database = input("Please enter the Database Name: ")
#
##143.42.21.178 5432 rbt_text_user snbL7T28rOJj4w2 database: rbt_text
##request the user to add the path of output CSV file
#output = input("Please enter the path to create output CSV file: ")
#
query = "select sb.msisdn FROM public.subscriber_blacklist sb"

#request th
username = "rbt_text_user"
password = "snbL7T28rOJj4w2"
ip = "143.42.21.178"
database = "rbt_text"



# Run the query on postgresdb
conn = psycopg2.connect(database=database, user=username, password=password, host=ip, port="5432")
cursor = conn.cursor()

# Execute the query anf return the result
cursor.execute(query)
result = cursor.fetchall()

# create a for loop to loop through the result
rslt = list(result)
for i in range(len(result)):
    rslt[i] = str(rslt[i]).replace("('", "").replace("',)", "")
    print(rslt[i])


with open(file2, 'w', newline='') as f4:
    writer = csv.writer(f4)
    #Write the header row to the new CSV file
    writer.writerow(['MSISDN'])
    # Loop through the rows of the new CSV file
    for row in rslt:
        # Print the cell and location
         writer.writerow([row])