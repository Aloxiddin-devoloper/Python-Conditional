money = 5000
mahsulot = int(input())

if mahsulot<0:
    print("Manfiy summa kiritib bo'lmaydi")

if 5000 > mahsulot and mahsulot >0:
    print("Pul yechildi. Qolgan balans:", money-mahsulot, "so'm")
if mahsulot >5000 and mahsulot>0:
    print("Mablag' yetarli emas. Sizning balansingiz:",5000, "so'm")

