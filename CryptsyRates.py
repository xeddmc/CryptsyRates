# -*- coding: utf-8 -*-
"""
Created on Sun May  4 14:28:55 2014

@author: chris
"""
#from Tkinter import *
import Cryptsy
import Tkinter
import sys
class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        
    def quitfunction(self):
        sys.exit()

    def initialize(self):
        self.frame = Tkinter.Frame(master = self.master)
        self.entry = Tkinter.Entry(self)

        self.frame.grid(column=0, row=1, columnspan=2)
        self.entry.grid(column=0,row=0,sticky='N')

        self.entry.focus_set()
        self.entry.bind('<Return>', (self.get_coins))
        
        ratesbutton = Tkinter.Button(self,text="Get Rates", command=self.get_coins)
        ratesbutton.grid(column=1,row=0)

        quitbutton = Tkinter.Button(self,text="Close", command=self.quitfunction)
        quitbutton.grid(column=2,row=0)
        
    def get_coins(self, event=None):
        self.watching = self.entry.get().upper().split()
        self.frame.grid_forget()

        self.frame = Tkinter.Frame(master = self.master)
        self.frame.grid(column=0, row=1, columnspan=2)

        self.waiting = Tkinter.Label(master = self.frame, text="Loading Data...")

        self.frame.grid(column=0, row=1, columnspan=2)
        self.waiting.grid(column=0, row=1, columnspan=2)
        self.update()

        coins = []
        watchedcoins = []
        Exchange = Cryptsy.Cryptsy("APIkey", "APIsecret")   
        orders = Exchange.api_query("marketdatav2")           
        
        self.frame.grid_forget()

        self.frame = Tkinter.Frame(master = self.master)
        self.frame.grid(column=0, row=1, columnspan=2)


        for market in orders['return']['markets']:
            coinpair = orders['return']['markets'][market]['label']
            try:            
                buyorders = orders['return']['markets'][market]['buyorders'][0:3]
            except:
                buyorders = "No Buy Orders"     
            try:
                price = str(buyorders[0]['price'])
                price = float(price)
            except:
                price = 0.00000000
            
            coins.append((coinpair,price))
        for coinpair in sorted(coins):
            if coinpair[0].split("/")[0] in self.watching or coinpair[0].split("/")[1] in self.watching:
                watchedcoins.append(coinpair)
        n=1        
        for coinpair in sorted(watchedcoins):
            if n <=40:
                self.L = Tkinter.Label(master = self.frame, text = coinpair[0])     
                self.L.grid(column=0, row=n)

                self.P = Tkinter.Label(master = self.frame, text = "%.8f" % coinpair[1])     
                self.P.grid(column=1, row=n)
            elif 40<= n <=80:
                self.L = Tkinter.Label(master = self.frame, text = coinpair[0])     
                self.L.grid(column=3, row=n-40)

                self.space = Tkinter.Label(master = self.frame, text="                ")
                self.space.grid(column=2, row=n-40)

                self.P = Tkinter.Label(master = self.frame, text = "%.8f" % coinpair[1])     
                self.P.grid(column=4, row=n-40)
            elif 80 <= n <= 120:
                self.L = Tkinter.Label(master = self.frame, text = coinpair[0])     
                self.L.grid(column=6, row=n-80)
                
                self.space = Tkinter.Label(master = self.frame, text="                ")
                self.space.grid(column=5, row=n-80)

                self.P = Tkinter.Label(master = self.frame, text = "%.8f" % coinpair[1])     
                self.P.grid(column=7, row=n-80)
            elif 120 <= n <= 160:
                self.L = Tkinter.Label(master = self.frame, text = coinpair[0])     
                self.L.grid(column=9, row=n-120)
                
                self.space = Tkinter.Label(master = self.frame, text="                ")
                self.space.grid(column=8, row=n-120)

                self.P = Tkinter.Label(master = self.frame, text = "%.8f" % coinpair[1])     
                self.P.grid(column=10, row=n-120)
                
            elif 160 <= n <= 200:
                self.L = Tkinter.Label(master = self.frame, text = coinpair[0])     
                self.L.grid(column=12, row=n-160)
                
                self.space = Tkinter.Label(master = self.frame, text="                ")
                self.space.grid(column=11, row=n-160)

                self.P = Tkinter.Label(master = self.frame, text = "%.8f" % coinpair[1])     
                self.P.grid(column=13, row=n-160)
            elif 200 <= n <= 240:
                self.L = Tkinter.Label(master = self.frame, text = coinpair[0])     
                self.L.grid(column=15, row=n-200)
                
                self.space = Tkinter.Label(master = self.frame, text="                ")
                self.space.grid(column=14, row=n-200)

                self.P = Tkinter.Label(master = self.frame, text = "%.8f" % coinpair[1])     
                self.P.grid(column=16, row=n-200)
            
            n+=1

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('CryptsyRates v1.0')
    app.mainloop()

