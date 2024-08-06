import numpy as np
from scipy import stats

def var_test(data, sd, test_type, confidence_level = 0.95):
    n = len(data)
    alpha = 1 - confidence_level
    df = n - 1

    #Tinh phuong sai mau
    var = np.var(data, ddof=1)

    # Tinh epsilon
    e1 = stats.chi2.ppf(alpha / 2, df)
    e2 = stats.chi2.ppf(1 - alpha / 2, df)

    #Tinh chi binh phuong
    chiSquare = df * var / (sd ** 2)

    #Tinh p-value
    if test_type == "<":
        p_value = stats.chi2.cdf(chiSquare, df)
        khoangTinCay = [0, stats.chi2.ppf(1 - alpha, df)]
    elif test_type == ">":
        p_value = 1 - stats.chi2.cdf(chiSquare, df)
        khoangTinCay = [stats.chi2.ppf(alpha, df), np.inf]
    elif test_type == "=":
        p_value = 2 * min(1 - stats.chi2.cdf(chiSquare, df), stats.chi2.cdf(chiSquare, df))
        khoangTinCay = e1, e2
    else:
        raise ValueError("Nhập sai loại kiểm định. Vui lòng nhập lại")


    #Ket luan
    if p_value < alpha:
        ketLuan = "Có bằng chứng để bác bỏ giả thuyết H0"
    else:
        ketLuan = "Không có bằng chứng để bác bỏ giả thuyết H0"

    result = {
        "Loại kiểm đinh": test_type,
        "p-value": p_value,
        "Bậc tự do": df,
        "Khoảng tin cậy": khoangTinCay,
        "Kết luận": ketLuan
    }

    return result


#Chay thu:
data = [10, 12, 14, 15, 18, 20, 21, 22, 24, 25]
sd = 5
test_type = "="
confident_level = 0.95

result = var_test(data, sd, test_type, confident_level)
print(result)