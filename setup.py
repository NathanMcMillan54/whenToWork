userName = input("What is your name? ")
Nf = open("textFiles/userName.txt", "w")
Nf.read()
Nf.writelines(userName)

companyName = input("What company/organization do you work at? ")
COf = open("textFiles/companyName.txt", "w")
COf.read()
COf.writelines(userName)
