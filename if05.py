gradus = int(input("Temperaturani kiriting :"))

if gradus < 0:
    print("juda sovuq ! Issiq kiyim kiying")

if 0 <= gradus <= 14:
    print("Sovuq. Kurtka kiying.")
    
if gradus >= 60:
    print("Ob-havo yaxshi.")