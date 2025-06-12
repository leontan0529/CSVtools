''' Import required libraries, CSVtools Class and your CSV file '''
import os
import sys
import pandas as pd
import numpy as np
import copy
sys.path.insert(0, ".")
from src.csvtool import CSVtools
# Edit line below
filepath = r'I:\\leontan\DataCollection_TLC_sat_waveform_plot_config_rd 1.csv'

# Initialisation
editor = CSVtools(filepath)
editor.display_data()

def main():
    ''' Print out user prompt '''
    print("""
    Choose an option
    ---View Dataframes---
    1. Display current Dataframe
    2. Display previously saved Dataframe
    ---View Dimensions---
    3. Get number of rows
    4. Get number of columns
    5. Get dimensions
    ---Edit Dataframes---
    6. Update cell(s)
    7. Filter a column
    8. Duplicate a specific row
    9. Overwrite previously saved Dataframe with current Dataframe
    ---Make changes to CSV file---
    10. Update CSV file
    """)
    prompt = int(input("Please select an option(1-8): "))

    match prompt:
        case 1: # Display current Dataframe
            editor.display_data()
        case 2: # Display any saved Dataframe
            editor.display_saved_df()
            print("\nSaved Dataframes:")
        case 3: # Display number of rows
            print(f'\nRows: {editor.get_rows()}')
        case 4: # Display number of columns
            print(f'\nColumns: {editor.get_columns()}')
        case 5: # Display rows x columns
            print(f"\nDimensions (RxC): {editor.get_dimensions()}")
        case 6: # Allow users to edit cell(s) in Dataframe from different rows and columns
            save = str(input("\nDo you want to save your current Dataframe before making changes? (y/n (default))"))
            if save.lower() == "y":
                comment = str(input("\nPlease leave a comment for your Dataframe before saving: "))
                editor.save_dataframe(comment)
            else:
                pass

            print("If you would like to edit multiple rows and/or columns, please provide them in a list (e.g. ['EXP', 'SEQ', 'offset'])")
            print(f"From row 0 to {editor.get_rows()}")
            row = input("Which row do you want to edit?")
            row = [int(r) for r in row.split(',')] if ',' in row else [row]

            print(editor.data.columns.tolist())
            col = input("Which column do you want to edit?\n")
            col = [str(c).strip() for c in col.split(',')] if ',' in col else [col]
            print(f"test col: {col}")

            val = str(input("What value do you want to update?"))
            editor.update_cell(row, col, val)
        case 7: # Apply filter and display filtered Dataframe
            print(editor.data.columns.tolist())
            col = str(input("Which column do you want to filter from?"))
            cond = str(input("What do you want to filter from the following columns?\n (e.g. SPB)"))
            editor.filter_data(col, cond)
        case 8: # Allow users to duplicate a specific row
            save = str(input("\nDo you want to save your current Dataframe before making changes? (y/n (default))"))
            if save.lower() == "y":
                comment = str(input("\nPlease leave a comment for your Dataframe before saving: "))
                editor.save_dataframe(comment)
            else:
                pass

            print(f"From row 0 to {editor.get_rows()}")
            row = int(input("Which row do you want to duplicate?"))
            times = int(input("How many times do you want to duplicate?"))
            editor.duplicate_row(row, times)
            editor.display_data()
        case 9: # Overwrite current Dataframe with a saved Dataframe
            comment = str(input("\nPlease leave a comment for your Dataframe before saving: "))
            editor.save_dataframe(comment)
            print("\nDataframe permanently updated.")
        case 10: # Save current Dataframe as a new/update existing CSV file
            editor.save_csv()
            print("\nCSV file updated.")

    print("\nREMEMBER TO SAVE TO CSV ONCE YOU ARE DONE EDITING!")

try:
    while True:
        main()
except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting gracefully...")