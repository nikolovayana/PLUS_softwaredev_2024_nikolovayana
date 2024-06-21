"""
eco_geo.py

A module for ecological and conservation biology analysis using geospatial data. 
This module provides tools to visualize geographic data, analyze satellite imagery, 
and calculate biodiversity indices across different geographies.
"""

import folium
import rasterio
from rasterio import plot
import gdal

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

def read_raster_data(file_path):
    """
    Read a raster file using Rasterio and return the dataset object for analysis.

    Args:
        file_path (str): Path to the raster file.

    Returns:
        rasterio.io.DatasetReader: Rasterio dataset reader object.
    """
    # Open the raster file
    dataset = rasterio.open(file_path)
    return dataset

def calculate_ndvi(red_band, nir_band):
    """
    Calculate the Normalized Difference Vegetation Index (NDVI) from red and NIR bands.

    Args:
        red_band (numpy.ndarray): Array representing the red band of the image.
        nir_band (numpy.ndarray): Array representing the near-infrared band of the image.

    Returns:
        numpy.ndarray: NDVI index array.
    """
    # Calculate NDVI
    ndvi = (nir_band - red_band) / (nir_band + red_band)
    return ndvi