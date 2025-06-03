soat = int(input("Soatni kiriting (0-23): "))

if 0 <= soat <= 23:
    if 5 <= soat <= 11:
        print("Ertalab")
    elif 12 <= soat <= 17:
        print("Kunduzi")
    elif 18 <= soat <= 21:
        print("Kechqurun")
    else:
        print("Tun")
else:
    print("Soat 0-23 oralig'ida bo'lishi kerak!")
