userName = input("What is your name? ")
Nf = open("textFiles/userName.txt", "w")
Nf.read()
Nf.writelines(userName)
