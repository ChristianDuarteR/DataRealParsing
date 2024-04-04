import matplotlib.pyplot as plt
import seaborn as sns

def plot_vehicle_year_distribution(data):
    years = [int(entry['year']) for entry in data]
    plt.hist(years, bins=20, color='#86bf91', edgecolor='black')
    plt.xlabel('Año')
    plt.ylabel('Cantidad de vehículos')
    plt.title('Distribución de años de los vehículos')
    plt.grid(True)
    plt.show()


def plot_transmission_distribution(data):
    transmission_types = [entry['transmission_type'] for entry in data]
    unique_transmissions = list(set(transmission_types))
    transmission_counts = [transmission_types.count(transmission) for transmission in unique_transmissions]

    sns.barplot(x=unique_transmissions, y=transmission_counts, palette='Blues_d')
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

    sns.barplot(x=top_brands, y=brand_values, palette='Set2')
    plt.xlabel('Marca del Vehículo')
    plt.ylabel('Cantidad de Vehículos')
    plt.title('Distribución de Marcas de Vehículos (Top 10)')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')
    plt.show()

def plot_color_distribution(data):
    # Extraer la columna de color del conjunto de datos
    colors = [row['color'] for row in data]

    # Contar la frecuencia de cada color
    color_counts = {}
    for color in colors:
        color_counts[color] = color_counts.get(color, 0) + 1

    # Ordenar los colores por frecuencia descendente
    sorted_colors = sorted(color_counts.items(), key=lambda x: x[1], reverse=True)

    # Extraer los colores y las frecuencias ordenadas
    colors_sorted = [color[0] for color in sorted_colors]
    counts_sorted = [color[1] for color in sorted_colors]

    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    sns.barplot(x=colors_sorted, y=counts_sorted, palette='pastel')
    plt.title('Distribución de Colores de Vehículos')
    plt.xlabel('Color')
    plt.ylabel('Frecuencia')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def plot_engine_size_by_brand(data):
    # Crear un diccionario para almacenar los tamaños de motor promedio por marca
    engine_size_by_brand = {}

    # Iterar sobre los datos para calcular el tamaño de motor promedio para cada marca
    for row in data:
        brand = row['brand']
        engine_size = float(row['engine_size'][:-1])  # Eliminar la unidad ('L') y convertir a flotante
        if brand not in engine_size_by_brand:
            engine_size_by_brand[brand] = []
        engine_size_by_brand[brand].append(engine_size)

    # Calcular el tamaño de motor promedio para cada marca
    avg_engine_size_by_brand = {brand: sum(engine_sizes) / len(engine_sizes) for brand, engine_sizes in engine_size_by_brand.items()}

    # Ordenar las marcas por tamaño de motor promedio descendente
    sorted_brands = sorted(avg_engine_size_by_brand.items(), key=lambda x: x[1], reverse=True)

    # Extraer las marcas y los tamaños de motor promedio ordenados
    brands_sorted = [brand[0] for brand in sorted_brands]
    engine_sizes_sorted = [brand[1] for brand in sorted_brands]

    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    sns.barplot(x=brands_sorted, y=engine_sizes_sorted, palette='husl')
    plt.title('Tamaño Promedio del Motor por Marca de Vehículo')
    plt.xlabel('Marca')
    plt.ylabel('Tamaño del Motor Promedio (Litros)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def plot_fuel_type_distribution(data):
    # Crear un diccionario para almacenar la frecuencia de cada tipo de combustible
    fuel_type_counts = {}

    # Contar la frecuencia de cada tipo de combustible
    for row in data:
        fuel_type = row['fuel_Type']
        if fuel_type not in fuel_type_counts:
            fuel_type_counts[fuel_type] = 0
        fuel_type_counts[fuel_type] += 1

    # Extraer los tipos de combustible y sus frecuencias
    fuel_types = list(fuel_type_counts.keys())
    counts = [fuel_type_counts[fuel_type] for fuel_type in fuel_types]

    # Crear el gráfico de barras
    plt.figure(figsize=(8, 6))
    sns.barplot(x=fuel_types, y=counts, palette='hsv')
    plt.title('Distribución de Tipos de Combustible')
    plt.xlabel('Tipo de Combustible')
    plt.ylabel('Frecuencia')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
