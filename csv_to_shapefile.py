import pandas as pd
import numpy as np
import re
import math
import geopandas as gpd

data = pd.read_csv('file_processed.csv',encoding='utf-8')
data_gdf = gpd.GeoDataFrame(data, geometry = gpd.points_from_xy(data['longitude'], data['latitude']))
data_gdf.plot()
# plt.show()
ESRI_WKT = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]]'

# Save the file as an ESRI Shapefile
data_gdf.to_file(filename = 'data.shp', driver = 'ESRI Shapefile', crs_wkt = ESRI_WKT)
