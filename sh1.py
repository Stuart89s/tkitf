
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import random
from kneed import KneeLocator

class vassal:
    def __init__(self, loyalty, life, greed) -> None:
        self.loyalty = loyalty
        self.life = life
        self.greed = greed

vassals = [vassal(random.random(), random.random(), random.random()) for _ in range(300)]

loyalty = [v.loyalty for v in vassals]
greed = [v.greed for v in vassals]

# numpy 배열로 변환
data = np.array(list(zip(loyalty, greed)))

# WCSS 계산
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)

# KneeLocator로 최적의 K 찾기
kn = KneeLocator(range(1, 11), wcss, curve='convex', direction='decreasing')
optimal_k = kn.knee

# 최적의 K 값으로 K-평균 클러스터링을 수행하고 결과를 시각화합니다.
kmeans = KMeans(n_clusters=optimal_k, init='k-means++', max_iter=300, n_init=10, random_state=0)
clusters = kmeans.fit_predict(data)

plt.scatter(data[:, 0], data[:, 1], c=clusters, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.title(f'K-Means Clustering with k={optimal_k}')
plt.show()