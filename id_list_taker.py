import csv
import argparse
import os

def get_ids_from_csv(input_path, output_path, id_column):
    if not os.path.exists(input_path):
        print(f"Error: {input_path} does not exist.")
        return
    with open(input_path, newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        ids = [row[id_column] for row in reader if id_column in row]
        with open(output_path, "w", encoding="utf-8") as f:
            print("('" + "','".join(map(str, ids)) + "')", file=f)

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
