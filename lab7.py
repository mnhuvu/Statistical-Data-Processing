import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.stats as stats
import statistics as st
import pandas as pd

def lab7(data, type_of_bin):
    min_val = min(data)
    max_val = max(data)

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
        K = 1 + np.log2(n) + nplog2(1 + abs(skewness) / sigma_g1)
    elif type_of_bin == "Freedman-Diaconis's Rule":
        IQR = stats.iqr(data, rng = (25, 75), scale = "raw", nan_policy = "omit")
        K = 2 * IQR * n ** (-1 / 3)
    K = math.floor(K)
    return K

    #Tính bảng tần suất dạng khoảng
    intervalLength = (max_val - min_val) / k
    intervals = [(min_val + i * intervalLength, min_val + (i + 1) * intervalLength) for i in range(K)]

    frequencyTable = {interval: 0 for interval in intervals}
    for val in data:
        for interval in intervals:
            if interval[0] <= val < interval[1]:
                frequencyTable[interval] += 1

    return frequencyTable

# Phân phối chuẩn
normal_distribution = np.random.normal(0, 1, 1000)
num_bins = lab7(normal_distribution, "Sturge's Rule")
counts, bin_edges = np.histogram(normal_distribution, bins=num_bins)
labels = [f'{bin_edges[i]} - {bin_edges[i+1]}' for i in range(num_bins)]
df = pd.DataFrame({'Bin_Range': labels, 'Frequency': counts})
print(df)

bin_width = bin_edges[1] - bin_edges[0]

# Vẽ biểu đồ bar liên tục
plt.bar(bin_edges[:-1], counts, width=bin_width, edgecolor='blue')
plt.title('Continuous Bar Chart')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Vẽ histogram
plt.hist(normal_distribution, bins=num_bins, edgecolor='blue')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

#Phân phối đều
uniform = np.random.uniform(0, 2, 1000)
num_bins = lab7(uniform,"Sturge's Rule")
counts, bin_edges = np.histogram(uniform, bins=num_bins)
labels = [f'{bin_edges[i]} - {bin_edges[i+1]}' for i in range (num_bins)]
df = pd.DataFrame({'Bin_Range': labels, 'Frequency': counts})
print(df)
bin_width = bin_edges[1] - bin_edges[0]

# Vẽ biểu đồ bar liên tục
plt.bar(bin_edges[:-1], counts, width=bin_width, edgecolor='blue')
plt.title('Continuous Bar Chart')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

#Phân phối Cauchy
cauchy = np.random.standard_cauchy(1000)
num_bins =lab7(cauchy,"Sturge's Rule")
counts, bin_edges = np.histogram(cauchy, bins=num_bins)
labels = [f'{bin_edges[i]} - {bin_edges[i+1]}' for i in range (num_bins)]
df = pd.DataFrame({'Bin_Range': labels, 'Frequency': counts})
print(df)
bin_width = bin_edges[1] - bin_edges[0]

# Vẽ biểu đồ bar liên tục
plt.bar(bin_edges[:-1], counts, width=bin_width, edgecolor='blue')
plt.title('Continuous Bar Chart')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

#Phân phối fisher
fisher = np.random.f(10, 20, 1000)
num_bins =lab7(fisher,"Sturge's Rule")
counts, bin_edges = np.histogram(fisher, bins=num_bins)
labels = [f'{bin_edges[i]} - {bin_edges[i+1]}' for i in range (num_bins)]
df = pd.DataFrame({'Bin_Range': labels, 'Frequency': counts})
print(df)
bin_width = bin_edges[1] - bin_edges[0]

# Vẽ biểu đồ bar liên tục
plt.bar(bin_edges[:-1], counts, width=bin_width, edgecolor='blue')
plt.title('Continuous Bar Chart')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

#Phân phối Chi bình phương
chi_square = np.random.chisquare(2, 10000)
num_bins =lab7(chi_square,"Sturge's Rule")
counts, bin_edges = np.histogram(chi_square, bins=num_bins)
labels = [f'{bin_edges[i]} - {bin_edges[i+1]}' for i in range (num_bins)]
df = pd.DataFrame({'Bin_Range': labels, 'Frequency': counts})
print(df)
bin_width = bin_edges[1] - bin_edges[0]

# Vẽ biểu đồ bar liên tục
plt.bar(bin_edges[:-1], counts, width=bin_width, edgecolor='blue')
plt.title('Continuous Bar Chart')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()




