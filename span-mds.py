import numpy as np
from scipy.sparse import csgraph
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

# Rastgele bir benzersiz graf oluşturmak için nokta koordinatlarını oluşturur
def generate_points(n):
    return np.random.rand(n, 2)

# Öklidyen mesafeyi hesaplar
def euclidean_distance(a, b):
    return np.linalg.norm(a - b)

# Grafı oluşturur ve minimum ağaç üzerinden MDS uygular
def spanning_mds(points):
    n = points.shape[0]

    # Noktalar arasındaki mesafeleri hesaplar
    distances = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            distances[i, j] = euclidean_distance(points[i], points[j])
            distances[j, i] = distances[i, j]

    # Minimum ağacı bulur
    adjacency_matrix = csgraph.minimum_spanning_tree(distances).toarray()

    # MDS uygulanır
    mds = MDS(n_components=2, dissimilarity="precomputed", random_state=42)
    embedded_points = mds.fit_transform(distances)

    return embedded_points, adjacency_matrix

# Nokta koordinatlarını oluşturur
points = generate_points(10)

# Spanning MDS algoritması çağrılır
embedded_points, adjacency_matrix = spanning_mds(points)

# Görselleştirme
plt.figure(figsize=(8, 8))
for i, (x, y) in enumerate(embedded_points):
    plt.scatter(x, y, color='blue', edgecolors='black')
    plt.text(x, y, f'P{i}', fontsize=12, ha='center', va='center')

# Minimum ağacı görselleştirir
for i in range(len(adjacency_matrix)):
    for j in range(i+1, len(adjacency_matrix)):
        if adjacency_matrix[i, j] > 0:
            plt.plot([embedded_points[i, 0], embedded_points[j, 0]],
                     [embedded_points[i, 1], embedded_points[j, 1]],
                     color='red', linewidth=1)

plt.title("Spanning MDS")
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.show()
