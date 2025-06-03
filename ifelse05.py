email = input()

if email[-10] =="@" and email.endswith(".com") or email.endswith(".uz") or email.endswith(".org"):
    print("Email qabul qilindi.")
else:
    print("Email noto'g'ri formatda.")
