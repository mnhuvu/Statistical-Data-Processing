import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.stats as stats
import statistics as st
#Sử dụng gói pandas
import pandas as pd

# 1. Load data -> data frame
data = pd.read_csv('bostonh.csv', sep = '\s+', header = None)
data

# 2. Sử dụng hàm histogram đã viết -> histogram từng cột
def histogram(col, data, type_of_bin):
    #Tính số bin
    n = len(data)
    if type_of_bin == "Sturge's Rule":
        K = 1 + 3.322 * np.log(n)
    elif type_of_bin == "Scott's Rule":
        std = st.stdev(data)
        K = 3.49 * std * n ** (-1 / 3)
    elif type_of_bin == "Rice's Rule":
        K = 2 * (n ** (1 / 3))
    elif type_of_bin == "Doane's Rule":
        skewness = stats.skew(data)
        sigma_g1 = np.sqrt((6 * (n-2)) / ((n + 1) * (n + 3)))
        K = 1 + np.log2(n) + np.log2(1 + abs(skewness) / sigma_g1)
    elif type_of_bin == "Freedman-Diaconis's Rule":
        IQR = stats.iqr(data, rng = (25, 75), scale = "raw", nan_policy = "omit")
        K = 2 * IQR * n ** (-1 / 3)
    K = math.floor(K)
    counts, bin_edges = np.histogram(data, bins= K)
    labels = [f'{bin_edges[i]} - {bin_edges[i + 1]}' for i in range(K)]
    bin_width = bin_edges[1] - bin_edges[0]
    plt.bar(bin_edges[:-1], counts, width=bin_width, edgecolor='blue')
    plt.hist(data, bins=K, edgecolor='blue')
    plt.title('Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

histogram(0, data[0], "Rice's Rule")
histogram(1, data[1], "Rice's Rule")
histogram(2, data[2], "Rice's Rule")
histogram(3, data[3], "Rice's Rule")
histogram(4, data[4], "Rice's Rule")
histogram(5, data[5], "Rice's Rule")
histogram(6, data[6], "Rice's Rule")
histogram(7, data[7], "Rice's Rule")
histogram(8, data[8], "Rice's Rule")
histogram(9, data[9], "Rice's Rule")
histogram(10, data[10], "Rice's Rule")
histogram(11, data[11], "Rice's Rule")
histogram(12, data[12], "Rice's Rule")
histogram(13, data[13], "Rice's Rule")

headers = ['col' + str(i) for i in range(14)]
data.columns = headers
data

#3. Sort tăng dần bằng hàm trong Pandas
sort = data.sort_values(by='col1', ascending = False)
sort

#4. Viết hàm PCA như sau:
#Input: Dataframe, tỷ lệ giữ data
#Thuật toán: BT2/8
#Output: Data đã giảm số chiều
data = np.loadtxt('bostonh.csv')
X_meaned = np.mean(data, axis=0)
h = np.ones((data.shape[0], 1))
B = X - h.dot(X_meaned.reshape(1, -1))
C = B.T.dot(B)
eigen_values, eigen_vectors = np.linalg.eigh(C)
sorted_index = np.argsort(eigen_values)[::-1]
sorted_eigenvalues = eigen_values[sorted_index]
sorted_eigenvectors = eigen_vectors[:, sorted_index]
cum_eigen_values_ratio = np.cumsum(eigen_values) / np.sum(eigen_values)
PCA_threshold = 0.9
num_vectors = np.argmax(cum_eigen_values_ratio >= PCA_threshold) + 1
W = eigen_vectors[:, :num_vectors]
W
T = B.dot(W)
T


