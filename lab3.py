import math
import scipy.stats as ss

#Tim trung binh va do lech chuan bang lab 1
def mean_var(data):
    n = len(data)
    tb_mau = sum(data) / n
    deviations = ((x - tb_mau) ** 2 for x in data)
    ps_mau = sum(deviations) / (n-1)
    return tb_mau, ps_mau

def tkkd(data, muy, loaiKD, doTinCay=0.95):
    n = len(data)
    alpha = 1 - doTinCay
    bacTuDo = n - 1

    tb_mau, ps_mau = mean_var(data)

    # Tinh thong ke kiem dinh
    t0 = (tb_mau-muy)/(math.sqrt(ps_mau)/math.sqrt(n))

    #Tinh epsilon
    epsilon = ss.t.ppf(1-alpha/2, n-1)

    #Tinh p-value
    P = ss.t.cdf(abs(t0), n-1)
    if loaiKD == "<":
        p_value = P
    elif loaiKD == ">":
        p_value = 1 - P
    elif loaiKD == "=":
        p_value = 2 * (1-P)
    else:
        raise ValueError("Nhap sai loai kiem dinh. Vui long nhap lai")

    print("Trung binh: " + str(tb_mau))
    print("p-value: " + str(p_value))
    print("Loai KD: " + loaiKD)
    print("Khoang tin cay: " + '[' + str(tb_mau - epsilon) + ', ' + str(tb_mau + epsilon) + ']')

#Chay thu:
data = [1, 2, 3, 4, 5]
muy = 5
loaiKD = ">"
doTinCay = 0.95

result = tkkd(data, muy, loaiKD, doTinCay)
print(result)



