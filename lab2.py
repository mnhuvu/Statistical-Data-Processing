def tansuat(data, k):
    data.sort()

    min_val = min(data)
    max_val = max(data)
    doDaiKhoang = (max_val - min_val) / k
    khoang = [(min_val + i * doDaiKhoang, min_val + (i + 1) * doDaiKhoang) for i in range(k)]

    bangTanSuat = {khoang_con: 0 for khoang_con in khoang}
    for giaTri in data:
        for khoang_con in khoang:
            if khoang_con[0] <= giaTri < khoang_con[1]:
                bangTanSuat[khoang_con] += 1

    return bangTanSuat

data = [int(i) for i in input("Nhap mang: ").split()]
k = int(input("Nhap do rong k: "))

bangTanSuat = tansuat(data, k)
for khoang_con, tanSuat in bangTanSuat.items():
    print(f"Khoang {khoang_con}: Tan suat = {tanSuat}")
