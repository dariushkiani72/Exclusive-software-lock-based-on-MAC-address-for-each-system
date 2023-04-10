
from tkinter import *
import csv
import uuid
import pandas as pd




root = Tk()
root.state('zoomed')
root.resizable(width=True, height=True)
root.title('lock')
root['bg'] ="#353434"
frame12 = LabelFrame(root, text="", padx=1, pady=1)
frame12.pack(side="right", fill="both")
frame12['bg'] = "#818181"
frame11 = LabelFrame(root, text="", padx=1, pady=1)
frame11.pack(side="left", fill="both")
frame11['bg'] = "#818181"




e1400 = pd.read_csv("license.txt", sep=' ')
df11 = pd.DataFrame.from_dict(e1400)
df111 = df11.iloc[1, 2]


global ur,ps
ur = round((uuid.getnode() - 1119469837986)/1000000)
ps = round((ur-4646464)/13)

def licencedestroy():
    root.destroy()
    root0.destroy()
if df111 == ps:
    print("ok")
else:
    frame12.destroy()
    frame11.destroy()
    root0 = Tk()
    root0.geometry('450x400')
    root0['bg'] = "#E6E6E6"
    root0.title('license')

    # printing the value of unique MAC
    # address using uuid and getnode() function
    l01 = Label(root0, text='User Id: ', font=('arial', 14, 'bold'), fg="#FE2E2E", bg="#E6E6E6")
    l01.place(x=35, y=20)
    l02 = Label(root0, text=ur, font=('arial', 14, 'bold'), fg="#491AC4", bg="#E6E6E6")
    l02.place(x=160, y=20)
    l03 = Label(root0, text="Activation Key:", font=('arial', 12, 'bold'), fg="#491AC4", bg="#E6E6E6")
    l03.place(x=35, y=76)
    e01 = Entry(root0)
    e01.place(x=170, y=80)
    l08 = Label(root0,
                text=".*........*........*.........*........*........*.........*........*........*.........*........*........*.........*........*........*........*.",
                font=('arial', 12), fg="black", bg="#E6E6E6")
    l08.place(x=0, y=250)
    l07 = Label(root0, text="* Send us the user ID and we will send you the key.", font=('arial', 11), fg="black",
                bg="#E6E6E6")
    l07.place(x=5, y=280)
    l07 = Label(root0, text="* After activation, press the exit button and run the program again. ", font=('arial', 11),
                fg="black", bg="#E6E6E6")
    l07.place(x=5, y=300)



    def get():
        global e01
        e11 = e01.get()
        e12 = int(e11)
        if e12 == ps:
            pss = ps
            print("ok")
            l04 = Label(root0, text='Activated   ', font=('arial', 16, 'bold'), fg="#491AC4", bg="#E6E6E6")
            l04.place(x=170, y=120)
            df112 = pd.DataFrame([[9958777, 4458963], [1401, pss]],
                                 index=['0', '1', ],
                                 columns=['2', '3'])
            df112.to_csv(r'license.txt', sep=' ')

        else:
            l05 = Label(root0, text='Incorrect     ', font=('arial', 16, 'bold'), fg="#DF0101", bg="#E6E6E6")
            l05.place(x=170, y=120)


    button78 = Button(root0, text="Enter", font=('verdana', '10'), command=get, borderwidth=4, bg='#BDBDBD', fg="black")
    button78.place(x=340, y=75)
    button87 = Button(root0, text="Qiut", font=('verdana', '10'), command=licencedestroy, borderwidth=4, bg='#BDBDBD',
                      fg="black")
    button87.place(x=390, y=75)
    root0.mainloop()
root.mainloop()
