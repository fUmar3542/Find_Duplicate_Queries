import csv


def merge_columns(input_csv_file, output_csv_file):
    with open(input_csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]

    # Merge all columns into the first column
    merged_rows = ['~'.join(row) for row in rows]

    with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for merged_row in merged_rows:
            writer.writerow([merged_row.replace('~', ' ')])


# Example usage:
input_file_path = 'input_assign.csv'  # Replace with the path to your input CSV file
output_file_path = 'output_merged.csv'  # Replace with the desired output file path

merge_columns(input_file_path, output_file_path)
