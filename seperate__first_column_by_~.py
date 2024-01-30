import csv


def process_csv(input_csv_file, output_csv_file):
    encoding = 'utf-8'  # You can try 'latin-1' or other encodings based on your file content

    with open(input_csv_file, 'r', newline='', encoding=encoding) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        rows = [row for row in reader]

    # Extracting relevant values from each row
    processed_rows = []
    for row in rows:
        query = row[0].split("~")
        processed_rows.append(query)

    # Writing the processed data to a new CSV file
    with open(output_csv_file, 'w', newline='', encoding=encoding) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(processed_rows)


# Example usage:
input_file_path = 'output_merged.csv'  # Replace with the path to your input CSV file
output_file_path = 'output_processed.csv'  # Replace with the desired output file path

process_csv(input_file_path, output_file_path)
