# Create a script that will compare the cells the first is from a query in the database and of csv file taken then compare both if they are not similar then output the the cell and location as (column number and row number) in a new csv file on Windows

import csv
import os

#import postgres connector
import psycopg2

#Get the current working directory
#cwd = os.getcwd()


##request the user to add the path of file1 CSV file
file1 = input("Please enter the path of file1 CSV file: ")
file2 = input("Enter your current path")+ "_query.csv"
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
output = input("Please enter the path to create output CSV file: ")
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
    #writer.writerow(['MSISDN'])
    # Loop through the rows of the new CSV file
    for j in rslt:
        # Print the cell and location
         writer.writerow([j])

         # Open the 2 CSV files
with open( file1, 'r') as f1, open(file2, 'r') as f2:
    reader1 = csv.reader(f1)
    reader2 = csv.reader(f2)
    # Create a new CSV file to write the result to
    with open(output+'\\output.csv', 'w', newline='') as f3:
        writer = csv.writer(f3)
        #Write the header row to the new CSV file
        writer.writerow(['File 1', 'File 2', 'Row', 'Column'])
        # Loop through the rows of the 2 CSV files
        for row1, row2 in zip(reader1, reader2):
            # Loop through the cells of the 2 CSV files
            for cell1, cell2 in zip(row1, row2):
                # Compare the cells of the 2 CSV files
                if cell1 != cell2:
                    # Write the cell and location to the new CSV file
                    writer.writerow([cell1, cell2, reader1.line_num, row1.index(cell1)+1])