from graphs import plot_vehicle_year_distribution, plot_transmission_distribution, plot_brand_distribution, \
    plot_color_distribution, plot_engine_size_by_brand, plot_fuel_type_distribution
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
    plot_transmission_distribution(data)
    plot_brand_distribution(data)
    plot_color_distribution(data)
    plot_fuel_type_distribution(data)
