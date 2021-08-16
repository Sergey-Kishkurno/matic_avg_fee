import csv

file_name = "data.csv"


def save_file(list_to_save, fname = file_name):
    with open(fname, 'w',  newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        for line in list_to_save:
            writer.writerow(line)
