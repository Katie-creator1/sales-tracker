import csv
import datetime

product_data = {                #The keys are the product IDs and the values are lists
    "P001": ["Wireless Headphones", 100],
    "P002": ["Laptop Backpack", 60],
    "P003": ["Bluetooth Speaker", 50],
    "P004": ["USB Flashdrive", 20],
    "P005": ["Mobile Phone Case", 15],
    "P006": ["Wireless Mouse", 30],
    "P007": ["Laptop Stand", 40],
    "P008": ["HDMI Cable", 15],
    "P009": ["Smartphone", 600],
    "P010": ["External Hard Drive", 100],
}
csv_data = []       #This is an empty list that will store each row of sale data before writing it to the csv file. This will be built up later using .append() in the loop

with open('product_sales.txt', 'r') as file:    #This opens and reads the list of product IDs
    product_ids = file.readlines() #This creates a list of lines from the file like: 'P001\n', 'P002\n', etc.

sale_id = 1         #This is a counter variable, it identifies each unique sale. It starts at 1 and increments per row
current_date = datetime.date.today()    #This fetches today's date for all the dates inside the loop, you only call this once for performance and consistency

for product_id in product_ids:      #This creates a loop over the product IDs read from the file
    product_id = product_id.strip() #This removes any newline or accidental whitespace from the ID, this helps avoid mismatches when looping up product IDs
    product_name = product_data[product_id][0]      #Each line represents once sale, so this loop is the core f your data generation process
    product_price = product_data[product_id][1]

    row = [current_date, sale_id, product_id, product_name, product_price] #This creates the full row that will be written to the CSV

    csv_data.append(row) #This adds the row to the empty csv_data list made earlier

    sale_id += 1 #This adds increments for the next sale

with open ('product_sales.csv','w', newline='') as csv_file:    #This opens the file as a CSV for writing
    csv_writer = csv.writer(csv_file)   #This creates an object that lets you write rows to the file

    csv_writer.writerow(['Current Date', 'Sale ID', 'Product ID', 'Product Name','Product Price']) #This writes the first row with column names, so your CSV in human-readable and compatible with Excel/Sheets

    csv_writer.writerows(csv_data)  #This writes every row from the csv_data list into the file in one batch
