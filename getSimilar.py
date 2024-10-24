import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from sentence_transformers import SentenceTransformer
from scipy.cluster.hierarchy import fcluster
import numpy as np
import csv
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import defaultdict
import translate

file_path = translate.getOuput()
articles = pd.read_csv(file_path)

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(articles['Data'], show_progress_bar=True)

Z = linkage(embeddings, 'ward')

threshold = 1.0
cluster_labels = fcluster(Z, threshold, criterion='distance')

articles['hierarchical_cluster'] = cluster_labels

def find_optimal_clusters(data, max_k):
    iters = range(2, max_k+1)
    s = []

    for k in iters:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        s.append(silhouette_score(data, kmeans.labels_))

    return iters[np.argmax(s)], s

# Tìm số lượng cụm tối ưu
optimal_k_silhouette, silhouette_scores = find_optimal_clusters(embeddings, 20)
km = KMeans(n_clusters=optimal_k_silhouette, random_state=42)
km.fit(embeddings)
articles['cluster'] = km.labels_


output_file_path = 'output.csv'
output_dir = ''
if(translate.getContent.getLink.getTag() == "1002565"):
    output_dir = 'thethao_'
    output_file_path = 'thethao_output.csv'

articles.to_csv(output_file_path, index=False)

csv_file_path = output_file_path
namefile = []
grouped_data = defaultdict(lambda: defaultdict(list))

with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader) 
    for row in csv_reader:
        group_number = row[2]
        order_number = row[1]
        text = row[0]
        grouped_data[group_number][order_number].append(text)

# Ghi dữ liệu vào các file text 
for group, orders in grouped_data.items():
    for order, texts in orders.items():
        if texts:  
            output_file_path = f"{output_dir}group_{group}_order_{order}.txt"
            namefile.append(output_file_path)
            with open(output_file_path, mode='w', encoding='utf-8') as outfile:
                outfile.write(' ||||| '.join(texts))

def getNameFile():
    return namefile