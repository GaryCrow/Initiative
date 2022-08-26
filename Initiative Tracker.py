from tkinter import *
import tkinter.ttk as ttk
import glob
import os
root = Tk()
root.title("Encounter Tracker")
root.option_add('*Font','30')
root.geometry("600x600")
root.minsize(400, 490)
root.maxsize(780,800)
global FONT
FONT = "Georgia"
global order
global name
global HPMAX
global HP
global team
global initiative
global AC
global tracker
global storage

tracker = []
storage = []
order = []
name = []
HPMAX = []
HP = []
team = []
initiative = []
AC =[]
'''
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(2, weight=1)
'''
for i in range(20):
    root.grid_rowconfigure(i, weight=1)
root.grid_rowconfigure(0, weight=5)
root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(1, weight=2)
root.grid_columnconfigure(2, weight=1)
#Start making background
root.wm_attributes('-transparentcolor','purple')
importList = StringVar(value=order)
bg = PhotoImage(file="Big city.png")
background = Label(root, image  = bg)
background.place(x=0,y=0)
#my_canvas=Canvas(root)
#my_canvas.pack(fill="both",expand=True)

#my_canvas.create_image(0,0, image=bg,anchor=NW)
TBWIDTH = 34
TBSIZE = 12
#End Background

lst = Listbox(root, selectmode=MULTIPLE, font =(FONT, TBSIZE),width=20)
root.wm_attributes('-transparentcolor','purple')
lst.insert(END, *order)
lst.grid(column=0,row=0,sticky ="ns",padx=0,pady=5,rowspan=17,columnspan=1)
#Check for the Saves folder
if(os.path.exists('Saves')):
    os.chdir('Saves')
else:
    os.mkdir('Saves')
#Button to add people
listHP = Listbox(root, font =(FONT, TBSIZE),width=30)
root.wm_attributes('-transparentcolor','purple')
listHP.grid(column=1,row=0,sticky ="ns",padx=5,pady=5,rowspan=17)
#Damage/Heal Buttons
def Heal():
    if(len(HPMOD.get()) !=0 and listHP.curselection()):
        selection = listHP.curselection()
       #print(selection)
        sel = listHP.get(selection[0]).split('|')[1].lstrip().split('[')[0]
       #print(sel)
        
        
    
        for i in range(len(name)):
            if(sel == name[i]):
                #print(i)
                HP[i]= str(int(HP[i]) + int(HPMOD.get()))
                #print(HP[i])
                tracker.clear()
                for i in range(len(name)):
                    tracker.append(team[i]+'|'+name[i]+'['+HP[i]+'/'+HPMAX[i]+']('+AC[i]+')')
                #print(tracker)
                storage[i*5+3] = HP[i]
                tracker.sort()
                listHP.delete(0,END)
                listHP.insert(END,*tracker)
        
HEALBTNX =625
HealFrame = Frame(root)
HealFrame.grid(column=2,row=0,sticky ="nw",padx=5,pady=2)
btnHeal = Button(HealFrame, text = "Heal", fg = "green", command = Heal, font=(FONT))
btnHeal.pack(fill='x')

def Damage():
    if(len(HPMOD.get()) !=0 and listHP.curselection()):
        selection = listHP.curselection()
       #print("You selected:"+str(selection))
        sel = listHP.get(selection[0]).split('|')[1].lstrip().split('[')[0]
        #print("Name is:"+sel)
        
        
    
        for i in range(len(name)):
            if(sel == name[i]):
                
                HP[i]= str(int(HP[i]) - int(HPMOD.get()))
                
                tracker.clear()
                for i in range(len(name)):
                    
                    tracker.append(team[i]+'|'+name[i]+'['+HP[i]+'/'+HPMAX[i]+']('+AC[i]+')')
                #print(tracker)
                storage[i*5+3] = HP[i]
                tracker.sort()
                listHP.delete(0,END)
                listHP.insert(END,*tracker)

HPMOD = Entry(HealFrame,width=5)
HPMOD.pack(fill='x')


btnDMG = Button(HealFrame, text = "Damage", fg = "Red", command = Damage, font=(FONT))
btnDMG.pack()


#Enter key for easy entering

def Enter(event):
    clicked()
root.bind('<Return>', Enter)

def clicked():
    if(len(rollTxt.get()) != 0 and len(nameTxt.get()) != 0
       and len(rollTxt.get()) <4 and str.isdigit(rollTxt.get())
       and len(TeamTXT.get())!=0):
        '''
        order.clear()
        tracker.clear()
        storage.clear()
        '''
        if(len(rollTxt.get()) <2):
            name.append(nameTxt.get())
            initiative.append('0'+rollTxt.get())
            HP.append(HPTXT.get())
            HPMAX.append(HPTXT.get())
            team.append(TeamTXT.get())
            if len(ACTXT.get()) !=0:
                AC.append(ACTXT.get())
            else:
                AC.append(' ')
            i = len(name)-1
            order.append(initiative[i]+'-'+name[i])
            tracker.append(team[i]+'|'+name[i]+'['+HP[i]+'/'+HPMAX[i]+']('+AC[i]+')')
            storage.append(name[i])
            storage.append(initiative[i])
            storage.append(HP[i])
            storage.append(HPMAX[i])
            storage.append(team[i])
            storage.append(AC[i])
        elif len(rollTxt.get()) == 3:
            name.append(nameTxt.get())
            initiative.append(str(int(rollTxt.get())/10))
            HP.append(HPTXT.get())
            HPMAX.append(HPTXT.get())
            team.append(TeamTXT.get())
            if len(ACTXT.get()) !=0:
                AC.append(ACTXT.get())
            else:
                AC.append(' ')
            
            i = len(name)-1
            order.append(initiative[i]+'-'+name[i])
            tracker.append(team[i]+'|'+name[i]+'['+HP[i]+'/'+HPMAX[i]+']('+AC[i]+')')
            storage.append(name[i])
            storage.append(initiative[i])
            storage.append(HP[i])
            storage.append(HPMAX[i])
            storage.append(team[i])
            storage.append(AC[i])
        else:
            name.append(nameTxt.get())
            initiative.append(rollTxt.get())
            HP.append(HPTXT.get())
            HPMAX.append(HPTXT.get())
            team.append(TeamTXT.get())
            if len(ACTXT.get()) !=0:
                AC.append(ACTXT.get())
            else:
                AC.append(' ')
            
            i = len(name)-1
            order.append(initiative[i]+'-'+name[i])
            tracker.append(team[i]+'|'+name[i]+'['+HP[i]+'/'+HPMAX[i]+']('+AC[i]+')')
            storage.append(name[i])
            storage.append(initiative[i])
            storage.append(HP[i])
            storage.append(HPMAX[i])
            storage.append(team[i])
            storage.append(AC[i])
        rollTxt.delete(0,END)
        nameTxt.delete(0,END)
        HPTXT.delete(0,END)
        ACTXT.delete(0,END)
        order.sort(reverse = True)
        tracker.sort()
        listHP.delete(0,END)
        listHP.insert(END,*tracker)
        lst.delete(0,END)
        lst.insert(END,*order)
        nameTxt.focus_set()
       # #print(order)
def rotate():
    order.sort(key = order[0].__eq__)
    ##print(order)
    lst.delete(0,END)
    lst.insert(END,*order)
# Delete Button & Function
def delete():
    selection = lst.curselection()
    for i in selection[::-1]:
        lst.delete(i)
        del order[i]
def HPdelete():
    selection = listHP.curselection()
    for i in selection[::-1]:
        listHP.delete(i)
        del order[i]
              

btnDelete = Button(root, text = "Delete Selection", command = delete, font=(FONT))
btnDelete.grid(column=0,row=17,sticky ="nw",padx=5,pady=2)
btnHPDelete = Button(root, text = "Delete Selection", command = HPdelete, font=(FONT))
btnHPDelete.grid(column=1,row=17,sticky ="nw",padx=5,pady=2)
#Textboxes for name and roll
InfoFrame = Frame(root)
InfoFrame.grid(column=2,row=15,sticky ="se",padx=5,pady=2,rowspan=5)

nameVar = StringVar()
namelabel = Label(InfoFrame, textvariable=nameVar, font=(FONT))
nameVar.set("Character Name")
namelabel.pack()
nameTxt = Entry(InfoFrame, width=20, font=("Georgia"))
nameTxt.pack()

#Handle Roll input

rollVar = StringVar()
rolllabel = Label(InfoFrame, textvariable=rollVar, font=(FONT))
rollVar.set("Initiative")
rolllabel.pack()

#my_canvas.create_text(400,250, text = "Initiative", font=("Georgia"), anchor=SE)

rollTxt = Entry(InfoFrame,width=10)
rollTxt.pack()
#Health
HPVar = StringVar()
HPlabel = Label(InfoFrame, textvariable=HPVar, font=(FONT))
HPVar.set("Max Health")
HPlabel.pack()
HPTXT = Entry(InfoFrame,width=10)
HPTXT.pack()

#Allegiance
TeamVar = StringVar()
Teamlabel = Label(InfoFrame, textvariable=TeamVar, font=(FONT))
TeamVar.set("Allegiance")
Teamlabel.pack()
TeamTXT = Entry(InfoFrame,width=10)
TeamTXT.pack()

#AC
ACVar = StringVar()
AClabel = Label(InfoFrame, textvariable=ACVar, font=(FONT))
ACVar.set("Optional: AC")
AClabel.pack()
ACTXT = Entry(InfoFrame,width=10)
ACTXT.pack()




#Begin Save Area
saveFrame = Frame(root)
saveFrame.grid(column=0,row=18,sticky ="nw",padx=5,pady=2)
savetxt = Entry(saveFrame, font=("Georgia"))
savetxt.pack(fill='y')
'''
saveVar = StringVar()
savelabel = Label(root, textvariable=saveVar, font=(FONT))
saveVar.set("Save As")
savelabel.grid(column=0,row=9,sticky ="nw",padx=5,pady=2)
'''
def save():
    if(len(savetxt.get()) !=0):
        if(os.path.exists(savetxt.get()+'.txt')):
            #print("File Found")
            with open(savetxt.get()+'.txt', 'r+') as output:
                output.truncate(0)
            
                for listitem in storage:
                    output.write('%s\n' % listitem)
                output.close()
        else:
            with open(savetxt.get()+'.txt', 'w') as output:
                output.truncate(0)
            
                for listitem in storage:
                    output.write('%s\n' % listitem)
                output.close()
    #print("save here")
    
        my_files = glob.glob('*.txt')
        my_files = [os.path.splitext(x)[0] for x in my_files]
        loadtxt.delete(0,END)
        loadtxt.insert(0,*my_files)

btnSave = Button(saveFrame, text = "Save Scenario", fg = "green", command = save, font=(FONT))
btnSave.pack(fill='x')

#Begin Load Area

#get the save files
my_files = glob.glob('*.txt')

#print(my_files)
my_files = [os.path.splitext(x)[0] for x in my_files]
loadtxt = Listbox(root, width = 25, height =5, font=(FONT))

loadtxt.place(rely=1.0, x=5,y=-5, anchor =SW)
loadtxt.insert(0,*my_files)



def load():
    selection = loadtxt.curselection()
    order.clear()
    tracker.clear()
    name.clear()
    initiative.clear()
    HP.clear()
    HPMAX.clear()
    team.clear()
    storage.clear()
    for i in selection[::-1]:
        #print(loadtxt.get(i))
        input = open(loadtxt.get(i)+".txt", "r")
        temp = input.read().splitlines()
       
        #print(len(temp))
        for i in range(0,len(temp),6):
           #print(i)
            name.append(temp[i])
            #print(temp[i])
            initiative.append(temp[i+1])
            HP.append(temp[i+2])
            HPMAX.append(temp[i+3])
            team.append(temp[i+4])
            AC.append(temp[i+5])
        #print(team)  
        for i in range(len(name)):
            storage.append(name[i])
            storage.append(initiative[i])
            storage.append(HP[i])
            storage.append(HPMAX[i])
            storage.append(team[i])
            storage.append(AC[i])
            order.append(initiative[i]+'-'+name[i])
            tracker.append(team[i]+'|'+name[i]+'['+HP[i]+'/'+HPMAX[i]+']('+AC[i]+')')
        order.sort(reverse = True)
        trackertemp = tracker
        trackertemp.sort()
                
        lst.delete(0,END)
        lst.insert(END,*order)
        listHP.delete(0,END)
        listHP.insert(END,*trackertemp)
print(order)
btnLoad = Button(InfoFrame, text = "Load", fg = "green", command = load, font=(FONT))
btnLoad.pack()

btn = Button(InfoFrame, text = "Insert" ,
             fg = "red", command=clicked, font=("Georgia"))
btn.pack()

btnRo = Button(InfoFrame, text = "Next Turn", fg = "blue", command = rotate, font=(FONT))
btnRo.pack()
# Set Button Grid
#print(order)

root.mainloop()
