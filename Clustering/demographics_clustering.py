import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import plotly.express as px

X=pd.read_csv('../Datasets/demographics/Demographics_of_India.csv')
X=X.dropna()
O=X.copy()
X=X.drop(columns=['objectid', 'statecode', 'statename', 'state_ut', 'distcode','globalid']) #drop useless columns
X=X.set_index('distname')
X=StandardScaler().fit_transform(X) #scale data

pca=PCA(n_components=2)
pcx=pca.fit_transform(X) #principal component analysis, reduce to 2 components

db=DBSCAN(eps=0.45,min_samples=3)
db.fit(pcx) #fit reduced data into dbscan model

yy=db.fit_predict(pcx) #perform dbscan on reduced data to get clusters
yy=yy.astype(str)

O['pc1']=pcx[:,0]
O['pc2']=pcx[:,1]

##fig=px.scatter(O,x='Total Individuals Registered',y='Total Sites',color=yy,hover_name='District',hover_data=['State'])
##fig.show()

fig=px.scatter(O,x='pc1',y='pc2',color=yy,hover_name='distname',hover_data=['statename'],color_discrete_sequence=px.colors.qualitative.Dark24) #plot clusters
fig.show()
