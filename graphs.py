import matplotlib.pyplot as plt

def plot_vehicle_year_distribution(data):
    years = [int(entry['year']) for entry in data]
    plt.hist(years, bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Año')
    plt.ylabel('Cantidad de vehículos')
    plt.title('Distribución de años de los vehículos')
    plt.grid(True)
    plt.show()


def plot_transmission_distribution(data):
    transmission_types = [entry['transmission_type'] for entry in data]
    unique_transmissions = list(set(transmission_types))
    transmission_counts = [transmission_types.count(transmission) for transmission in unique_transmissions]

    plt.bar(unique_transmissions, transmission_counts, color='lightgreen', edgecolor='black')
    plt.xlabel('Tipo de Transmisión')
    plt.ylabel('Cantidad de Vehículos')
    plt.title('Distribución de Tipos de Transmisión')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')
    plt.show()

def plot_brand_distribution(data):
    brand_counts = {}
    for entry in data:
        brand = entry['brand']
        if brand in brand_counts:
            brand_counts[brand] += 1
        else:
            brand_counts[brand] = 1

    sorted_brands = sorted(brand_counts.items(), key=lambda x: x[1], reverse=True)
    top_brands = [brand[0] for brand in sorted_brands[:10]]
    brand_values = [brand_counts[brand] for brand in top_brands]

    plt.bar(top_brands, brand_values, color='red', edgecolor='black')
    plt.xlabel('Marca del Vehículo')
    plt.ylabel('Cantidad de Vehículos')
    plt.title('Distribución de Marcas de Vehículos (Top 10)')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')
    plt.show()