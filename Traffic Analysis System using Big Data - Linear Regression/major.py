from Tkinter import *

import numpy as np
import matplotlib.pyplot as plt
import os
import os.path
import copy
from PIL import ImageTk, Image
import Image #PIL  
import ImageTk #PIL
root = Tk()
root.title("Traffic Analysis System")

text1 = Text(root, height=19, width=58)
photo=PhotoImage(file='./pic.gif')
text1.insert(END,'\n')
text1.image_create(END, image=photo)

text1.pack(side=TOP)

text2 = Text(root, height=5, width=58)
text2.tag_configure('bold_italics', font=('Arial', 20, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color', foreground='#476042', 
                        font=('times new roman', 10, 'bold'))
text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "N!"))
text2.insert(END,'\n    Traffic Analysis System \n', 'big')
text2.insert(END, '\n', 'follow')
text2.pack(side=LEFT)


root.mainloop()


class Application(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
	
	self.var = StringVar()
        self.var.set("Enter the Location")
        OptionMenu(self, self.var, "South Lanarkshire-Dillarburn Road","Derby-Nairn Avenue","Cambridgeshire-Fox Street","new").grid(row=0,column=0,sticky=W)
	
	self.sar = StringVar()
        self.sar.set("Enter the time")
        OptionMenu(self, self.sar,"7","8","9", "10","11","12","13","14","15","16","17","18").grid(row=0,column=1,sticky=W)

        self.a=BooleanVar()
        Checkbutton(self,text="Current traffic details",variable=self.a,command=self.update_text).grid(row=7,column=0,sticky=W)

        self.b=BooleanVar()
        Checkbutton(self,text="Vehicle frequency graph",variable=self.b,command=self.update_texts).grid(row=8,column=0,sticky=W)

        self.c=BooleanVar()
        Checkbutton(self,text="Recommended Vehicle ",variable=self.c,command=self.update_texts1).grid(row=9,column=0,sticky=W)

	button = Button(self, text="Submit", command=self.ok)
        button.grid(row=2,column=0,sticky=W)

        self.text = Text(self, width=38, height=3,wrap=WORD)
        self.text.grid(row=6, column=0, columnspan=2, sticky=W) 
                
    def ok(self):
        location = self.var.get()
	time=self.sar.get()
	str1=location+time+".txt"
        filePath=copy.copy(str1)
        if(os.path.isfile(filePath)):
            message="Location found"
            
        else:
            message= "Sorry Location not in database"
        self.text.delete(0.0,END)
        self.text.insert(0.0,message)
        
    def update_text(self):
        location = self.var.get()
	time=self.sar.get()
	str1=location+time+".txt"
        filePath=copy.copy(str1)
	
        a=range(5)
        i=0
        file = open(filePath, 'rU')
        for line in file:
            for word in line.split():
                a[i]=float(word)
                i=i+1
	j=int(a[0])
	k=int(a[1])
	l=int(a[2])
	h=int(a[3])
	z=str(j)
	x=str(k)
	n=str(l)
	m=str(h)
        Print="No of car="+z+"\n"+"No of Truck="+x+"\n"+"No of Bus="+n+"\n"+"No of Bike="+m
        smal=copy.copy(Print)
        class Apps(Frame):

            def __init__(seel,master):
                Frame.__init__(seel,master)
                seel.grid()
                seel.create_widgets()

            def create_widgets(seel):

                seel.text = Text(seel, width=40, height=9,wrap=WORD)
                seel.text.grid(row=5, column=0, columnspan=2, sticky=W)
                        
                message3=copy.copy(smal)
                seel.text.delete(0.0,END)
                seel.text.insert(0.0,message3)
                
        root=Tk()
        root.title("Current taffic details")
        root.geometry("450x250")
        app=Apps(root)
        root.mainloop()

    def update_texts(self):
        location = self.var.get()
	time=self.sar.get()
	str1=location+time+".txt"
        filePath=copy.copy(str1)
        a=range(5)
        i=0
        file = open(filePath, 'rU')
        for line in file:
            for word in line.split():
                a[i]=float(word)
                i=i+1    
        if self.b.get():
            N = 4
            menMeans = (a[0],a[1],a[2],a[3])
            menStd =   (2, 3, 4,5)

            ind = np.arange(N)  # the x locations for the groups
            width = 0.20       # the width of the bars

            fig, ax = plt.subplots()
            rects1 = ax.bar(ind, menMeans, width, color='BLUE', yerr=menStd)


            # add some text for labels, title and axes ticks
            ax.set_ylabel('Frequency of vehicle')
            ax.set_title('Type of vehicle')
            ax.set_xticks(ind+width)
            ax.set_xticklabels( ('CAR', 'TRUCK', 'BUS','BIKE'))



            def autolabel(rects):
                # attach some text labels
                for rect in rects:
                    height = rect.get_height()
                    ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                            ha='center', va='bottom')

            autolabel(rects1)
            plt.show()
                
    def update_texts1(self):
        location = self.var.get()
	time=self.sar.get()
	a=range(5)
	i=0
	str1=location+time+".txt"
        filePath=copy.copy(str1)
        file = open(filePath, 'rU')
        for line in file:
            for word in line.split():
                a[i]=float(word)
                i=i+1 
	if time=='7' or time=='8' or time=='9':
		small="Opt for public transport(bus)"
	if time=='10' or time=='11' or time=='12' or time=='13' or time=='14' or time=='15':
		if a[0]>a[3]:
			small="Opt for Two weeler"
		else:
			small="Opt for car"
	if time=='16' or time=='17' or time=='18':
		small="Opt for public transport(bus)"
	  
        class Apps(Frame):

            def __init__(seel,master):
                Frame.__init__(seel,master)
                seel.grid()
                seel.create_widgets()

            def create_widgets(seel):

                seel.text = Text(seel, width=45, height=9,wrap=WORD)
                seel.text.grid(row=5, column=0, columnspan=2, sticky=W)
                        
                message2=copy.copy(small)
                seel.text.delete(0.0,END)
                seel.text.insert(0.0,message2)
                
        root=Tk()
        root.title("Movie description")
        root.geometry("450x250")
        app=Apps(root)
        root.mainloop()
               
root=Tk()
root.title("Traffic Analysis System")
root.geometry("430x250")
app=Application(root)

root.mainloop()

