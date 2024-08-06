import numpy as np
from scipy.stats import f

def var_test(data1, data2, test_type, alpha = 0.05):
    n1 = len(data1)
    n2 = len(data2)
    df1 = n1 - 1
    df2 = n2 - 1

    #Tim 2 phuong sai mau, 2 trung binh mau
    var_sample1 = np.var(data1, ddof=1)
    var_sample2 = np.var(data2, ddof=1)
    mean_sample1 = np.mean(data1)
    mean_sample2 = np.mean(data2)


    #Thong ke kiem dinh
    F_test = var_sample1 / var_sample2

    # Conclusion:
    if test_type == "<":
        f_critical = f.ppf(alpha, df1, df2)
        if F_test < f_critical:
            conclusion = "Có cơ sở để bác bỏ giả thuyết H0"
        else:
            conclusion = "Chưa đủ cơ sở để bác bỏ giả thuyết H0"
    elif test_type == ">":
        f_critical = f.ppf(1 - alpha, df1, df2)
        if F_test > f_critical:
            conclusion = "Có cơ sở để bác bỏ giả thuyết H0"
        else:
            conclusion = "Chưa đủ cơ sở để bác bỏ giả thuyết H0"
    elif test_type == "=":
        f_critical = [f.ppf(alpha / 2, df1, df2),f.ppf(1 - alpha / 2, df1, df2)]
        if F_test < f_critical[0] or F_test > f_critical[1]:
            conclusion = "Có cơ sở để bác bỏ giả thuyết H0"
        else:
            conclusion = "Chưa đủ cơ sở để bác bỏ giả thuyết H0"

    #Tinh p-value:
    if test_type == "=":
        p_value = 2 * min(1 - f.cdf(F_test, df1, df2), f.cdf(F_test, df1, df2))
    elif test_type == ">":
        p_value = 1 - f.cdf(F_test, df1, df2)
    else:
        p_value = f.cdf(F_test, df1, df2)

    result = {
        "Phương sai mẫu 1": var_sample1,
        "Trung bình mẫu 1": mean_sample1,
        "Phương sai mẫu 2": var_sample2,
        "Trung bình mẫu 2": mean_sample2,
        "f-critical": f_critical,
        "p-value": p_value,
        "Mức ý nghĩa:": alpha,
        "Kết luận": conclusion
    }

    return result

#Chay thu
data1 = [24, 32, 32, 21, 28, 29, 26, 31]
data2 = [17, 20, 28, 32, 21, 27, 28, 29]
test_type = "="
x = var_test(data1, data2, test_type, alpha = 0.05)
print(x)
