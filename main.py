import time
import os

t = time.localtime()
# 'a' is for short name of week day, 'd' is for day of month, 'B' is for month name, 'Y' is for year number
date = time.strftime("%a, %d, %B, %Y", t)

print("Current date: ", date)
time.sleep(1)

Nf = open("whenToWork/textFiles/userName.txt").read()
COf = open("whenToWork/textFiles/companyName.txt").read()
print(Nf, "working at", COf)

time.sleep(1)

project = input("Input project: ")
print("Input number between 1 and 10")
projectValue = int(input("1 being not important 10 being very important "))

while True:
    if projectValue > 7:
        print("Work for 60 minutes")
        time.sleep(3600)
        os.system('python whenToWork/stop.py')
        print("Stop")
        exit()
    elif projectValue < 3:
        print("Work for 15 minutes")
        time.sleep(900)
        os.system('python whenToWork/stop.py')
        print("Stop")
        exit()
    elif projectValue == 4:
        print("Work for 30 minutes")
        time.sleep(1800)
        os.system('python whenToWork/stop.py')
        exit()
    elif projectValue == 5:
        print("Work for 45 minutes")
        time.sleep(2700)
        os.system('python whenToWork/stop.py')
        exit()
    elif projectValue == 6:
        print("Work for 45 minutes")
        time.sleep(2700)
        os.system('python whenToWork/stop.py')
        exit()
