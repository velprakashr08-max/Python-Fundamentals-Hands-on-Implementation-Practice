empolyee_file = open("empolyees.txt", "r")
print(empolyee_file.readable())
empolyee_file.close()

empolyee_file = open("empolyees.txt", "r")
print(empolyee_file.readline())
empolyee_file.close()

empolyee_file = open("empolyees.txt", "r")
print(empolyee_file.read())
empolyee_file.close()

empolyee_file = open("empolyees.txt", "r")
print(empolyee_file.readlines())
empolyee_file.close()

empolyee_file = open("empolyees.txt", "r")
print(empolyee_file.readline())
print(empolyee_file.readline())
empolyee_file.close()

empolyee_file = open("employees.txt", "r")
print(empolyee_file.readlines()[[2]])
empolyee_file.close()

empolyee_file = open("empolyees.txt", "w")
print(empolyee_file.readable())
empolyee_file.close()