import time

while True:
    t0=time.time()
    inputtext=str(input('Start Typing:'))
    t1=time.time()
    wordcount=len(inputtext.split())
    timetaken=t1-t0
    wpm=wordcount/timetaken
    print("WPM=",wpm,"Timetaken=",timetaken)