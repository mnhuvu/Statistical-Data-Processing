import numpy as np
from scipy import stats

def t_test(data1, data2, confidence_level, test_type):
    n1 = len(data1)
    n2 = len(data2)
    alpha = 1 - confidence_level

    #Tinh phuong sai mau, trung binh mau
    var_sample1 = np.var(data1, ddof=1)
    var_sample2 = np.var(data2, ddof=1)
    mean_sample1 = np.mean(data1)
    mean_sample2 = np.mean(data2)

    #Thong ke kiem dinh khi chua biet phuong sai tong the
    T0= (mean_sample1 - mean_sample2) / np.sqrt((var_sample1 / n1 + var_sample2 / n2))

    #Bac tu do
    x = var_sample1 / n1
    y = var_sample2 / n2
    df = ((x + y) ** 2) / ((x ** 2 / (n1 - 1)) + (y ** 2 / (n2 - 1)))

    #p-value
    P = stats.t.cdf(T0, df)
    if test_type == "=":
        p_value = 2 * min(1 - P, P)
    elif test_type == ">":
        p_value = 1 - P
    elif test_type == "<":
        p_value = P
    else:
        raise ValueError("Nhập sai loại kiểm định. Vui lòng nhập lại")

    #Ket luan
    if p_value < alpha:
        ketLuan = "Có bằng chứng để bác bỏ giả thuyết H0"
    else:
        ketLuan = "Không có bằng chứng để bác bỏ giá thuyết H0"

    result = {
        "Phương sai mẫu 1": var_sample1,
        "Trung bình mẫu 1": mean_sample1,
        "Phương sai mẫu 2": var_sample2,
        "Trung bình mẫu 2": mean_sample2,
        "Loại kiểm định": test_type,
        "p-value": p_value,
        "Mức ý nghĩa:": alpha,
        "Kết luận": ketLuan
    }

    return result

def z_test(data1, data2, confidence_level, sd1, sd2, test_type):
    n1 = len(data1)
    n2 = len(data2)
    alpha = 1 - confidence_level
    var1 = sd1 ** 2
    var2 = sd2 ** 2

    #Tinh phuong sai mau, trung binh mau
    var_sample1 = np.var(data1, ddof = 1)
    var_sample2 = np.var(data2, ddof = 1)
    mean_sample1 = np.mean(data1)
    mean_sample2 = np.mean(data2)

    #Thong ke kiem dinh khi da biet phuong sai tong the
    z0 = (mean_sample1 - mean_sample2) / np.sqrt(var1 / n1 + var2 / n2)

    #Tinh p-value
    P = stats.norm.cdf(z0)
    if test_type == "=":
        p_value = 2 * min(1 - P, P)
    elif test_type == ">":
        p_value = 1 - P
    elif test_type == "<":
        p_value = P
    else:
        raise ValueError("Nhập sai loại kiểm đinh. Vui lòng nhập lại")

    #Ket luan
    if p_value < alpha:
        ketLuan = "Có bằng chứng để bác bỏ giả thuyết H0"
    else:
        ketLuan = "Không có bằng chứng để bác bỏ giá thuyết H0"

    result = {
        "Phương sai mẫu 1": var_sample1,
        "Trung bình mẫu 1": mean_sample1,
        "Phương sai mẫu 2": var_sample2,
        "Trung bình mẫu 2": mean_sample2,
        "Loại kiểm định": test_type,
        "p-value": p_value,
        "Mức ý nghĩa:": alpha,
        "Kết luận": ketLuan
    }

    return result

#Chay thu
data1 = [24, 32, 32, 21, 28, 29, 26, 31]
data2 = [17, 20, 28, 32, 21, 27, 28, 29]
confident_level = 0.95
sd1 = 3
sd2 = 2
test_type = "="
x = t_test(data1, data2, confident_level, test_type)
print(x)
y = z_test(data1, data2, confident_level, sd1, sd2, test_type)
print(y)