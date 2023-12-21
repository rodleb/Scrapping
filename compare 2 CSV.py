# Create a script that will compare 2 the cells of csv file taken from 2 Files and output the the cell and location as (column number and row number) in a new csv file on Windows

import csv
import os

#request the user to add the path of file1 CSV file
file1 = input("Please enter the path of file1 CSV file: ")

#request the user to add the path of file2 CSV file
file2 = input("Please enter the path of file2 CSV file: ")

#request the user to add the path of output CSV file
output = input("Please enter the path to create output CSV file: ")


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

# Open the new CSV file
with open(output+'\\output.csv', 'r') as f4:
    reader = csv.reader(f4)
    # Loop through the rows of the new CSV file
    for row in reader:
        # Print the cell and location
        print(row)

# Close the 2 CSV files
f1.close()
f2.close()

# Close the new CSV file
f3.close()


