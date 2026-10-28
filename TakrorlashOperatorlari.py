# Summa=0
# for i in range(1,101):
#     Summa+=i
# print("1 dan 100 gacha sonlar yig'indisi=",Summa)
# Suz="SALOM DUNYO"
# for i in Suz:
#     print(i)
#     i=1
#     while i<=10:
#         print(i)
#         i+=1
#     print("1 dan 10 gacha sonlar chiqarildi")
# OqYaktakli = 0
# KukYaktakli = 0
# vaqt = 0
# while True:
#         vaqt+=1
#         KukYaktakli+=int(input("Kuk yaktakli bali: "))
#         OqYaktakli+=int(input("Oq yaktakli bali: "))
#         if vaqt<=300:
#             if KukYaktakli>=100:
#                 print ("Kuk yaktakli G'olib bo'ldi")
#                 break
#             if OqYaktakli>=100:
#                 print ("Oq yaktakli G'olib bo'ldi")
#                 break
#         else:
#          KukYaktakli+=int(input("Kuk yaktakli bali: "))
#          OqYaktakli+=int(input("Oq yaktakli bali: "))   
#          if KukYaktakli>=0:
#                          print ("Kuk yaktakli G'olib bo'ldi")
#                          break
#          if OqYaktakli>=0:
#                          print ("Oq yaktakli G'olib bo'ldi")
# while True:
#     try:
#            n = int(input("Musbat son kiriting: "))
#     except ValueError:
#            print("Butun son kiriting!")
#            continue
#     if n < 0:
#         print("Musbat bo'lsin!")
#     print("Qabul qilindi:", n)
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