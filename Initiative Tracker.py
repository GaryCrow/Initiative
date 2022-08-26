from tkinter import *
import tkinter.ttk as ttk
import glob
import os
root = Tk()
root.title("Encounter Tracker")
root.option_add('*Font','50')
root.geometry("600x600")
root.minsize(690, 690)
root.maxsize(1200,800)
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
lst = Listbox(root, selectmode=MULTIPLE, font =(FONT, TBSIZE),height = 22, width = int(TBWIDTH*0.65))
root.wm_attributes('-transparentcolor','purple')
lst.insert(END, *order)
lst.place(x=10,y=10,anchor = NW)
#Check for the Saves folder
if(os.path.exists('Saves')):
    os.chdir('Saves')
else:
    os.mkdir('Saves')
#Button to add people
listHP = Listbox(root, font =(FONT, TBSIZE),height = 22, width = TBWIDTH)
root.wm_attributes('-transparentcolor','purple')
listHP.place(x=260, y=10, anchor = NW)
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
btnHeal = Button(root, text = "Heal", fg = "green", command = Heal, font=(FONT))
btnHeal.place(x=HEALBTNX,y=70, anchor=NW)

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

btnDMG = Button(root, text = "Damage", fg = "Red", command = Damage, font=(FONT))
btnDMG.place(x=HEALBTNX,y=110, anchor=NW)

HPMOD = Entry(root,width=5)
HPMOD.place(x=HEALBTNX, y=40,anchor = NW)

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
btnDelete.place(anchor =NW, x=10, y=435)
btnHPDelete = Button(root, text = "Delete Selection", command = HPdelete, font=(FONT))
btnHPDelete.place(anchor =NW, x=260, y=435)
#Textboxes for name and roll
nameVar = StringVar()
namelabel = Label(root, textvariable=nameVar, font=(FONT))
nameVar.set("Character Name")
namelabel.place(rely=1.0,x=-10, y=-230, relx=1.0,anchor = SE)
nameTxt = Entry(root, width=20, font=("Georgia"))
nameTxt.place(rely=1.0,x=-10, y=-210, relx=1.0,anchor = SE)

#Handle Roll input

rollVar = StringVar()
rolllabel = Label(root, textvariable=rollVar, font=(FONT))
rollVar.set("Initiative")
rolllabel.place(rely=1.0,x=-10, y=-186, relx=1.0,anchor = SE)

#my_canvas.create_text(400,250, text = "Initiative", font=("Georgia"), anchor=SE)

rollTxt = Entry(root,width=5)
rollTxt.place(rely=1.0,x=-10, y=-165, relx=1.0,anchor = SE)
#Health
HPTXT = Entry(root,width=5)
HPTXT.place(rely=1.0,x=-10, y=-120, relx=1.0,anchor = SE)
HPVar = StringVar()
HPlabel = Label(root, textvariable=HPVar, font=(FONT))
HPVar.set("Max Health")
HPlabel.place(rely=1.0,x=-10, y=-142, relx=1.0,anchor = SE)
#Allegiance
TeamTXT = Entry(root,width=10)
TeamTXT.place(rely=1.0,x=-10, y=-80, relx=1.0,anchor = SE)
TeamVar = StringVar()
Teamlabel = Label(root, textvariable=TeamVar, font=(FONT))
TeamVar.set("Allegiance")
Teamlabel.place(rely=1.0,x=-10, y=-100, relx=1.0,anchor = SE)
#AC
ACTXT = Entry(root,width=10)
ACTXT.place(rely=1.0,x=-120, y=-80, relx=1.0,anchor = SE)
ACVar = StringVar()
AClabel = Label(root, textvariable=ACVar, font=(FONT))
ACVar.set("Optional: AC")
AClabel.place(rely=1.0,x=-120, y=-100, relx=1.0,anchor = SE)



#Begin Save Area
savetxt = Entry(root, width = 25, font=("Georgia"))
savetxt.place(rely=1.0, x=10,y=-125, anchor =SW)

saveVar = StringVar()
savelabel = Label(root, textvariable=saveVar, font=(FONT))
saveVar.set("Save As")
savelabel.place(rely=1.0, x=10, y=-150, anchor = SW)

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

btnSave = Button(root, text = "Save", fg = "green", command = save, font=(FONT))
btnSave.place(rely=1.0, x=265,y=-120, anchor=SW)

#Begin Load Area

#get the save files
my_files = glob.glob('*.txt')

#print(my_files)
my_files = [os.path.splitext(x)[0] for x in my_files]
loadtxt = Listbox(root, width = 25, height =5, font=(FONT))

loadtxt.place(rely=1.0, x=10,y=-10, anchor =SW)
loadtxt.insert(0,*my_files)
    
scrollbar = Scrollbar(loadtxt, orient="vertical")
scrollbar.place(rely=1.0, x=255, y = -80)
scrollbar.config(command=loadtxt.yview)
#scrollbar.pack(side="right", fill="y")
loadtxt.config(yscrollcommand=scrollbar.set)

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
btnLoad = Button(root, text = "Load", fg = "green", command = load, font=(FONT))
btnLoad.place(rely=1.0, x=265,y=-10, anchor=SW)

btn = Button(root, text = "Insert" ,
             fg = "red", command=clicked, font=("Georgia"))
btn.place(rely=1.0,x=-10, y=-45, relx=1.0,anchor = SE)

btnRo = Button(root, text = "Next Turn", fg = "blue", command = rotate, font=(FONT))
btnRo.place(rely=1.0,x=-10, y=-10, relx=1.0,anchor = SE)
# Set Button Grid
#print(order)

root.mainloop()