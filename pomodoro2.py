import time
import datetime
def pomodoros(x):
    today = datetime.datetime.now()
    timepomodoro = datetime.timedelta(minutes=x)
    Limit_Time = today + timepomodoro
    Round = 0

    input("PRESS ENTER")
    while datetime.datetime.now() <= ( Limit_Time ):
        time.sleep(60)
        print(datetime.datetime.now().strftime('%I:%M %p'))
    print ("First Round complete")
    Round +=1
    if Round == 1:
        print("Five minutes break")
    mins = 0
    while mins != 5:
        time.sleep(60)
        mins += 1
        print(str(mins) + " minutes")
    print (" Do you want to continue, Yes or No")
    answer = input()
    if answer == "no":
        return ("congratulation you did " + str(Round) + " Round")
    if answer == "yes":
        print("ok let's go")
        Round += 1
    else:
        print("please write a valid answer")

    while answer == "yes":
        pomodoros(x)
     
pomodoros(5)
