import csv
import argparse
import os

def get_ids_from_csv(input_path, output_path, id_column):
    if not os.path.exists(input_path):
        print(f"Error: {input_path} does not exist.")
        return

    with open(input_path, newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)

        # Ensure the specified column exists
        if id_column not in reader.fieldnames:
            print(f"Error: Column '{id_column}' not found in {input_path}. Available columns: {', '.join(reader.fieldnames)}")
            return

        ids = [row[id_column] for row in reader if row[id_column]]

    if not ids:
        print(f"Warning: No IDs found in column '{id_column}'.")
        return

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"('{','.join(map(str, ids))}')\n")

    print(f"Extracted {len(ids)} IDs and saved to {output_path}.")

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description='Get a list of ID column.')
    parser.add_argument('input_path', help='The path to the file')
    parser.add_argument('output_path', help='The column name to output')
    parser.add_argument('id', help='The column name of id')

    # Parse the command-line arguments
    args = parser.parse_args()
    get_ids_from_csv(args.input_path, args.output_path, args.id)

if __name__ == '__main__':
    main()
