'''
Import required libraries
'''
import pandas as pd
import numpy as np
import copy

class CSVtools:
    def __init__(self, file_path):
        # Initialisation
        # DO NOT EDIT
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.saved_df = [copy.deepcopy(self.data)]
        self.comments = ["initial dataframe"]


    ''' View Dataframes '''
    def display_data(self):
        # View current Dataframe that you are working on
        # It is always the first Dataframe found in your list of saved dataframes
        #print(f"Comment: {self.comments[0]}\n") -> removed to avoid confusion between Dataframe that's still editing
        print(self.data.to_markdown())

    def display_saved_df(self):
        # View any of the saved Dataframe
        for i, comment in enumerate(self.comments):
            print(f"{i}: {comment}")
        index = int(input("Enter the index of the Dataframe that you want to view: "))
        if 0 <= index < len(self.saved_df):
            selected_df = self.saved_df[index]
            selected_comment = self.comments[index]
            print(f"Comment: {selected_comment}\n")
            print(selected_df.to_markdown())
        else:
            print("Invalid index. Try again.")


    ''' View Dimensions '''
    def get_rows(self):
        # Display number of rows
        return self.data.shape[0]

    def get_columns(self):
        # Display number of columns
        return self.data.shape[1]
    
    def get_dimensions(self):
        # Display rows x columns
        return self.data.shape[0], self.data.shape[1]


    ''' Edit Dataframes '''
    def update_cell(self, row, column, value):
        # Allow users to edit cell(s) in Dataframe
        # Edit multiple cells from different rows and columns
        if isinstance(row, list) and isinstance(column, list):
            for r in row:
                for c in column:
                    if 0 <= r < self.get_rows() and c in self.data.columns:
                        self.data.at[r, c] = value
                    else:
                        print("Invalid row or column.")
        self.display_data()
    
    def filter_data(self, column, condition):
        # Apply filter and print out filtered DataFrame
        print(f"{column} == {condition}")
        self.data = self.data.query(f"{column} == '{condition}'")
        print(self.data.to_markdown())

    def duplicate_row(self, row, times):
        # Allow users to duplicate a specific row 
        if 0 <= row < self.get_rows():
            row_data = self.data.iloc[[row]]  
            duplicates = pd.concat([row_data] * times, ignore_index=True)
            self.data = pd.concat([self.data.iloc[:row + 1], duplicates, self.data.iloc[row + 1:]], ignore_index=True)
        else:
            print("Invalid row index.")

    def extract_columns(self, columns):
        # Allow users to extract specific columns from Dataframe
        if all(col in self.data.columns for col in columns):
            self.data = self.data[columns]
            print(self.data.to_markdown())
        else:
            print("One or more columns not found in the DataFrame.")

    def save_dataframe(self, comment):
        # Save current working Dataframe with comment
        # Automatically remove oldest Dataframe when there are 10 saved Dataframes
        if (len(self.saved_df)) > 10:
            self.saved_df.pop()
            self.comments.pop()
        self.saved_df.insert(0, copy.deepcopy(self.data))
        self.comments.insert(0, comment)
        print(f"Dataframe saved with comment: {comment}")

    def revert_dataframe(self):
        # Revert to previously saved Dataframe
        for i, comment in enumerate(self.comments):
            print(f"{i}: {comment}")
        index = int(input("Enter the index of the Dataframe that you want to revert: "))
        if 0 <= index < len(self.saved_df):
            self.data = copy.deepcopy(self.saved_df[index])
            self.display_data()
            print(f"Reverted to Dataframe saved with comment: {self.comments[index]}")
            self.save_dataframe(self.comments[index])
            self.saved_df.pop(index+1)
            self.comments.pop(index+1)


    ''' Make Changes to CSV File '''
    def save_csv(self, new_file_path=None):
        print(f"Current filepath: {self.file_path}")
        new_file_path = str(input("Enter new filepath (if you want to change or press Enter to skip): "))
        if new_file_path:
            self.data.to_csv(new_file_path, index=False)
            print(f"Dataframe saved to {new_file_path}")
        else:
            self.data.to_csv(self.file_path, index=False)
            print(f"Dataframe saved to {self.file_path}")