import time
print('Appuie sur ENTRER pour calculer ton temps')
startTime = time.time()
lastTime = startTime
lapNum = 1
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('rep #%s: %s (%s)' % (lapNum, totalTime, lapTime), end="")
        lapNum += 1
        lastTime = time.time() #reset the last lap time
except KeyboardInterrupt:
        #handle the Ctrl-C.
        print('\nDone.')
