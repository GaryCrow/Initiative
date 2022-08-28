from tkinter import *
import tkinter.ttk as ttk
import glob
import os
root = Tk()
root.title("Encounter Tracker")
root.option_add('*Font','30')
root.geometry("650x600")
root.minsize(400, 490)
root.maxsize(780,650)
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
lst.grid(column=0,row=0,sticky ="ns",padx=5,pady=5,rowspan=17,columnspan=1)
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
       #print("You selected:"+str(selection))
        sel = listHP.get(selection[0]).split('|')[1].lstrip().split('[')[0]
        #print("Name is:"+sel)
        
        
    
        for i in range(0,len(storage),6):
            if(sel == storage[i]):
                
                storage[i+2]= str(int(storage[i+2]) + int(HPMOD.get()))
                
                tracker.clear()
                for i in range(0,len(storage),6):
                    
                    tracker.append(storage[i+4]+'|'+storage[i]+'['+storage[i+2]+'/'+storage[i+3]+']('+storage[i+5]+')')
                #print(tracker)
                
                tracker.sort()
                listHP.delete(0,END)
                listHP.insert(END,*tracker)
    save()        
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
        
        
    
        for i in range(0,len(storage),6):
            if(sel == storage[i]):
                
                storage[i+2]= str(int(storage[i+2]) - int(HPMOD.get()))
                
                tracker.clear()
                for i in range(0,len(storage),6):
                    
                    tracker.append(storage[i+4]+'|'+storage[i]+'['+storage[i+2]+'/'+storage[i+3]+']('+storage[i+5]+')')
                #print(tracker)
                
                tracker.sort()
                listHP.delete(0,END)
                listHP.insert(END,*tracker)
    save()
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
        
        
        i = (len(storage)/6)
        i=int(i*6)
        storage.append(nameTxt.get())
        #storage.append(initiative[i])
        if(len(rollTxt.get()) <2):
            storage.append('0'+rollTxt.get())
        elif len(rollTxt.get()) == 3:
            storage.append(str(int(rollTxt.get())/10))  
        else:
            storage.append(rollTxt.get())

        storage.append(HPTXT.get())
        storage.append(HPTXT.get())
        storage.append(TeamTXT.get())
        if len(ACTXT.get()) !=0:
            storage.append(ACTXT.get())  
        else:
            storage.append(' ')
        order.append(storage[i+1]+'-'+storage[i])
        tracker.append(storage[i+4]+'|'+storage[i]+'['+storage[i+2]+'/'+storage[i+3]+']('+storage[i+5]+')')
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
    save()
def rotate():
    order.sort(key = order[0].__eq__)
    ##print(order)
    lst.delete(0,END)
    lst.insert(END,*order)
# Delete Button & Function
def delete():
    if lst.curselection():
        selection = lst.curselection()
        for i in selection[::-1]:
            TempName = lst.get(i).split("-",1)[1]
            lst.delete(i)
            del order[i]
            for i, listbox_entry in enumerate(listHP.get(0, END)):
                if TempName in listbox_entry:
                    listHP.delete(i)
                    del tracker[i]
            print(storage)
            for i in range (len(storage)-6):
            
                if TempName == storage[i]:
                    for j in range(6):
                        print(storage[int(i)],i,j,i+j)
                        del storage[int(i)]
            print(storage)        
    elif listHP.curselection():
        selection = listHP.curselection()
        for i in selection[::-1]:
            TempName = listHP.get(selection[0]).split('|')[1].lstrip().split('[')[0]
            listHP.delete(i)
            del tracker[i]
            for i, listbox_entry in enumerate(lst.get(0, END)):
                if TempName in listbox_entry:
                    lst.delete(i)
                    del order[i]
            print(storage)
            for i in range (len(storage)-6):
            
                if TempName == storage[i]:
                    for j in range(6):
                        print(storage[int(i)],i,j,i+j)
                        del storage[int(i)]
            print(storage)      
'''   
def HPdelete():
    selection = listHP.curselection()
    for i in selection[::-1]:
        listHP.delete(i)
        del order[i]
 '''             

btnDelete = Button(root, text = "Delete Selection", command = delete, font=(FONT))
btnDelete.grid(column=0,row=17,sticky ="nw",padx=5,pady=2)
#btnHPDelete = Button(root, text = "Delete Selection", command = HPdelete, font=(FONT))
#btnHPDelete.grid(column=1,row=17,sticky ="nw",padx=5,pady=2)
#Textboxes for name and roll
InfoFrame = Frame(root)
InfoFrame.grid(column=2,row=13,sticky ="se",padx=5,pady=2,rowspan=7)

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
saveFrame.grid(column=2,row=10,sticky ="nw",padx=5,pady=2)
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
    for j in selection[::-1]:
        #print(loadtxt.get(i))
        loader=loadtxt.get(j)
        input = open(loadtxt.get(j)+".txt", "r")
        temp = input.read().splitlines()
       
        #print(len(temp))
        for i in range(0,len(temp),6):
           #print(i)
            storage.append(temp[i])
            #print(temp[i])
            storage.append(temp[i+1])
            storage.append(temp[i+2])
            storage.append(temp[i+3])
            storage.append(temp[i+4])
            storage.append(temp[i+5])  
            for j in range(6):
                print(storage[j])
            order.append(storage[i+1]+'-'+storage[i])
            tracker.append(storage[i+4]+'|'+storage[i]+'['+storage[i+2]+'/'+storage[i+3]+']('+storage[i+5]+')')
        order.sort(reverse = True)
        trackertemp = tracker
        trackertemp.sort()
                
        lst.delete(0,END)
        lst.insert(END,*order)
        listHP.delete(0,END)
        listHP.insert(END,*trackertemp)
        savetxt.delete(0,END)
        savetxt.insert(END,loader)
print(order)
btnLoad = Button(InfoFrame, text = "Load", fg = "green", command = load, font=(FONT))
btnLoad.pack(side=LEFT)

btn = Button(InfoFrame, text = "Insert" ,
             fg = "red", command=clicked, font=("Georgia"))
btn.pack()

btnRo = Button(InfoFrame, text = "Next Turn", fg = "blue", command = rotate, font=(FONT))
btnRo.pack()
# Set Button Grid
#print(order)

root.mainloop()
