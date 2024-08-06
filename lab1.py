import math
import statistics

def mean():
    tb_mau = sum(vecto)/n
    print(f"Trung binh mau la: {tb_mau}")


def variance():
    mean = sum(vecto)/n
    deviations = ((x-mean)**2 for x in vecto)
    ps_mau = sum(deviations)/(n-1)
    print(f"Phuong sai mau la: {ps_mau}")

def standard_deviation():
    mean = sum(vecto)/n
    deviations = ((x-mean)**2 for x in vecto)
    ps_mau = sum(deviations)/(n-1)
    dlc = math.sqrt(ps_mau)
    print(f"Đo lech chuan la: {dlc}")


def maximum():
    max_val = max(vecto)
    print(f"Gia tri lon nhat la: {max_val}")


def minimum():
    min_val = min(vecto)
    print(f"Gia tri nho nhat la: {min_val}")


def med():
    trungvi = statistics.median(vecto)
    print(f"Trung vi la: {trungvi}")

vecto = [int(i) for i in input("Nhap mang lab 1:").split()]
n = len(vecto)
mean()
variance()
standard_deviation()
maximum()
minimum()
med()

