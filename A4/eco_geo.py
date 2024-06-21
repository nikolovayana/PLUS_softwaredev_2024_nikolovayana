"""
eco_geo.py

A module for ecological and conservation biology analysis using geospatial data. 
This module provides tools to visualize geographic data, analyze habitat maps, 
and calculate vegetation indices from satellite images.
"""

import folium
import rasterio
from rasterio import plot
from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def create_map(location, zoom_start=10):
    """
    Generate an interactive map using the Folium library centered at the provided location.
    
    Args:
        location (tuple): A tuple containing the latitude and longitude of the map's center.
        zoom_start (int): Initial zoom level for the map.

    Returns:
        folium.Map: A Folium Map object.
    """
    # Create a map centered around the provided location
    map = folium.Map(location=location, zoom_start=zoom_start)
    folium.TileLayer('OpenStreetMap').add_to(map)
    return map

def analyze_habitat_raster(raster_path, pixel_size):
    """
    Opens a raster of habitat types, displays it with unique colors, and calculates the area of each habitat type.
    
    Args:
        raster_path (str): The file path to the raster file.
        pixel_size (float): The size of one pixel in square meters.
    
    Returns:
        None: Displays a plot and prints area statistics.
    """
    # Open the raster file
    with rasterio.open(raster_path) as src:
        habitat_data = src.read(1)  # Assume habitat data is in the first band

    # Define a unique color for each habitat type (up to 10 types in this example)
    colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'orange', 'purple', 'brown', 'pink']
    cmap = ListedColormap(colors[:np.max(habitat_data) + 1])  # Create a color map

    # Display the raster data
    plt.figure(figsize=(10, 10))
    plt.imshow(habitat_data, cmap=cmap)
    plt.colorbar()
    plt.title('Habitat Types')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.show()

    # Calculate the area of each habitat type
    unique, counts = np.unique(habitat_data, return_counts=True)
    areas = counts * pixel_size  # Calculate area by multiplying count by pixel size

    # Print the area of each habitat type
    for habitat_type, area in zip(unique, areas):
        print(f'Habitat Type {int(habitat_type)}: {area:.2f} square meters')



def display_ndvi(image_path, red_band_index, nir_band_index):
    """
    Calculate and display the NDVI from a satellite image using band indices.

    Args:
        image_path (str): The file path to the satellite image.
        red_band_index (int): The index of the red band in the satellite image.
        nir_band_index (int): The index of the NIR band in the satellite image.
    """
    # Open the satellite image
    with rasterio.open(image_path) as src:
        # Read the specific bands using indices
        red = src.read(red_band_index)
        nir = src.read(nir_band_index)

        # Calculate NDVI
        ndvi = (nir.astype(float) - red.astype(float)) / (nir + red)

        # Set any division by zero to zero
        ndvi[np.isnan(ndvi)] = 0

        # Plot NDVI
        plt.figure(figsize=(10, 10))
        plt.imshow(ndvi, cmap='RdYlGn')
        plt.colorbar()
        plt.title('NDVI Image')
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.show()