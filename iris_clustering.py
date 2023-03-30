from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from kneed import KneeLocator
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Seccion 1 o seccion 2
def iris_clustering(feature_1, feature_2, ideal_k):
    """Seccion 1 y seccion 2 unificada, cambiando sus reasultado de acuerdo a los features considerados para el clustering.

    Args:
        feature_1 (_type_): _description_
        feature_2 (_type_): _description_
    """
    DATA_PATH = "./data" 
    data = pd.read_csv(f"{DATA_PATH}/iris.csv")
    # 1. Visualicen los datos para ver si pueden detectar algunos grupos. Ayuda: utilicen la forma del sépalo
    plt.scatter(data[feature_1], data[feature_2])

    min_sepal_length = data[feature_1].min()
    max_sepal_length = data[feature_1].max() 

    min_sepal_width = data[feature_2].min()
    max_sepal_width = data[feature_2].max() 

    plt.xlim(min_sepal_length, max_sepal_length)
    plt.ylim(min_sepal_width, max_sepal_width)
    plt.show()
    # 2. Visualicen los datos para ver si pueden detectar algunos grupos. Ayuda: utilicen la forma del sépalo
    X = data.filter([feature_1, feature_2])
    kmeans = KMeans(2)
    kmeans.fit(X)
    clusters = kmeans.fit_predict(X)
    data_sec1 = data.copy()
    data_sec1["Cluster"] = clusters
    data_sec1["Cluster"] =data_sec1["Cluster"].astype("category")
    fig = px.scatter(data_sec1, x = feature_1, y = feature_2, color = "Cluster", hover_data = ['Cluster'])
    fig.update_xaxes(range=[min_sepal_length, max_sepal_length])
    fig.update_yaxes(range=[min_sepal_width, max_sepal_width])
    fig.show()
    # 3 Estandaricen los datos e intenten el paso 2, de nuevo. ¿Qué diferencias hay, si es que lo hay?
    scaler = StandardScaler()
    X_standarized = X.copy()
    X_standarized[X_standarized.columns] = scaler.fit_transform(X_standarized[X_standarized.columns])
    kmeans = KMeans(2)
    kmeans.fit(X_standarized)
    clusters = kmeans.fit_predict(X_standarized)
    data_sec1_3 = data.copy()
    data_sec1_3["Cluster"] = clusters
    data_sec1_3["Cluster"] =data_sec1_3["Cluster"].astype("category")
    fig = px.scatter(data_sec1_3, x = feature_1, y = feature_2, color = "Cluster", hover_data = ['Cluster'])
    fig.update_xaxes(range=[min_sepal_length, max_sepal_length])
    fig.update_yaxes(range=[min_sepal_width, max_sepal_width])
    fig.show()
    # 4 Utilicen el método del "codo" para determinar cuantos "clusters" es el ideal. (prueben un rango de 1 a 10)
    wss = []
    x_graph = range(1, 11)
    for i in range(1, 11):
        kmeans = KMeans(i)
        kmeans.fit(X_standarized)
        wss.append(kmeans.inertia_)
    plt.plot(x_graph, wss)
    plt.title('K-means K vs WSS ')
    plt.xlabel('Número de clusters')
    plt.ylabel('WSS')
    plt.show()
    #5 Basado en la gráfica del "codo" realicen varias gráficas con el número de clusters (unos 3 o 4 diferentes) que Uds creen mejor se ajusten a los datos.
    k = ideal_k
    for _ in range(4):
        kmeans = KMeans(k)
        kmeans.fit(X_standarized)
        clusters = kmeans.fit_predict(X_standarized)
        data_sec1_5 = data.copy()
        data_sec1_5["Cluster"] = clusters
        data_sec1_5["Cluster"] =data_sec1_5["Cluster"].astype("category")
        fig = px.scatter(data_sec1_5, x = feature_1, y = feature_2, color = "Cluster", hover_data = ['Cluster'])
        fig.update_xaxes(range=[min_sepal_length, max_sepal_length])
        fig.update_yaxes(range=[min_sepal_width, max_sepal_width])
        fig.show()
    # 6 Comparacion con la data real
    categorized_data = pd.read_csv(f"{DATA_PATH}/iris-con-respuestas.csv")
    categorized_data["species"] = categorized_data["species"].astype("category")
    fig = px.scatter(categorized_data, x = feature_1, y = feature_2, color = "species", hover_data = ['species'])
    fig.update_xaxes(range=[min_sepal_length, max_sepal_length])
    fig.update_yaxes(range=[min_sepal_width, max_sepal_width])
    fig.show()

def get_optimal_k(feature_1, feature_2):
    DATA_PATH = "./data" 
    data = pd.read_csv(f"{DATA_PATH}/iris.csv")
    X = data.filter([feature_1, feature_2])
    scaler = StandardScaler()
    X_standarized = X.copy()
    X_standarized[X_standarized.columns] = scaler.fit_transform(X_standarized[X_standarized.columns])

    wss = []
    x_graph = range(1, 11)
    for i in range(1, 11):
        kmeans = KMeans(i)
        kmeans.fit(X_standarized)
        wss.append(kmeans.inertia_)
    kl = KneeLocator(x_graph, wss, curve="convex", direction="decreasing")
    optimal_k = kl.elbow
    print(f"El k optimo encontrado para el clustering con {feature_1} y {feature_2}: {optimal_k}")

if __name__ == "__main__":
    # iris_clustering("sepal_length", "sepal_width", 3) #Seccion 1
    # iris_clustering("petal_length", "petal_width", 3) #Seccion 2
    get_optimal_k("petal_length", "petal_width")# section 3
