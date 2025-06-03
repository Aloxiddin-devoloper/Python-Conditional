import os 

file_name = input()

if os.path.exists(file_name):
    print("fayl mavjud")
else:
    print("File mavjud emas")
