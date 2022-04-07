import pandas as pd 
import geopandas as gpd

# Read the .csv file using Pandas 
airport_data = pd.read_csv('file_processed.csv',encoding='utf-8')

# Creating GeoPandas GeoDataFrame using the Pandas Dataframe 
airport_gdf = gpd.GeoDataFrame(airport_data, geometry = gpd.points_from_xy(airport_data['longitude'],airport_data['latitude'] ))

# Obtain the ESRI WKT
ESRI_WKT = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]]'

# Save the file as an ESRI Shapefile
airport_gdf.to_file(filename = 'dataHue.shp', driver = 'ESRI Shapefile', crs_wkt = ESRI_WKT,encoding='utf-8')
