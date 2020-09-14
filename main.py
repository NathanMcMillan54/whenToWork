import time
import os

t = time.localtime()
# 'a' is for short name of week day, 'd' is for day of month, 'B' is for month name, 'Y' is for year number
date = time.strftime("%a, %d, %B, %Y", t)

print("Current date: ", date)
time.sleep(1)

Nf = open("textFiles/userName.txt").read()
COf = open("textFiles/companyName.txt").read()
print(Nf, "working at", COf)

time.sleep(1)

p1 = input("Input project: ")
p1I = input("Input number between 1 and 10: ")

while True:
    print(p1)
    if p1I > 7:
        print("Work for 60 minutes")
        time.sleep(3600)
        os.system('sh beep.sh')
        print("Stop")
        exit()
    elif p1I < 4:
        print("Work for 30 minutes")
        time.sleep(1800)
        os.system('sh beep.sh')
        print("Stop")
        exit()
