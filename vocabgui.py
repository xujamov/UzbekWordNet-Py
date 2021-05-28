from tracemalloc import Frame

import vocab
from tkinter import *
import tkFont
import ttk

BASE = RAISED
SELECTED = FLAT
ROOTBG="azure"


class Tab(Frame):
    def __init__(self, master, name):
        Frame.__init__(self, master)
        self.tab_name = name

class TabBar(Frame):
    def __init__(self, master=None, init_name=None):
        Frame.__init__(self, master,bg=ROOTBG)
        self.tabs = {}
        self.buttons = {}
        self.current_tab = None
        self.init_name = init_name
    
    def show(self):
        self.pack(side=TOP, expand=NO, fill=X)
        self.switch_tab(self.init_name or self.tabs.keys()[-1])
    
    def add(self, tab):
        tab.pack_forget()                                   
        self.tabs[tab.tab_name] = tab                       
        b = Button(self, text=tab.tab_name, relief=BASE,command=(lambda name=tab.tab_name: self.switch_tab(name)),bg="white")  
        b.pack(side=LEFT)                                               
        self.buttons[tab.tab_name] = b                                          
    
    def delete(self, tabname):
        if tabname == self.current_tab:
            self.current_tab = None
            self.tabs[tabname].pack_forget()
            del self.tabs[tabname]
            self.switch_tab(self.tabs.keys()[0])
        else:
            del self.tabs[tabname]
        self.buttons[tabname].pack_forget()
        del self.buttons[tabname] 
        
    def switch_tab(self, name):
        if self.current_tab:
          self.buttons[self.current_tab].config(relief=BASE,bg="white")
          self.tabs[self.current_tab].pack_forget()           
        self.tabs[name].pack(side=BOTTOM)                           
        self.current_tab = name                                 
        self.buttons[name].config(relief=SELECTED,bg="turquoise2")


 
class RESULT():
    def __init__(self,query):
        #result={'synonyms': u'good day,howdy,hi,hey,so long', 'meaning': u'interjection:Used to greet someone, answer the telephone, or express surprise.\n\n', 'antonyms': 'N/A', 'usage': u'Hello Sara.  How are you?Hello Danny.  I am good.\n\n"Hello, It\'s you!!"\n\n1.  \'HELLO!!!!!!\'2.  \'I satyed at home last night watching movies\'     \'... HELLO!!?!! You were supposed to come to my party last night!\'\n\n-Hot person walks into the room-Adoring member of the opposite sex: "hello"\n\n(1)Bob (sees Bill on street): "Hello, Bill!"Bill: "Well, hello, Bob."(2)(Phone rings loudly) Jim: "Hello?"James Watson from AT&T: "Hi, this is James Watson from AT&T.  I\'m calling to talk to you about your long distance plan."\n\nWhat\'s the field integral of the magnetic flux of the solenoid?Do you understand this?hEllo?\n\n<<<CRREEEEAAAAKKKK>>>> ...Hell-O.\n\nWhat the hell(mom enters)-o mom.\n\nperson 1: helloPerson 2: hiPerson 1: goodbyePerson 2: Farewell, and may the forces of evil become confused in their eternal search for you*person 1 runs away*\n\nhello im silly\n\n', 'translation': u'\u0939\u0932\u094b,\u0928\u092e\u0938\u094d\u0924\u0947,\u0928\u092e\u0938\u094d\u0915\u093e\u0930,kya,\u0939\u0947\u0932\u094b,\u0938\u0924\u094d\u092f,satya,\u0938\u0941\u0928\u093f\u092f\u0947,\u0938\u0932\u093e\u092e,\u0928\u092e\u0938\u0924\u0947,\u0939\u0948\u0932\u094b,\u0938\u0924 \u0936\u094d\u0930\u0940 \u0905\u0915\u093e\u0932', 'pronunciation': '(h\xc4\x95-l\xc5\x8d\xcb\x88, h\xc9\x99-)'}
        self.root = Tk()
        self.root.title("vocab-o-nary")
        self.root["bg"]=ROOTBG
        self.root["pady"] = 30
        self.root.minsize(width=800, height=200)
        self.customFont = tkFont.Font(family="Andalus", size=12,weight="bold")

        self.titleFrame = Frame(self.root,bg=ROOTBG)
        self.titleFrame["pady"]=30
        self.titleLabel = Label(self.titleFrame,fg="white",background="tan1")
        self.titleLabel["text"] = "VOCAB-O-NARY"
        self.titleLabel["font"] = tkFont.Font(family="Castellar", size=30,weight="bold") 
        self.titleLabel["relief"] = GROOVE
        self.titleLabel["padx"]=10
        self.titleLabel.pack()
        self.titleFrame.pack()

        
        self.backFrame= Frame(self.root,bg=ROOTBG)
        self.button = Button(self.backFrame,text="<- Go back",command=self.searchagain)
        self.button.pack()
        self.backFrame["pady"]=5
        self.backFrame["padx"]=5
        self.backFrame.pack(side=BOTTOM,anchor=E)
        
        self.titleFrame = Frame(self.root,bg=ROOTBG)
        self.titleFrame["pady"]=20
        self.titleLabel = Label(self.titleFrame,fg="white",background="MediumPurple1")
        self.titleLabel["text"] = query
        self.titleLabel["font"] = tkFont.Font(family="Arial Rounded MT Bold", size=25,weight="bold")
        self.titleLabel["relief"] = SUNKEN
        self.titleLabel["padx"]=10
        self.titleLabel.pack()
        self.titleFrame.pack()

        result=self.getresults(query)
        
        self.bar = TabBar(self.root,"meaning")
        self.bar.config(bd=2, relief=FLAT)
        
        self.tab1 = Tab(self.root,"meaning")
        Label(self.tab1, text=result['meaning'], bg="turquoise", fg="white",font=self.customFont,wraplength=800, width=80).pack(side=TOP, expand=NO, fill=Y)
        self.bar.add(self.tab1)
        
        self.tab2 = Tab(self.root,"translation")
        Label(self.tab2, text=result['translation'], bg="turquoise", fg="white", font=self.customFont,wraplength=800, width=80).pack(side=TOP, expand=NO, fill=BOTH)
        self.bar.add(self.tab2)
        
        self.tab3 = Tab(self.root,"usage")
        Label(self.tab3, text=result['usage'],pady=10, bg="turquoise", fg="white",font=self.customFont,wraplength=800, width=80).pack(side=TOP, expand=NO, fill=BOTH)
        self.bar.add(self.tab3)
        
        self.tab4 = Tab(self.root,"antonyms")
        Label(self.tab4, text=result['antonyms'], bg="turquoise", fg="white", font=self.customFont,wraplength=800, width=80).pack(side=TOP, expand=NO, fill=BOTH)
        self.bar.add(self.tab4)

        self.tab5 = Tab(self.root,"synonyms")
        Label(self.tab5, text=result['synonyms'],  bg="turquoise", fg="white", font=self.customFont,wraplength=800, width=80).pack(side=TOP, expand=NO, fill=BOTH)
        self.bar.add(self.tab5)

        self.tab6 = Tab(self.root,"pronunciation")
        Label(self.tab6, text=result['pronunciation'],  bg="turquoise", fg="white",font=self.customFont, wraplength=800,width=80).pack(side=TOP, expand=NO, fill=BOTH)
        self.bar.add(self.tab6)
        
        self.bar.show()
        self.root.mainloop()

    def searchagain(self):
        self.root.destroy()
        SEARCH()

        
    def getresults(self,query):
    
        self.waitFrame = Frame(self.root,bg=ROOTBG)
        self.titleLabel["padx"]=10
        self.waitFrame["pady"]=20
        self.waitLabel = Label(self.waitFrame,fg="goldenrod1",bg=ROOTBG)
        self.waitLabel["font"] = tkFont.Font(family="Arial Rounded MT Bold", size=25,weight="bold")
        self.waitLabel["relief"] = FLAT
        self.waitLabel.pack()
        self.waitFrame.pack()
        self.waitLabel.config(text ="Loading...")
        self.waitLabel.update_idletasks()
        result=vocab.create_result(query)
        self.waitFrame.destroy()
        return result
        



class SEARCH():
    def __init__(self):
        self.root = Tk()
        self.root.title("vocab-o-nary")
        self.root["padx"] = 0
        self.root["pady"] = 0
        self.root["bg"]=ROOTBG
        self.root.minsize(width=800, height=250)

        self.customFont = tkFont.Font(family="Castellar", size=30,weight="bold") 

        self.titleFrame = Frame(self.root,bg=ROOTBG)
        self.titleFrame["pady"]=40
        self.titleLabel = Label(self.titleFrame,fg="white",background="tan1")
        self.titleLabel["padx"]=10
        self.titleLabel["text"] = "VOCAB-O-NARY"
        self.titleLabel["font"] = self.customFont
        self.titleLabel["relief"] =  GROOVE
        self.titleLabel.pack()
        self.titleFrame.pack(side=TOP)
        

        self.textFrame = Frame(self.root,bg=ROOTBG)
        self.entryLabel = Label(self.textFrame,bg=ROOTBG,fg="OrangeRed2")
        self.entryLabel["text"] = "Enter the word here:"
        self.entryLabel["font"] = tkFont.Font(family="Andalus", size=12,weight="bold")
        self.entryLabel.pack(side=LEFT)
        
        self.entryWidget = Entry(self.textFrame,bg="cornsilk2")
        self.entryWidget["width"] = 30
        self.entryWidget["font"] = tkFont.Font(family="Times", size=15)
        self.entryWidget.pack(side=LEFT)

        self.entryFrame= Frame(self.textFrame,bg=ROOTBG)
        self.button = Button(self.entryFrame,text="Search",command=self.displayresult,bg="tomato2",fg="white")
        self.button.pack()
        self.entryFrame["padx"]=5
        self.entryFrame.pack()
        self.textFrame.pack()
        

        self.baseFrame = Frame(self.root,bg=ROOTBG)
        self.baseFrame["pady"]=20
        self.baseLabel = Label(self.baseFrame,fg="white",background="black",wraplength=800, width=80)
        self.baseLabel["text"] = "Search for a word and get to know its meaning,usage examples,synonyms,antonyms and pronunciation."
        self.baseLabel["font"] = tkFont.Font(family="Andalus", size=10,weight="bold")
        self.baseLabel["relief"] = GROOVE
        self.baseLabel["padx"]=10
        self.baseLabel.pack()
        self.baseFrame.pack(anchor=S,side=BOTTOM)

        self.root.mainloop() 

    def displayresult(self):
            query=self.entryWidget.get().strip()
            self.root.destroy()
            RESULT(query)
        

        
        
if __name__ == "__main__":
  SEARCH()       
