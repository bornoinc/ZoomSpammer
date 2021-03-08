#this program is to spam in chatbox
 
 
import pyautogui as pg 
import keyboard
 
 
def texter(x, y, n, text, t):     #(x,y) = position, n= number of hit
    #pg.click(x, y)
    for i in range(n):
        pg.click(x, y)
        pg.write(text)
 
        pg.press('Enter', interval = t )
        #pg.click(0,0)/////// #if enter to sent not works 
 
 
 
while(True):
    print ("Put Your curson on chat box and press 'tab'")
 
    if keyboard.read_key() == "tab":
        print("You pressed p")
        (x,y) = pg.position()
        print (x , y)
        text = input("Enter the text: ")
        n = input("Enter Number of hit : ")
        t = input("time delay in second: ")
 
 
 
        texter(x, y, int(n), text, t)
