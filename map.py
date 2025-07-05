import matplotlib.pyplot as plt
import geopandas as gpd
import folium
from folium import plugins
import requests
import json

# Method 1: Using GeoPandas with Natural Earth data
def create_nigeria_map_geopandas():
    """
    Create a map of Nigeria using GeoPandas and Natural Earth data
    """
    # Download world map data
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    
    # Filter for Nigeria
    nigeria = world[world.name == 'Nigeria']
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 8))
    nigeria.plot(ax=ax, color='lightgreen', edgecolor='black', linewidth=2)
    
    # Customize the plot
    ax.set_title('Map of Nigeria', fontsize=16, fontweight='bold')
    ax.set_xlabel('Longitude', fontsize=12)
    ax.set_ylabel('Latitude', fontsize=12)
    ax.grid(True, alpha=0.3)
    
    # Remove axis spines for cleaner look
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.show()
    
    return fig

# Method 2: Interactive map using Folium
def create_nigeria_interactive_map():
    """
    Create an interactive map of Nigeria using Folium
    """
    # Nigeria's approximate center coordinates
    nigeria_center = [9.0820, 8.6753]
    
    # Create base map
    m = folium.Map(
        location=nigeria_center,
        zoom_start=6,
        tiles='OpenStreetMap'
    )
    
    # Add major Nigerian cities
    cities = {
        'Lagos': [6.5244, 3.3792],
        'Abuja': [9.0765, 7.3986],
        'Kano': [12.0022, 8.5920],
        'Ibadan': [7.3775, 3.9470],
        'Port Harcourt': [4.8156, 7.0498],
        'Benin City': [6.3350, 5.6037],
        'Maiduguri': [11.8311, 13.1511],
        'Zaria': [11.0449, 7.7336],
        'Aba': [5.1066, 7.3667],
        'Jos': [9.8965, 8.8583]
    }
    
    # Add city markers
    for city, coords in cities.items():
        folium.Marker(
            coords,
            popup=f'<b>{city}</b>',
            tooltip=city,
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)
    
    # Add a marker for the capital
    folium.Marker(
        cities['Abuja'],
        popup='<b>Abuja - Federal Capital Territory</b>',
        tooltip='Capital City',
        icon=folium.Icon(color='green', icon='star')
    ).add_to(m)
    
    # Save the map
    m.save('nigeria_interactive_map.html')
    print("Interactive map saved as 'nigeria_interactive_map.html'")
    
    return m

# Method 3: Using administrative boundaries from online source
def create_detailed_nigeria_map():
    """
    Create a detailed map of Nigeria with state boundaries
    """
    try:
        # URL for Nigeria administrative boundaries (states)
        url = "https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson"
        
        # For this example, we'll use a simpler approach
        # In practice, you'd want to use a specific Nigeria GeoJSON file
        
        # Create a basic map with state information
        fig, ax = plt.subplots(figsize=(15, 10))
        
        # Nigeria's major states (approximate center coordinates)
        states = {
            'Lagos': [6.5244, 3.3792],
            'Ogun': [7.1608, 3.3566],
            'Oyo': [7.8451, 3.9314],
            'Osun': [7.5629, 4.5200],
            'Ondo': [7.2506, 5.2111],
            'Ekiti': [7.7188, 5.3111],
            'Kwara': [8.9670, 4.3060],
            'Kogi': [7.7323, 6.6383],
            'Benue': [7.3373, 8.7500],
            'Plateau': [9.2182, 9.5179],
            'Nasarawa': [8.5378, 8.1139],
            'Abuja': [9.0765, 7.3986],
            'Niger': [10.4806, 6.5447],
            'Kebbi': [12.4539, 4.1994],
            'Sokoto': [13.0059, 5.2476],
            'Zamfara': [12.1743, 6.6594],
            'Katsina': [13.0001, 7.6177],
            'Kano': [12.0022, 8.5920],
            'Jigawa': [12.4500, 9.3500],
            'Bauchi': [10.3158, 9.8442],
            'Gombe': [10.2896, 11.1670],
            'Yobe': [12.2943, 11.9670],
            'Borno': [11.8311, 13.1511],
            'Adamawa': [9.3265, 12.3984],
            'Taraba': [8.8921, 11.3604],
            'Kaduna': [10.5105, 7.4165],
            'Katsina': [13.0001, 7.6177],
            'Cross River': [6.3093, 8.3000],
            'Akwa Ibom': [5.0088, 7.8699],
            'Rivers': [4.8156, 7.0498],
            'Bayelsa': [4.7719, 6.0699],
            'Delta': [5.6037, 6.1319],
            'Edo': [6.3350, 5.6037],
            'Anambra': [6.2107, 6.9975],
            'Enugu': [6.4474, 7.5425],
            'Ebonyi': [6.2649, 8.0137],
            'Abia': [5.4527, 7.5248],
            'Imo': [5.5720, 7.0588]
        }
        
        # Plot states as points (in a real scenario, you'd use actual polygons)
        lons = [coord[1] for coord in states.values()]
        lats = [coord[0] for coord in states.values()]
        
        ax.scatter(lons, lats, c='red', s=50, alpha=0.6, edgecolors='black')
        
        # Add state labels
        for state, coords in states.items():
            ax.annotate(state, (coords[1], coords[0]), 
                       xytext=(5, 5), textcoords='offset points',
                       fontsize=8, ha='left')
        
        # Set the map boundaries for Nigeria
        ax.set_xlim(2.5, 15.0)
        ax.set_ylim(4.0, 14.0)
        
        ax.set_title('Nigeria - States Overview', fontsize=16, fontweight='bold')
        ax.set_xlabel('Longitude', fontsize=12)
        ax.set_ylabel('Latitude', fontsize=12)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        
        return fig
        
    except Exception as e:
        print(f"Error creating detailed map: {e}")
        return None

# Method 4: Simple coordinate-based outline
def create_simple_nigeria_outline():
    """
    Create a simple outline map of Nigeria using approximate coordinates
    """
    # Approximate Nigeria boundary coordinates
    nigeria_outline = [
        [2.69, 6.26], [2.76, 9.23], [3.32, 11.99], [3.84, 13.85],
        [5.44, 13.87], [6.70, 13.25], [8.50, 13.25], [9.50, 12.95],
        [10.50, 13.25], [11.97, 13.37], [13.44, 13.73], [14.68, 13.25],
        [14.68, 12.48], [14.89, 11.57], [14.96, 10.26], [14.68, 9.90],
        [14.68, 9.14], [14.68, 8.10], [14.68, 6.50], [14.18, 6.02],
        [13.89, 5.47], [13.22, 4.89], [12.35, 4.89], [11.70, 4.89],
        [9.97, 4.89], [9.30, 4.89], [8.50, 4.89], [7.46, 4.89],
        [6.70, 4.89], [5.44, 4.89], [4.18, 4.89], [3.32, 4.89],
        [2.69, 5.47], [2.69, 6.26]
    ]
    
    # Extract x and y coordinates
    x_coords = [point[0] for point in nigeria_outline]
    y_coords = [point[1] for point in nigeria_outline]
    
    # Close the polygon
    x_coords.append(x_coords[0])
    y_coords.append(y_coords[0])
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(x_coords, y_coords, 'b-', linewidth=2, label='Nigeria Boundary')
    ax.fill(x_coords, y_coords, alpha=0.3, color='lightblue')
    
    # Add major cities
    cities = {
        'Lagos': [3.3792, 6.5244],
        'Abuja': [7.3986, 9.0765],
        'Kano': [8.5920, 12.0022],
        'Ibadan': [3.9470, 7.3775],
        'Port Harcourt': [7.0498, 4.8156]
    }
    
    for city, coords in cities.items():
        ax.plot(coords[0], coords[1], 'ro', markersize=8)
        ax.annotate(city, (coords[0], coords[1]), 
                   xytext=(5, 5), textcoords='offset points',
                   fontsize=10, fontweight='bold')
    
    ax.set_title('Nigeria - Simple Outline Map', fontsize=16, fontweight='bold')
    ax.set_xlabel('Longitude', fontsize=12)
    ax.set_ylabel('Latitude', fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    plt.tight_layout()
    plt.show()
    
    return fig

# Main execution
if __name__ == "__main__":
    print("Creating Nigeria Maps...")
    print("=" * 50)
    
    # Method 1: GeoPandas map
    print("1. Creating GeoPandas map...")
    try:
        fig1 = create_nigeria_map_geopandas()
        print("✓ GeoPandas map created successfully")
    except Exception as e:
        print(f"✗ GeoPandas map failed: {e}")
    
    # Method 2: Interactive map
    print("\n2. Creating interactive map...")
    try:
        map2 = create_nigeria_interactive_map()
        print("✓ Interactive map created successfully")
    except Exception as e:
        print(f"✗ Interactive map failed: {e}")
    
    # Method 3: Detailed map
    print("\n3. Creating detailed map...")
    try:
        fig3 = create_detailed_nigeria_map()
        print("✓ Detailed map created successfully")
    except Exception as e:
        print(f"✗ Detailed map failed: {e}")
    
    # Method 4: Simple outline
    print("\n4. Creating simple outline map...")
    try:
        fig4 = create_simple_nigeria_outline()
        print("✓ Simple outline map created successfully")
    except Exception as e:
        print(f"✗ Simple outline map failed: {e}")
    
    print("\n" + "=" * 50)
    print("Map generation complete!")
    print("Note: Make sure you have the required libraries installed:")
    print("pip install matplotlib geopandas folium requests")
