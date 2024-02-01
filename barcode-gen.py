# -*- coding: utf-8 -*-
"""
Created on Thu Feb 1 07:48:22 2024

@author: mumble

barcode generator 
will read an excel file and then generate a barcode
"""

from barcode import EAN13
from barcode.writer import ImageWriter
import pandas as pd
from datetime import datetime
import os

# Read numbers from Excel file
df = pd.read_excel("random_num.xlsx") # input file name of excel here
numbers = df['Random Number EAN'].astype(str)  # input column name here (the random 12 digit string generator already has this column name, no need to edit this one (only whene necessary ^_^))

# will create folder with timestamp format "day-month-year-time"

timestamp_folder = datetime.now().strftime("%d-%m-%Y-%H%M%S")
os.makedirs(timestamp_folder, exist_ok=True)

# Generate and save barcodes with timestamp and string name
for number in numbers:
    if len(number) == 11:
        number = '0' + number  # Add leading zero to make it 12 digits for EAN-13
    elif len(number) != 12:
        print(f"Skipping invalid number: {number}")
        continue

    my_code = EAN13(number, writer=ImageWriter())
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp_folder}/barcode_{timestamp}_{number}"
    my_code.save(filename)
