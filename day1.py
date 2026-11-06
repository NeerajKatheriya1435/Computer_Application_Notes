
with open("student.txt", "w") as file:
    file.write("Roll No: 101\n")
    file.write("Name: Rahul\n")
    file.write("Course: BBA\n")
with open("student.txt", "r") as file:
    data = file.read() # Reading data from the filewith
    print(data)