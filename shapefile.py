import pandas as pd
import numpy as np
import re
import math
import geopandas as gpd
import matplotlib.pyplot as plt

data = pd.read_csv('123.csv',encoding='utf-8')
khuvuc = np.array([])
diachi = np.array([])
latitude = np.array([])
longitude = np.array([])
year1953 = np.array([])
year1975 = np.array([])
year1983 = np.array([])
year1999 = np.array([])

def dms_to_degree(deg,minutes,seconds):
    degree = (float(deg) + float(minutes)/60 + float(seconds)/(60*60)) * 1 # vi tri VN o ban cau bac, ban cau dong
    return degree

for i in range(0,len(data)):
    # print(data['STT'][i])
    if data['STT'][i] == 'I':
        flag = 1
    elif data['STT'][i] == 'II':
        flag = 2
    elif data['STT'][i] == 'III':
        flag = 3
    elif data['STT'][i] == 'IV':
        flag = 4
    elif data['STT'][i] == 'V':
        flag = 5
    elif data['STT'][i] == 'VI':
        flag = 6
    if pd.isna(data['lat'][i]) and pd.isna(data['long'][i]):
        pass
    else:
        dms_lat = data['lat'][i].replace(',','.').split(' ')
        deg = dms_lat[0]
        minutes = dms_lat[1]
        seconds = dms_lat[2]
        degree_lat = dms_to_degree(deg,minutes,seconds)
        latitude = np.append(latitude,degree_lat)
        
        dms_long = data['long'][i].replace(',','.').split(' ')
        deg = dms_long[0]
        minutes = dms_long[1]
        seconds = dms_long[2]
        degree_long = dms_to_degree(deg,minutes,seconds)
        longitude = np.append(longitude,degree_long)

        diachi = np.append(diachi,data['Địa điểm'][i])

        year1953 = np.append(year1953,data['1953'][i])
        year1975 = np.append(year1975,data['1975'][i])
        year1983 = np.append(year1983,data['1983'][i])
        year1999 = np.append(year1999,data['1999'][i])

        if flag == 1:
            khuvuc = np.append(khuvuc,'Thành phố Huế')
        elif flag == 2:
            khuvuc = np.append(khuvuc,'Huyện Quảng điền')
        elif flag == 3:
            khuvuc = np.append(khuvuc,'Huyện Hương Trà')
        elif flag == 4:
            khuvuc = np.append(khuvuc,'Huyện Phong điền')
        elif flag == 5:
            khuvuc = np.append(khuvuc,'Huyện Hương Thuỷ')
        elif flag == 6:
            khuvuc = np.append(khuvuc,'Huyện Phú vang')

dict = {'Địa điểm':diachi, 'Khu vực':khuvuc, 'latitude':latitude,'longitude': longitude,'1953':year1953,'1975':year1975,'1983':year1983,'1999':year1999}

df = pd.DataFrame(dict)
df.to_csv('file_processed.csv',encoding='utf-8')
# data = pd.read_csv('file_processed.csv',encoding='utf-8')
# data_gdf = gpd.GeoDataFrame(data, geometry = gpd.points_from_xy(data['longitude'], data['latitude']))
# data_gdf.plot()
# # plt.show()
# ESRI_WKT = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]]'

# # Save the file as an ESRI Shapefile
# data_gdf.to_file(filename = 'data.shp', driver = 'ESRI Shapefile', crs_wkt = ESRI_WKT)
