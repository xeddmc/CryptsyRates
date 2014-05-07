# -*- coding: utf-8 -*-
"""
Created on Sun May  4 14:28:55 2014

@author: chris
"""
#from Tkinter import *
import Cryptsy
import Tkinter
import sys
import webbrowser
global count

coins = dict()
Exchange = Cryptsy.Cryptsy("APIkey", "APIsecret")   
orders = Exchange.api_query("marketdatav2")      
for market in orders['return']['markets']:
    coinpair = orders['return']['markets'][market]['label']
    coins[coinpair]=dict()
    coins[coinpair][0] = (coinpair, 0)
count = 1

cryptsyurl = "https://www.cryptsy.com/markets/view/"
def OpenUrl(url):
    webbrowser.open_new(url)

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def quitfunction(self):
        sys.exit()

    def initialize(self):
        self.frametop = Tkinter.Frame(master = self.master)
        self.frametop.grid(column=0, row=0, columnspan=4)

        self.frame = Tkinter.Frame(master = self.master)
        self.entry = Tkinter.Entry(self.frametop)

        self.frame.grid(column=0, row=1, columnspan=2)
        self.entry.grid(column=0,row=0, columnspan=4, sticky='W')

        self.entry.focus_set()
        self.entry.bind('<Return>', (self.get_coins))
        
        ratesbutton = Tkinter.Button(self.frametop, text="Get Rates", command=self.get_coins)
        ratesbutton.grid(column=5,row=0, columnspan=2, sticky='W')

        quitbutton = Tkinter.Button(self.frametop,text="Close", command=self.quitfunction)
        quitbutton.grid(column=7,row=0, columnspan=2, sticky='W')
        

        
    def get_coins(self, event=None):
        global count
        
        self.watching = self.entry.get().upper().split()
		
        self.frame.grid_forget()

        self.frame = Tkinter.Frame(master = self.master)
        self.frame.grid(column=0, row=1, columnspan=2)

        self.waiting = Tkinter.Label(master = self.frame, text="Loading Data...")

        self.frame.grid(column=0, row=1, columnspan=2)
        self.waiting.grid(column=0, row=1, columnspan=2)
        self.update()

        watchedcoins = []
        Exchange = Cryptsy.Cryptsy("APIkey", "APIsecret")   
        orders = Exchange.api_query("marketdatav2")           
        
        self.frame.grid_forget()

        self.frame = Tkinter.Frame(master = self.master)
        self.frame.grid(column=0, row=1, columnspan=2)


        for market in orders['return']['markets']:
            coinpair = orders['return']['markets'][market]['label']
            marketid = orders['return']['markets'][market]['marketid']
            try:            
                buyorders = orders['return']['markets'][market]['buyorders'][0:3]
            except:
                buyorders = "No Buy Orders"     
            try:
                price = str(buyorders[0]['price'])
                price = float(price)
            except:
                price = 0.00000000
            coins[coinpair][count] = (coinpair, price, marketid)
            if count > 2:
                del coins[coinpair][count-2]
            else:
                pass
        for coinpair in sorted(coins.keys()):
            if coins[coinpair][count][0].split("/")[0] in self.watching or coins[coinpair][count][0].split("/")[1] in self.watching:
                watchedcoins.append(coinpair)
        totalcoins = len(watchedcoins)
        rows = totalcoins//4+1
        if  0 !=  (rows % 2) :
            rows= totalcoins//4+1
        
        n=1        
        for coinpair in sorted(watchedcoins):
            abDiff = float((coins[coinpair][count][1]-coins[coinpair][count-1][1]))
            if abDiff > float(0.00000000):
                fgc = "darkgreen"
                Diff = "+ %.8f" % abs(abDiff)
            elif abDiff < float(0.00000000):
                fgc = "red"
                Diff = "- %.8f" % abs(abDiff)
            elif abDiff == float(0.00000000):
                fgc="darkslategrey"
                Diff = "%.8f" % abDiff
                
            if n <=rows:
                self.L = Tkinter.Button(master = self.frame, text = coins[coinpair][count][0], bd=0, height=1, command=lambda aurl=str(cryptsyurl+coins[coinpair][count][2]) :OpenUrl(aurl))     
                self.L.grid(column=0, row=n)
                
                self.P = Tkinter.Label(master = self.frame, text = "%.8f" % coins[coinpair][count][1])     
                self.P.grid(column=1, row=n)
                
                self.D = Tkinter.Label(master = self.frame, text = "%s" % Diff, fg=fgc)
                self.D.grid(column=2, row=n)
            elif rows <= n <=rows*2:
                self.L = Tkinter.Button(master = self.frame, text = coins[coinpair][count][0], bd=0, height=1, command=lambda aurl=str(cryptsyurl+coins[coinpair][count][2]) :OpenUrl(aurl)) 
                self.L.grid(column=4, row=n-rows)

                self.space = Tkinter.Label(master = self.frame, text=" ")
                self.space.grid(column=3, row=n-rows)

                self.P = Tkinter.Label(master = self.frame, text = "%.8f" % coins[coinpair][count][1])     
                self.P.grid(column=5, row=n-rows)
                
                self.D = Tkinter.Label(master = self.frame, text = "%s" % Diff, fg=fgc)
                self.D.grid(column=6, row=n-rows)
            elif rows*2 <= n <= rows*3:
                self.L = Tkinter.Button(master = self.frame, text = coins[coinpair][count][0], bd=0, height=1, command=lambda aurl=str(cryptsyurl+coins[coinpair][count][2]) :OpenUrl(aurl)) 
                self.L.grid(column=8, row=n-rows*2)
                
                self.space = Tkinter.Label(master = self.frame, text=" ")
                self.space.grid(column=7, row=n-rows*2)

                self.P = Tkinter.Label(master = self.frame, text = "%.8f" % coins[coinpair][count][1])     
                self.P.grid(column=9, row=n-rows*2)
                
                self.D = Tkinter.Label(master = self.frame, text = "%s" % Diff, fg=fgc)
                self.D.grid(column=10, row=n-rows*2)
            elif rows*3 <= n <= rows*4:
                self.L = Tkinter.Button(master = self.frame, text = coins[coinpair][count][0], bd=0, height=1, command=lambda aurl=str(cryptsyurl+coins[coinpair][count][2]) :OpenUrl(aurl)) 
                self.L.grid(column=12, row=n-rows*3)
                
                self.space = Tkinter.Label(master = self.frame, text=" ")
                self.space.grid(column=11, row=n-rows*3)

                self.P = Tkinter.Label(master = self.frame, text = "%.8f" % coins[coinpair][count][1])     
                self.P.grid(column=13, row=n-rows*3)

                self.D = Tkinter.Label(master = self.frame, text = "%s" % Diff, fg=fgc)
                self.D.grid(column=14, row=n-rows*3)
            elif rows*4 <= n :
                self.L = Tkinter.Button(master = self.frame, text = coins[coinpair][count][0], bd=0, height=1, command=lambda aurl=str(cryptsyurl+coins[coinpair][count][2]) :OpenUrl(aurl)) 
                self.L.grid(column=16, row=n-rows*4)
                
                self.space = Tkinter.Label(master = self.frame, text=" ")
                self.space.grid(column=15, row=n-rows*4)

                self.P = Tkinter.Label(master = self.frame, text = "%.8f" % coins[coinpair][count][1])     
                self.P.grid(column=17, row=n-rows*4)

                self.D = Tkinter.Label(master = self.frame, text = "%s" % Diff, fg=fgc)
                self.D.grid(column=18, row=n-rows*4)
            
            n+=1

        self.T = Tkinter.Label(master = self.frame, text = "Markets: %s" % totalcoins, fg="Black")
        self.T.grid(column=13, row=rows)        
        self.update()
        count +=1        

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('CryptsyRates v1.1')
    app.resizable(1,1)
    app.mainloop()
