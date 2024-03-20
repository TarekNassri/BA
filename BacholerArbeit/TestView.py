from tkinter import *
import matplotlib
import self as self

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import tkinter as Tk
import networkx as nx
import numpy as np
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from AdmL import AdmissibleLablling
from tkinter import filedialog




root = Tk.Tk()
root.wm_title("Animated Graph embedded in TK")
# Quit when the window is done
root.wm_protocol('WM_DELETE_WINDOW', root.quit)
root.title('Admissible Labeling')
root.geometry("800x800")
f = plt.figure(figsize=(1,1),dpi=100)
a = f.add_subplot(111)
plt.axis('off')



def openfile():
    text_file = filedialog.askopenfilename(initialdir ="C:/Users/tarek/Desktop/",title = "add_node",filetypes = (("Text Files","*.txt"),) )
    text_file = open(text_file,'r')
    stuff = text_file.read()
    my_text3.insert(END,stuff)
    text_file.close()
def file_save():
 text_file = filedialog.askopenfilename(initialdir ="C:/Users/tarek/Desktop/",title = "add_node",filetypes = (("Text Files","*.txt"),) )
 text_file = open(text_file,'w')
 text_file.write(my_text3.get(1.0,END))

def open_file():
    text_file = open("C:/Users/tarek/Desktop/Data.txt",'r')
    stuff = text_file.read()
    my_text3.insert(END,stuff)
    text_file.close()



def Deletet_graph():

     canvas.get_tk_widget().destroy()
     root.quit()     # stops mainloop
     root.destroy()  # this is necessary on Windows to prevent
# Fatal Python Error: PyEval_RestoreThread: NULL tstate
def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
    # Fatal Python Error: PyEval_RestoreThread: NULL tstate



text=Text(root)


def clearPlotPage():
    self.canvas.destroy()
    self.canvas = None
    self.plot()
    print("Plot Page has been cleared")




# the networkx part

result = []

def addnodes ():
    with open("C:/Users/tarek/Desktop/Data.txt") as fp:
        for i in fp.readlines():
            tmp = i.rstrip('\n').split(",")
            try:
                if len(tmp)==2:
                    result.append((tmp[0],tmp[1]))
                elif len(tmp)==1:
                    result.append(tmp)
            #result.append((eval(tmp[0]), eval(tmp[1])))
            except:pass

    return result







# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
def plot():
    if self.canvas == None:
        f = Figure(figsize=(8,4), dpi=100)
        a = f.add_subplot(111)
        G=nx.DiGraph()
        G.add_edges_from(
            addnodes())

        pos=nx.circular_layout(G)
        nx.draw_networkx(G,pos=pos,ax=a)


        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.draw()
        self. canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        print("Stuff has been plotted")
tuple1=[]

node = []
def space(l):
    if all('' == s or s.isspace() for s in l):
        return True
    else:
        return False

for s in addnodes():
    if len(s)==2:
        tuple1.append(s)
    elif len(s)==1 and space(s)==False:

        node.append(s)
print(tuple1)
print(node)
def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1
G=nx.DiGraph()
G.add_edges_from(tuple1)
for c in node :
    G.add_node(listToString(c))

def draw ():

    pos=nx.circular_layout(G)
    nx.draw_networkx(G,pos=pos,ax=a)
    print(G)

    canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    return canvas.draw()
def nodes1 ():
    return G.edges


toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()




def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)

    #canvas.mpl_connect("key_press_event", on_key_press)


button1 = Button(master=root, text="Quit", command=_quit)
button1.pack(side=BOTTOM)
button2 = Button(master=root, text="Zeichnen",  command=lambda: draw())
button2.pack(side=BOTTOM)


button4 = Button(master =root, text="Open", command=openfile)  # <------
button4.pack(side=BOTTOM)
button7 = Tk.Button(master =root, text="Zeige_die_Knoten", command=open_file)  # <------
button7.pack(side = TOP, pady = 10)
button5 = Button(master = root, text="Save", command=file_save)  # <------
button5.pack(side=BOTTOM)
button6 = Button(master =root, text="Delete", command=Deletet_graph)  # <------
button6.pack(side=BOTTOM)
button8 = Button(master=root, text="AdmisibleLabelling", command=lambda:AdmissibleLablling())
button8.pack(side=BOTTOM)
my_text3 = Text(master =root,width = 40,height = 10,font = ("Helvetica",16))
my_text3.pack(pady=20)


#root.mainloop()


Tk.mainloop()