import time

t = time.localtime()
# 'a' is for short name of week day, 'd' is for day of month, 'B' is for month name, 'Y' is for year number
date = time.strftime("%a, %d, %B, %Y", t)

print("Current date: ", date)
time.sleep(1)

Nf = open("textFiles/userName.txt").read()
COf = open("textFiles/companyName.txt").read()
print(Nf, "working at", COf)

