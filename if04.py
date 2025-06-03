age = int(input())
prace = int(input())

if age < 7:
    print("yakuniy narx:", (prace*50)/100,"so'm","50 foiz chegirma qo'llanildi")

if 7 <= age <= 17:
    print("yakuniy narx:", (prace*20)/100,"so'm","20 foiz chegirma qo'llanildi")

if age >= 18 and age <= 60:
    print("Chegirma qo'llanilmadi")
    
if age > 60:
    print("yakuniy narx:", (prace*50)/100,"so'm","50 foiz chegirma qo'llanildi")
