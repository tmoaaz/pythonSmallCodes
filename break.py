
import webbrowser
import time

print("Program start from here : "+ time.ctime())

i=0
while (i<4):
	time.sleep(2*60*60)
	webbrowser.open("https://www.youtube.com/watch?v=PoYVGqXuca4")
    i = i+1
print("done")
