import os

file_path = "C:/Users/USER/Pictures/error1.png"
print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print("the file exists and has been deleted")

else:
    print("the file does not exist")