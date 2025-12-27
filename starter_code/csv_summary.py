# csv_summary.py - read a CSV file and print a simple summary
import csv
import sys

def summarize_csv(path):
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        print(f'Rows: {len(rows)}')
        if rows:
            print('Columns: ' + ', '.join(reader.fieldnames))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python csv_summary.py data.csv')
    else:
        summarize_csv(sys.argv[1])
