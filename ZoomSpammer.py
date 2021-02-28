#this program is to spam in Zoom chatbox


import pyautogui as pg 


def texter(x, y, n, text):     #(x,y) = position, n= number of hit
    #pg.click(x, y)
    for i in range(n):
        pg.click(x, y)
        pg.write(text)

        pg.press('Enter', interval = 0 )
        #pg.click(0,0)/////// #if enter to sent not works 



while(True):
    text = input("Enter the text: ")
    n = input("Enter Number of hit : ")
    t = input("time delay in second: ")
    (x,y) = pg.position()
    

    texter(x, y, int(n), text)






