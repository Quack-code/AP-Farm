from time import sleep
import sys
import keyboard 
import random
import pyautogui 
import pygetwindow
import threading
import math
import numpy as np
from scipy import interpolate

lock=threading.Lock

def main():

    print('\nTo end the program : press Q for 3 sec')
    print('Starting bot')
    sleep(2)

    # check if valorant is active than run
    try:
        checkForValorant()
        sleep (1)
        global bot_flag
        bot_flag= True
        # came here means valo is active
        t1=threading.Thread(target=botControl)
        t2=threading.Thread(target=queue)
        t3=threading.Thread(target=animate)
        t1.start()
        t2.start()
        sleep(10)
        t3.start()       
    except:
        print('Something went wrong')
# end of main function

def botControl():
    global bot_flag
    global in_game
    while bot_flag == True:
        sleep(3)
        if keyboard.is_pressed('q'):
            bot_flag = False
            in_game = False
            print ('\n Bot has stopped')
            return


def checkForValorant():
    # get list of active windows with name = VALORANT
    list = pygetwindow.getWindowsWithTitle('VALORANT')
    # check 
    if len(list) == 0 :
        print('\n   Valorant is Not active')
        print('Exiting in 4 sec ',end='')
        for i in range(2):
            sleep(1)
            print('. ',end='')
        sys.exit()
    else:
        print ('VALORANT found', list)
        valorant = list[0]
        valorant.restore() #run



def queue():
    while bot_flag==True:
       print ('attempting to queue')
       x,y= (789,1017)
       r,g,b = pyautogui.pixel(x, y)
       checkrgb(r,g,b) #checks if the x,y matches something
       sleep(1)
       if matchrgb == True:
            print ('Start button found')
            points,delay = getMovePoints(x,y)
            movemouse(points,delay)
            pyautogui.click()
            sleep(30)
       elif matchrgb == False:
            print('Start button not found, checking to see if already in-game')
            sleep (.5)
            inGameCheck()
            if in_game==True:
                print('Already in-game, waiting 30 secounds')
                sleep(30)
            else:
                print('Could not determine if in-game, seeing if waiting to start again')
                x,y=(814,1058)
                r,g,b = pyautogui.pixel(x,y)
                print(r,g,b)
                checkrgb(r,g,b)
                if matchrgb == True:
                    print('Found play again button')
                    points,delay = getMovePoints(x,y)
                    movemouse(points,delay)
                    pyautogui.click()
                else:
                    print('Could not find any button')
                sleep(10)


def inGameCheck():
    x,y = (959,539) #center of screen
    r,g,b = pyautogui.pixel(x,y)
    checkrgb(r,g,b)
    global in_game
    if matchrgb == True:
        print('In-game')       
        in_game = True
    else:
        print('Not in-game')
        in_game = False
        
def animate():
    global bot_flag
    while bot_flag ==True:
        print('Animation checking in-game')        
        inGameCheck()
        sleep(5)
        if in_game == True:
            buygun()      
            while in_game == True:
                print('Animation Started')
                sleep(1)
                playermovement()




def playermovement():
    global bot_flag
    while bot_flag and in_game == True:
        movement_list = ['a','w','s','d'] #list of movement we can do
        choice = random.randint(1,2) #choose a random number
        rkey = random.sample(movement_list, choice) #pick random movement amounts and time, then press them randomly
        delay = random.uniform(1,5)
        print(rkey, delay)
        keyboard.press(rkey)
        sleep(delay)
        keyboard.release(rkey)
        shootandpan()


def buygun(): #from animate    
    print('Buying gun')
    keyboard.send('b')
    sleep(1)
    points,delay = getMovePoints(950,650)
    movemouse(points,delay)
    print('moved')
    pyautogui.click()
    print('clicked')
    sleep(1)
    keyboard.send('b')

def shootandpan():
    x,y = random.randint(1,300),random.randint(1,300)
    points,delay = getMovePoints(x,y)
    panmouse(points,delay)
    pyautogui.click()


def checkrgb(r,g,b): #check if the rgb matches a know pixel of something
    global matchrgb
    if r== 100 and g== 115 and b== 142: #start button color
        matchrgb = True
    elif r== 0 and g==255 and b==255: #crosshair color
        matchrgb = True
    elif r== 255 and g==255 and b==255: #play again button
        matchrgb = True
    else:
        matchrgb = False



def movemouse(points, timeout):
    for point in points:       
        delay=timeout+random.uniform(0,1)*.01
        print(*point, delay)
        pyautogui.moveTo(*point, delay)

def panmouse(points, timeout):
    for point in points:       
        delay=timeout+random.uniform(0,1)*.01
        print(*point, delay)
        pyautogui.dragTo(*point, delay)
        

def getMovePoints(targetx,targety):
    currX,currY = pyautogui.position()
    print(currX,currY)
    print(targetx,targety)
    start=[currX,currY]
    end=[targetx,targety]
    distance = math.dist(start,end)
    controlPoints = random.randint(3,5)
    point_list = []
    # Distribute control points between start and destination evenly.
    x = np.linspace(currX, targetx, num=controlPoints, dtype='int')
    y = np.linspace(currY, targety, num=controlPoints, dtype='int')

    # Randomise inner points a bit (+-RND at most).
    RND = 10
    xr = [random.randint(-RND, RND) for k in range(controlPoints)]
    yr = [random.randint(-RND, RND) for k in range(controlPoints)]
    xr[0] = yr[0] = xr[-1] = yr[-1] = 0
    x += xr
    y += yr

    # Approximate using Bezier spline.
    degree = 3 if controlPoints > 3 else controlPoints - 1  # Degree of b-spline. 3 is recommended.
                                      # Must be less than number of control points.
    tck, u = interpolate.splprep([x, y], k=degree)
    # Move upto a certain number of points
    u = np.linspace(0, 1, num=2+int(distance/50.0))
    points = interpolate.splev(u, tck)

    # Move mouse.
    timeout = random.uniform(0,1) / len(points[0])
    point_list=zip(*(i.astype(int) for i in points))
    return point_list, timeout

       
        #rgb(100,115,142)
        #(959,1000)
        # 9)buy gun x,y(950, 750)
        #center of screen rgb (0,255,255)

#Calling main function
if __name__ == "__main__":
    main()