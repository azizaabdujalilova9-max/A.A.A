# # Sodda hisoblash dasturi
# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi sonni kiriting: "))

# print(f"Yig'indi: {a + b}")
# print(f"Ayirma: {a - b}")
# print(f"Ko'paytma: {a * b}")

# if b != 0:
#     print(f"Bo'linma: {a / b}")
# else:
#     print("Nolga bo'lish mumkin emas!")
sir = 37
urinish = 0
while True:
    try:
        t = int(input("Taxmin: "))
    except ValueError:
        print(" Son kiriting!")
        continue
    urinish += 1
    if t < sir:
        print("Kattaroq")
    elif t > sir:
        print("Kichikroq")
    else:
        print(f"Topdingiz! {urinish} urunishda.")
        break