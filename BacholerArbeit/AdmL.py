import itertools
from itertools import combinations, chain
from tkinter import *
import matplotlib
import os
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import tkinter as Tk
import networkx as nx
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import filedialog



#also a -> b und b -> a. Des Weiteren b -> c, c -> d, d -> e, e ->c.
#Durch diese Funktion wird die Attacken zwischen die Knoten gelesen
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

#Hilfsfunktion, um die leere Zeichen zu lesen
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
nnode =node


#Hilfsfunktion, um eine Liste in String zu Konvertieren
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
    print(c)

p = []
for l in G.edges :
    p.append(l)


t3=p
out = [item for t in p for item in t]
Y=[]
for c in node:
    Y.append(listToString(c))
print(Y)
X= list(set(out+Y))
print('9-----------',X)
edges = (p)


Attack_list = []
Protect_list = []


#Hilfsfunktion, um alle Attacke für eine node zu bringen und in eine List zu speichern
def Attack(matrix,x,n):


    if x == matrix[n][0]:
      y= matrix[n][1]
      #print(x,"attakiert",y)
      Attack_list.append(y)
    if n < len(matrix)-1:
      n=n+1
      Attack(matrix,x,n)



#Hilfsfunktion, um alle Angreife für eine node zu bringen und in eine List zu speichern
def protect(matrix,x,n):
    if x == matrix[n][1]:
        y= matrix[n][0]

        #print(x,"protect",y)
        Protect_list.append(y)
    if n < len(matrix)-1:
        n=n+1
        protect(matrix,x,n)


m = 0
staerke_List = []
#Funktion, hier wird alle knoten zurückgegeben, wo jedes Knoten Admissible Menge ist
def starke_List ():
    for m in X:
      protect(t3,m,0)
      Attack(t3,m,0)
      if Attack_list==Protect_list :
          staerke_List.append(m)
      elif (Attack_list != Protect_list and all(elem in Attack_list  for elem in Protect_list)):

          staerke_List.append(m)

      Attack_list.clear()
      Protect_list.clear()
    return staerke_List


x2 =starke_List()
print("StaerkeListe: ",x2)



# hier wird alle knoten zurückgegeben,die vielleicht in die Admissible Menge sein können
def schwaeche_Liste():
  L = list(set(X) - set(x2))
  for x in L :
      for y in t3 :
          if y[0]==x and y[1]==x:
              L.remove(x)
  return L

x3= schwaeche_Liste()
print("schwaecheListe: ",x3)

#Hilfsfunktion, die die Potenzmengen für eine Menge zurückgibt
def powerset(iterable):

    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = iterable

    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


#Hilfsfunktion, die die subsets findet
def findsubsets(s, n):
    a = list(itertools.combinations(s, n))
    for m in a :
        if m in t3 :
            return False




#Hilfsfunktion, die die Mengen löschen die nicht Admissible Mengen sind
def menge_Löschen(c):
    f=[]
    for m in c :
        if len(m) >= 2:
            print('9---',m)
            f = list(powerset(m))
    for n in f :
        if n in t3 and m in c:
            print('10---',m)
            c.remove(m)
    for m in c :
        if m in t3:
            print('11---',m)
            c.remove(m)

Attack_list1 = []
Protect_list1 = []

#Hilfsfunktion, um alle Attacke für eine node zu bringen und in eine List zu speichern
def Attack1(matrix,x,n):


    if x == matrix[n][0]:
        y= matrix[n][1]
        #print(x,"attakiert",y)
        Attack_list1.append(y)
    if n < len(matrix)-1:
        n=n+1
        Attack1(matrix,x,n)

Attack_list2 = []
#Hilfsfunktion, um alle Attacke für eine node zu bringen und in eine List zu speichern
def Attack2(matrix,x,n):


    if x == matrix[n][0]:
        y= matrix[n][1]
        #print(x,"attakiert",y)
        Attack_list2.append(y)
    if n < len(matrix)-1:
        n=n+1
        Attack2(matrix,x,n)
#Hilfsfunktion, um alle Angreife für eine node zu bringen und in eine List zu speichern
def protect1(matrix,x,n):
    if x == matrix[n][1]:
        y= matrix[n][0]

        #print(x,"protect",y)
        Protect_list1.append(y)
    if n < len(matrix)-1:
        n=n+1
        protect1(matrix,x,n)

#Hilfsfunktion, um alle Attacke für eine node zu bringen und in eine List zu speichern
def attacken (liste):

    for l in liste :
        Attack1(t3,l,0)

    x= list(Attack_list1)

    Attack_list1.clear()
    return x
list2 =[]

# Hier wird knoten bestimmt, die ein knote geschwächt haben
def geschwaechteElm (list1):


    for elm in list1 :
       Attack2(t3,elm,0)
       protect1(t3,elm,0)
       list_difference = list([item for item in Protect_list1 if item not in Attack_list2])
       Attack_list2.clear()
       Protect_list1.clear()
       list2.append(list_difference)
       Protect_list1.clear()


    return list2


#Anfrage, um zu wissen, ob ein list leer ist
def Enquiry(lis1):
    if not lis1:
        return 1
    else:
        return 0



#hier wird die admissible Menge bestimmt
def admisible_Mengen():
   c = list(powerset(x2))
   a= []

   print('12-----',c)
   menge_Löschen(c)
   print('1-------',c)
   n = []
   geprüftelist= geschwaechteElm(x3)
   print('geprüftelist',geprüftelist)
   for i in c :

       for counter, j in enumerate(geprüftelist):

           h = attacken(i)
           print(h)
           if Enquiry(h)== 0 and set(j).issubset(set(h)):

            n.append(tuple(list(i)+list(x3[counter])))
            print('1------',list(i),list(x3[counter]))
   m = c+n
   return m


x4 = admisible_Mengen()
print('3---------',x4)
global adm
adm = len(x4)
#t3=[('A','B'),('B','A'),('B','C'),('C','D'),('D','E'),('E','C'),('C','E')]
Attack_liste3 = []
#Hilfsfunktion, um alle Attacke für eine node zu bringen und in eine List zu speichern
def Attack3(m):
    for x in t3 :
        if m == x[0] and x[0]!=x[1]:
            Attack_liste3.append(x[1])

    return Attack_liste3


#Hier wird Dictionary zurückgegeben
def my_function(x):
    return list(dict.fromkeys(x))
global long
long = 0

#in dieser Funktion wird mithilfe der Funktion von admisible_Mengen  die AdmissibleLablling Mengen bestimmt
# und danach wird die Mengen durch Graphen dargestellt
def AdmissibleLablling():
    OUT = []
    In = []
    Out = []
    u=[]
    long = 0
    i = 521
    for y in x4 :
        if not y:
            UNDEC1= X
        elif len(y)!=0:
            for x in y:
                IN = y
                z = list(Attack3(x))
                Attack_liste3.clear()
                OUT += z
                In = list(IN)
                Out = list(OUT)
                u =In + Out
        UNDEC1 = [item for item in X if item not in u]
        print('1-',In)
        print('2-',Out)
        print('3-',UNDEC1)
        G = nx.DiGraph()
        G.add_edges_from(
            p)
        for c in nnode :
         G.add_node(listToString(c))
        for l  in In :
         if list(l) in nnode:
            print ('8-----',list(l))
            m = listToString(l)
            In.remove(m)
            UNDEC1.append(m)
        print('1-',In)
        print('2-',Out)
        print('3-',UNDEC1)
        color_map = []
        for node in G:
          if node in In:
           color_map.append('blue')
          if node in Out:
           color_map.append('green')
          if node in UNDEC1:
            color_map.append('red')
        pos = pos = nx.spring_layout(G, k=0.15, iterations=2,seed=50)
        i = i+1
        plt.subplot(i)
        print('7----------',color_map)
        plt.title("▼ Admissible Labelling ▼")
        if long == adm-1 :
            plt.title("▼ die maximale Admissible Labelling ,die auch Preferred Labelling ist ▼")
        nx.draw(G,pos, node_color=color_map, with_labels=True)
        long=long+1
        print('1-------------------------',long)
        UNDEC1.clear()
        OUT.clear()
    return plt.show()



##############################################################################################################################################################################################################################

root = Tk.Tk()
root.wm_title("Animated Graph embedded in TK")
# Quit when the window is done
root.wm_protocol('WM_DELETE_WINDOW', root.quit)
root.title('Admissible Labeling')
root.geometry("400x800")
f = plt.figure(figsize=(1,1),dpi=100)
a = f.add_subplot(111)
plt.axis('off')
canvas = FigureCanvasTkAgg(f, master=root)
G1=nx.DiGraph()
G1.add_edges_from(tuple1)
for c in node :
    G1.add_node(listToString(c))


#Funktion um ein File zu Speichern
def file_save():
    text_file = filedialog.askopenfilename(initialdir ="C:/Users/tarek/Desktop/",title = "add_node",filetypes = (("Text Files","*.txt"),) )
    text_file = open(text_file,'w')
    text_file.write(my_text3.get(1.0,END))

#Funktion um ein File zu öffnen
def open_file():
    text_file = open("C:/Users/tarek/Desktop/Data.txt",'r')
    stuff = text_file.read()
    my_text3.insert(END,stuff)
    text_file.close()


#Funktion um einen Graph zu löschen
def Deletet_graph():

    canvas.get_tk_widget().destroy()
    root.quit()
    root.destroy()


#durch dieser Funktion wird das Programm beendet
def _quit():
    root.quit()
    root.destroy()
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
global Wait
Wait = 0
#Funktion, um zu verbieten, dass Mann die AdmissibleLablling Mengen darstellen, before Mann der Graph zeichnen
def onClick():
    if Wait == 0 :
      Tk.messagebox.showinfo("Please Zeichnen sie das Graph before sie Das Admissible Mengen zur Bestimmen ")
    elif  Wait == 1:
      AdmissibleLablling()
#def on_key_press(event):
    #print("you pressed {}".format(event.key))
    #key_press_handler(event, canvas, toolbar)
    #canvas.mpl_connect("key_press_event", on_key_press)

#Funktion ,um das Programm noch mal auszuführen
def helloCallBack():
    root.quit()     # stops mainloop
    root.destroy()
    os.system('AdmL.py')

#Funktion ,um der Graph zu zeichnen
def draw ():
    global Wait
    Wait = Wait + 1
    if Wait <= 1:
     print(Wait)
     pos= pos =nx.spring_layout(G, k=0.15, iterations=2,seed=50)
     nx.draw_networkx(G1,pos=pos,ax=a)
     canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
     return canvas.draw()
    elif Wait > 1 :
        Tk.messagebox.showinfo("schon gezeichnet ")

B=Button(master=root,text="Führen Sie das Programm erneut aus",command= helloCallBack)
B.pack(side = TOP, pady = 10)
button1 = Button(master=root, text="Quit", command=_quit)
button1.pack(side=BOTTOM)
button2 = Button(master=root, text="Zeichnen",  command=lambda: draw())
button2.pack(side=BOTTOM)
button7 = Tk.Button(master =root, text="Zeige_die_Knoten", command=open_file)  # <------
button7.pack(side = TOP, pady = 10)
button5 = Button(master = root, text="Save", command=file_save)  # <------
button5.pack(side=BOTTOM)
button6 = Button(master =root, text="Delete", command=Deletet_graph)  # <------
button6.pack(side=BOTTOM)
button9 = Button(master=root, text="AdmisibleLabelling", command=lambda:onClick())
button9.pack(side=BOTTOM)
my_text3 = Text(master =root,width = 40,height = 10,font = ("Helvetica",16))
my_text3.pack(pady=20)


#root.mainloop()


Tk.mainloop()