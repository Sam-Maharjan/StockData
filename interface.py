import tkinter as tk
from tkinter import ttk
from data import findBasic, findPrecise

name=''
def generate():
    temp=14
    try:
        
        name=inp.get()
        basic=findBasic(name)
        precise=findPrecise(name)
        B=tk.Label(gui, text=basic,font=('calibre',15, 'bold') )
        B.grid(row=13,column=0)
        for val in precise:
            P=tk.Label(gui, text=val+' = '+ precise.get(val),font=('calibre',15, 'bold') )
            P.grid(row=temp,column=0)
            temp+=1
    except:
        E=tk.Label(gui, text='ValueError',font=('calibre',15, 'bold') )
        empty=tk.Label(gui, text='',font=('calibre',15, 'bold') )
        E.grid(row=7,column=0)
        if(temp>14):
            for i in (14,temp):
                empty.grid(row=i,column=0)

    




gui = tk.Tk()
gui.geometry("750x550")
gui.title("Stock Data Scraper")
label = tk.Label(gui, text="Enter a Stock Symbol: ",font=('calibre',15, 'bold') )
inp = tk.Entry(gui,textvariable = "", font=('calibre',15,'normal'))
label.grid(row=0,column=0)
inp.grid(row=0,column=1)
gen=tk.Button(gui, text= "Generate Data",width= 20, command=generate)
gen.place(x=169,y=50)



gui.mainloop()