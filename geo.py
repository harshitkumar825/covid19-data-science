import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import numpy as np
import json 
from shapely.geometry import LineString
from shapely import wkt
import contextily as ctx

with open('Datasets/railway/trains.json') as f:
  data = json.load(f)

df = {
    'name':[],
    'geometry':[]
}
for i in range(len(data['features'])):
    props = data['features'][i]['properties']
    # print(temp)
    cords = (data['features'][i]['geometry']['coordinates'])
    try:
        linestring = LineString(cords)
        df['name'].append(props['name'])
        df['geometry'].append(linestring)
    except:
        pass
    
    # break

df = pd.DataFrame(df)
print(df.head())
# df['geometry'] = df['geometry'].a)
gdf = gpd.GeoDataFrame(df, crs="EPSG:3857")
# gdf = gdf.to_crs(epsg=3857)
ax = gdf.plot(figsize=(10,10), alpha=0.5)
# ctx.add_basemap(ax)
plt.show()
# print(df['features'][0])
# with open('trains_new.json', 'w') as f:
#     json.dump(data, f)

