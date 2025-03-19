import argparse
import pandas as pd
import os

def merge_csv(file_path1, file_path2, output_path, key1, key2):
    try:
        # Check if the files exist
        if not os.path.exists(file_path1):
            print(f"Error: {file_path1} does not exist.")
            return
        if not os.path.exists(file_path2):
            print(f"Error: {file_path2} does not exist.")
            return

        # Read the CSV files
        df1 = pd.read_csv(file_path1)
        df2 = pd.read_csv(file_path2)

        # Merge the two CSV files on the given keys
        merged_df = pd.merge(df1, df2, left_on=key1, right_on=key2, how='inner')

        # Output_path the merged CSV to the specified file
        merged_df.to_csv(output_path, index=False)
        print(f'Merged CSV saved to {output_path}')
    except Exception as e:
        print(f'Error: {e}')

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description='Merge two CSV files on different keys.')
    parser.add_argument('file_path1', help='The path to the first CSV file to merge')
    parser.add_argument('file_path2', help='The path to the second CSV file to merge')
    parser.add_argument('output_path', help='The output_path path to save the merged result')
    parser.add_argument('key1', help='The column name to join the first CSV on')
    parser.add_argument('key2', help='The column name to join the second CSV on')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the merge function with the arguments
    merge_csv(args.file_path1, args.file_path2, args.output_path, args.key1, args.key2)

if __name__ == '__main__':
    main()
