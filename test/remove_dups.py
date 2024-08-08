import pandas as pd

def remove_duplicates(input_file, output_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file, low_memory=False)

    # Drop duplicates based on 'CAS no.' column, keeping the first occurrence
    df_unique = df.drop_duplicates(subset='CASNumber', keep='first')

    # Write the resulting DataFrame to a new CSV file
    df_unique.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_csv = 'Master_List_UPDATED.csv'  # Replace with your input CSV file path
    output_csv = 'output.csv'  # Replace with your desired output CSV file path

    remove_duplicates(input_csv, output_csv)
