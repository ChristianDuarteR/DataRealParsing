from graphs import plot_vehicle_year_distribution
import csv

def parse_csv(csv_file):
    data = []
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


if __name__ == '__main__':
    data = parse_csv('files/out_20000.csv')
    plot_vehicle_year_distribution(data)
