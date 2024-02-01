# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 08:41:15 2024

@author: mumble

random 12string generator
"""

import random
import string
import pandas as pd

def generate_random_number_string(length):
    """Generate a random string with numbers only."""
    return ''.join(random.choice(string.digits) for _ in range(length))

def main():
    # Get user input for the number of strings to generate
    try:
        num_strings = int(input("Enter the number of strings to generate: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    # Generate random number strings
    random_strings = [generate_random_number_string(12) for _ in range(num_strings)]

    # Create a DataFrame with the generated strings
    data = {'Random Number EAN': random_strings}
    df = pd.DataFrame(data)

    # Save the DataFrame to an Excel file
    file_name = f"random_number_strings_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    df.to_excel(file_name, index=False)

    print(f"Generated {num_strings} random number strings and saved to {file_name}")

if __name__ == "__main__":
    main()

