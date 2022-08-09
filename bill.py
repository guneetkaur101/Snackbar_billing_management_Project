from tkinter import *
import random
import os
import tempfile
import sys
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0") 
        self.root.configure(bg="#1d3557")
        self.root.title("Billing management System")
        title=Label(self.root,text="Snackbar management System",bd=12,relief=RIDGE,font=("Arial Black",20,"bold"),bg="#457b9d",fg="white").pack(fill=X)
#===================================================variables=======================================================================================
        self.burger=IntVar()
        self.noodles=IntVar()
        self.pasta=IntVar()
        self.pizza=IntVar()
        self.dosa=IntVar()
        self.pavbhaji=IntVar()
        self.pepsi=IntVar()
        self.thumbsup=IntVar()
        self.coke=IntVar()
        self.maaza=IntVar()
        self.mountaindew=IntVar()
        self.sprite=IntVar()  

        self.Total=IntVar()

        self.cost_burger=StringVar()
        self.cost_noodles=StringVar()
        self.cost_pasta=StringVar()
        self.cost_pizza=StringVar()
        self.cost_dosa=StringVar()
        self.cost_pavbhaji=StringVar()
        self.cost_pepsi=StringVar()
        self.cost_coke=StringVar()
        self.cost_thumbsup=StringVar()
        self.cost_mountaindew=StringVar()
        self.cost_sprite=StringVar()
        self.cost_maaza=StringVar()
        self.total_cost=StringVar()

        self.fastfood_tax=StringVar()
        self.colddrink_tax=StringVar()

        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()

        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        
        self.var1=IntVar()
        self.var2=IntVar()
        self.var3=IntVar()
        self.var4=IntVar()
        self.var5=IntVar()
        self.var6=IntVar()
        self.var7=IntVar()
        self.var8=IntVar()
        self.var9=IntVar()
        self.var10=IntVar()
        self.var11=IntVar()
        self.var12=IntVar()

       
#=====================================================customer details label frame=================================================================
        details=LabelFrame(self.root,text="Customer Details",font=("Arial Black",12),bg="#457b9d",fg="white",relief=GROOVE,bd=10)
        details.place(x=0,y=80,relwidth=1)
        cust_name=Label(details,text="Customer Name",font=("Arial Black",14),bg="#457b9d",fg="white").grid(row=0,column=0,padx=15)
        cust_entry=Entry(details,textvariable=self.c_name ,borderwidth=4,width=30).grid(row=0,column=1,padx=8)
        
        contact_name=Label(details,text="Contact No.",font=("Arial Black",14),bg="#457b9d",fg="white").grid(row=0,column=2,padx=10)
        contact_entry=Entry(details,textvariable=self.c_phone, borderwidth=4,width=30).grid(row=0,column=3,padx=8)

        bill_name=Label(details,text="Bill.No.",font=("Arial Black",14),bg="#457b9d",fg="white").grid(row=0,column=4,padx=15)
        bill_entry=Entry(details,textvariable=self.bill_no, borderwidth=4,width=30).grid(row=0,column=5,padx=8)
        bill_btn=Button(details,text="Search",command=self.find_bill,width=8,bd=5,font=("Arial Black",14)).grid(row=0,column=12,padx=12,pady=3)
#======================================================FASTFOOD label frame=================================================================
        snacks=LabelFrame(self.root,text="FAST FOOD",font=("Arial Black",12),bg="#a8dadc",fg="#1d3557",relief=GROOVE,bd=10)
        snacks.place(x=5,y=200,height=400,width=580)
        
        item1=Label(snacks,text="Burger ",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=1,column=0,pady=11,sticky='w')
        item1=Label(snacks,text="Rs 35",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=1,column=1,pady=11,sticky='n')
        item1ch_entry=Checkbutton(snacks,onvalue=1,offvalue=0,variable=self.var1,command=self.Enable_burger,font=("arial",10,'bold')).grid(row=1,column=2,sticky="w")
        self.item1sp_entry=Spinbox(snacks,from_=0,to=100,width=8,font=("times",14,"bold"),textvariable=self.burger,state=DISABLED)
        self.item1sp_entry.grid(row=1,column=2,padx=15)
        # item1_entry=Entry(snacks,textvariable=self.burger ,borderwidth=2,width=15).gr id(row=1,column=2,padx=10)
        item1_cost_entry=Entry(snacks,textvariable=self.cost_burger,borderwidth=2,width=15).grid(row=1,column=3,padx=10)

        item2=Label(snacks,text="Noodles ",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=2,column=0,pady=11,sticky='w')
        item2=Label(snacks,text="Rs 90(/plate)",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=2,column=1,pady=11,sticky='n')
        item2ch_entry=Checkbutton(snacks,onvalue=1,offvalue=0,variable=self.var2,command=self.Enable_noodles,font=("arial",10,'bold')).grid(row=2,column=2,sticky="w")
        self.item2sp_entry=Spinbox(snacks,from_=0,to=100,width=8,font=("times",14,"bold"),textvariable=self.noodles,state=DISABLED)
        self.item2sp_entry.grid(row=2,column=2,padx=15)
        # item2_entry=Entry(snacks,textvariable=self.noodles ,borderwidth=2,width=15).grid(row=2,column=2,padx=10)
        item2_cost_entry=Entry(snacks,textvariable=self.cost_noodles ,borderwidth=2,width=15).grid(row=2,column=3,padx=10)

        item3=Label(snacks,text="Pasta ",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=3,column=0,pady=11,sticky='w')
        item3=Label(snacks,text="Rs 150(/plate)",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=3,column=1,pady=11,sticky='n')
        item3ch_entry=Checkbutton(snacks,onvalue=1,offvalue=0,variable=self.var3,command=self.Enable_pasta,font=("arial",10,'bold')).grid(row=3,column=2,sticky="w")
        self.item3sp_entry=Spinbox(snacks,from_=0,to=100,width=8,font=("times",14,"bold"),textvariable=self.pasta,state=DISABLED)
        self.item3sp_entry.grid(row=3,column=2,padx=15)
        # item3_entry=Entry(snacks,textvariable=self.pasta ,borderwidth=2,width=15).grid(row=3,column=2,padx=10)
        item3_cost_entry=Entry(snacks,textvariable=self.cost_pasta,borderwidth=2,width=15).grid(row=3,column=3,padx=10)

        item4=Label(snacks,text="Pizza ",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=4,column=0,pady=11,sticky='w')
        item4=Label(snacks,text="Rs 250(Regular)",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=4,column=1,pady=11,sticky='n')
        item4ch_entry=Checkbutton(snacks,onvalue=1,offvalue=0,variable=self.var4,command=self.Enable_pizza,font=("arial",10,'bold')).grid(row=4,column=2,sticky="w")
        self.item4sp_entry=Spinbox(snacks,from_=0,to=100,width=8,font=("times",14,"bold"),textvariable=self.pizza,state=DISABLED)
        self.item4sp_entry.grid(row=4,column=2,padx=15)
        # item4_entry=Entry(snacks,textvariable=self.pizza ,borderwidth=2,width=15).grid(row=4,column=2,padx=10)
        item4_cost_entry=Entry(snacks,textvariable=self.cost_pizza ,borderwidth=2,width=15).grid(row=4,column=3,padx=10)

        item5=Label(snacks,text="Dosa ",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=5,column=0,pady=11,sticky='w')
        item5=Label(snacks,text="Rs 120(masala)",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=5,column=1,pady=11,sticky='n')
        item1ch_entry=Checkbutton(snacks,onvalue=1,offvalue=0,variable=self.var5,command=self.Enable_dosa,font=("arial",10,'bold')).grid(row=5,column=2,sticky="w")
        self.item5sp_entry=Spinbox(snacks,from_=0,to=100,width=8,font=("times",14,"bold"),textvariable=self.dosa,state=DISABLED)
        self.item5sp_entry.grid(row=5,column=2,padx=15)
        # item5_entry=Entry(snacks,textvariable=self.dosa ,borderwidth=2,width=15).grid(row=5,column=2,padx=10)
        item5_cost_entry=Entry(snacks,textvariable=self.cost_dosa ,borderwidth=2,width=15).grid(row=5,column=3,padx=10)
        
        item6=Label(snacks,text="Pav bhaji ",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=6,column=0,pady=11,sticky='w')
        item6=Label(snacks,text="Rs 100(with 2 pav)",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=6,column=1,pady=11,sticky='n')
        item1ch_entry=Checkbutton(snacks,onvalue=1,offvalue=0,variable=self.var6,command=self.Enable_pavbhaji,font=("arial",10,'bold')).grid(row=6,column=2,sticky="w")
        self.item6sp_entry=Spinbox(snacks,from_=0,to=100,width=8,font=("times",14,"bold"),textvariable=self.pavbhaji,state=DISABLED)
        self.item6sp_entry.grid(row=6,column=2,padx=15)
        # item6_entry=Entry(snacks,textvariable=self.pavbhaji,borderwidth=2,width=15).grid(row=6,column=2,padx=10)
        item6_cost_entry=Entry(snacks,textvariable=self.cost_pavbhaji ,borderwidth=2,width=15).grid(row=6,column=3,padx=10)

        itm=Label(snacks, text='Items', font=('times',15, 'bold','italic'),bg="#a8dadc",fg="#1d3557" )
        itm.grid(row=0,column=0,padx=8,pady=10)

        itm=Label(snacks, text='Price', font=('times',15, 'bold','italic'),bg="#a8dadc",fg="#1d3557" )
        itm.grid(row=0,column=1,padx=4,pady=10,sticky='n')

        n=Label(snacks, text='Number of Items', font=('times',15, 'bold','italic'),bg="#a8dadc",fg="#1d3557")
        n.grid(row=0,column=2,padx=8,pady=10)

        cost=Label(snacks, text='Cost of Items', font=('times',15, 'bold','italic'),bg="#a8dadc",fg="#1d3557")
        cost.grid(row=0,column=3,padx=8,pady=10)

#================================================COLD DRINKS===================================================================================
        colddrink=LabelFrame(self.root,text="COLD DRINKS",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#a8dadc",fg="#1d3557")
        colddrink.place(x=600,y=200,height=400,width=575)

        item7=Label(colddrink,text="Pepsi(750ML) ",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=1,column=0,pady=11,sticky='w')
        item7=Label(colddrink,text="Rs 45",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=1,column=1,pady=11,sticky='n')
        item7ch_entry=Checkbutton(colddrink,onvalue=1,offvalue=0,variable=self.var7,command=self.Enable_pepsi,font=("arial",10,'bold')).grid(row=1,column=2,padx=20,sticky="w")
        self.item7sp_entry=Spinbox(colddrink,from_=0,to=100,width=8,font=("times",14,"bold"),textvariable=self.pepsi,state=DISABLED)
        self.item7sp_entry.grid(row=1,column=2,padx=55)
        # item7_entry=Entry(colddrink,textvariable=self.pepsi ,borderwidth=2,width=15).grid(row=1,column=2,padx=10)
        item7_cost_entry=Entry(colddrink,textvariable=self.cost_pepsi ,borderwidth=2,width=15).grid(row=1,column=3,padx=10)

        item8=Label(colddrink,text="Thumbs up ",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=2,column=0,pady=11,sticky='w')
        item8=Label(colddrink,text="Rs 38",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=2,column=1,pady=11,sticky='n')
        item1ch_entry=Checkbutton(colddrink,onvalue=1,offvalue=0,variable=self.var8,command=self.Enable_thumbsup,font=("arial",10,'bold')).grid(row=2,column=2,padx=20,sticky="w")
        self.item8sp_entry=Spinbox(colddrink,from_=0,to=100,width=8,font=("times",14,"bold"),textvariable=self.thumbsup,state=DISABLED)
        self.item8sp_entry.grid(row=2,column=2,padx=15)
        # item8_entry=Entry(colddrink,textvariable=self.thumbsup ,borderwidth=2,width=15).grid(row=2,column=2,padx=10)
        item8_cost_entry=Entry(colddrink,textvariable=self.cost_thumbsup ,borderwidth=2,width=15).grid(row=2,column=3,padx=10)

        item9=Label(colddrink,text="Coke ",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=3,column=0,pady=11,sticky='w')
        item9=Label(colddrink,text="Rs 48",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=3,column=1,pady=11,sticky='n')
        item9ch_entry=Checkbutton(colddrink,onvalue=1,offvalue=0,variable=self.var9,command=self.Enable_coke,font=("arial",10,'bold')).grid(row=3,column=2,padx=20,sticky="w")
        self.item9sp_entry=Spinbox(colddrink,from_=0,to=100,width=8,font=("times",14,"bold"),textvariable=self.coke,state=DISABLED)
        self.item9sp_entry.grid(row=3,column=2,padx=15)
        # item9_entry=Entry(colddrink,textvariable=self.coke ,borderwidth=2,width=15).grid(row=3,column=2,padx=10)
        item9_cost_entry=Entry(colddrink,textvariable=self.cost_coke ,borderwidth=2,width=15).grid(row=3,column=3,padx=10)

        item10=Label(colddrink,text="Maaza ",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=4,column=0,pady=11,sticky='w')
        item10=Label(colddrink,text="Rs 35",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=4,column=1,pady=11,sticky='n')
        item10ch_entry=Checkbutton(colddrink,onvalue=1,offvalue=0,variable=self.var10,command=self.Enable_maaza,font=("arial",10,'bold')).grid(row=4,column=2,padx=20,sticky="w")
        self.item10sp_entry=Spinbox(colddrink,from_=0,to=100,width=8,font=("times",14,"bold"),textvariable=self.maaza,state=DISABLED)
        self.item10sp_entry.grid(row=4,column=2,padx=15)
        # item10_entry=Entry(colddrink,textvariable=self.maaza ,borderwidth=2,width=15).grid(row=4,column=2,padx=10)
        item10_cost_entry=Entry(colddrink,textvariable=self.cost_maaza ,borderwidth=2,width=15).grid(row=4,column=3,padx=10)

        item11=Label(colddrink,text="Mountain dew ",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=5,column=0,pady=11,sticky='w')
        item11=Label(colddrink,text="Rs 30",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=5,column=1,pady=11,sticky='n')
        item11ch_entry=Checkbutton(colddrink,onvalue=1,offvalue=0,variable=self.var11,command=self.Enable_mountaindew,font=("arial",10,'bold')).grid(row=5,column=2,padx=20,sticky="w")
        self.item11sp_entry=Spinbox(colddrink,from_=0,to=100,width=8,font=("times",14,"bold"),textvariable=self.mountaindew,state=DISABLED)
        self.item11sp_entry.grid(row=5,column=2,padx=15)
        # item11_entry=Entry(colddrink,textvariable=self.mountaindew,borderwidth=2,width=15).grid(row=5,column=2,padx=10)
        item11_cost_entry=Entry(colddrink,textvariable=self.cost_mountaindew ,borderwidth=2,width=15).grid(row=5,column=3,padx=10)

        item12=Label(colddrink,text="Sprite ",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=6,column=0,pady=11,sticky='w')
        item12=Label(colddrink,text="Rs 45",font=("Arial Black",11),bg="#a8dadc",fg="#1d3557").grid(row=6,column=1,pady=11,sticky='n')
        item12ch_entry=Checkbutton(colddrink,onvalue=1,offvalue=0,variable=self.var12,command=self.Enable_sprite,font=("arial",10,'bold')).grid(row=6,column=2,padx=20,sticky="w")
        self.item12sp_entry=Spinbox(colddrink,from_=0,to=100,width=8,font=("times",14,"bold"),textvariable=self.sprite,state=DISABLED)
        self.item12sp_entry.grid(row=6,column=2,padx=15)
        # item12_entry=Entry(colddrink,textvariable=self.sprite ,borderwidth=2,width=15).grid(row=6,column=2,padx=10)
        item12_cost_entry=Entry(colddrink,textvariable=self.cost_sprite ,borderwidth=2,width=15).grid(row=6,column=3,padx=10)


        itm=Label(colddrink, text='Items', font=('times',15, 'bold','italic'),bg="#a8dadc",fg="#1d3557" )
        itm.grid(row=0,column=0,padx=15,pady=10)

        itm=Label(colddrink, text='Price', font=('times',15, 'bold','italic'),bg="#a8dadc",fg="#1d3557" )
        itm.grid(row=0,column=1,padx=15,pady=10)

        n=Label(colddrink, text='Number of Items', font=('times',15, 'bold','italic'),bg="#a8dadc",fg="#1d3557")
        n.grid(row=0,column=2,padx=15,pady=10)
  
        cost=Label(colddrink, text='Cost of Items', font=('times',15, 'bold','italic'),bg="#a8dadc",fg="#1d3557")
        cost.grid(row=0,column=3,padx=15,pady=10)
        
#========================================================================Bill Area==============================================================================
        billarea=Frame(self.root,bd=10,relief=GROOVE,bg="#a8dadc")
        billarea.place(x=1190,y=200,width=330,height=400)
        
        bill_title=Label(billarea,text="Bill Area",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#a8dadc",fg="#1d3557").pack(fill=X)
        
        scrol_y=Scrollbar(billarea,orient=VERTICAL)
        self.textarea=Text(billarea,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
#========================================================Billing Options=========================================================================================
       
        billing_menu=LabelFrame(self.root,text="Billing Options",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#457b9d",fg="white")
        billing_menu.place(x=0,y=620,relwidth=1,height=137)

# =====================================================================Button frames================================================================================

        button_frame=Frame(billing_menu,bd=7,relief=GROOVE,bg="#1d3557")
        button_frame.place(x=350,width=820,height=95)
        
        button_total=Button(button_frame,text="Total ",command=self.total,font=("Arial Black",15),pady=10,width=9,bg="#a8dadc",fg="#1d3557").grid(row=0,column=0,padx=16)
        button_clear=Button(button_frame,text="Reset",font=("Arial Black",15),pady=10,width=9,command=self.reset,bg="#a8dadc",fg="#1d3557").grid(row=0,column=3,padx=10,pady=6)
        button_receipt=Button(button_frame,text="Total Bill",font=("Arial Black",15),pady=10,width=9,command=self.bill,bg="#a8dadc",fg="#1d3557").grid(row=0,column=1,padx=10,pady=6)
        button_print=Button(button_frame,text="Print",font=("Arial Black",15),pady=10,width=9,command=self.print,bg="#a8dadc",fg="#1d3557").grid(row=0,column=2,padx=10,pady=6)
        button_exit=Button(button_frame,text="Exit",font=("Arial Black",15),pady=10,width=9,command=self.exit,bg="#a8dadc",fg="#1d3557").grid(row=0,column=4,padx=10,pady=6)
        self.intro()
        
#=========================================================================Function===================================================================================
    def Enable_burger(self):
        if (self.var1.get()==1):
            self.item1sp_entry.configure(state=NORMAL)
        elif self.var1.get()==0:
            self.item1sp_entry.configure(state=DISABLED)
            self.burger.set("0")
   
    def Enable_noodles(self):
        if (self.var2.get()==1):
            self.item2sp_entry.configure(state=NORMAL)
        elif self.var2.get()==0:
            self.item2sp_entry.configure(state=DISABLED)
            self.noodles.set("0")

    def Enable_pasta(self):
        if (self.var3.get()==1):
            self.item3sp_entry.configure(state=NORMAL)
        elif self.var3.get()==0:
            self.item3sp_entry.configure(state=DISABLED)
            self.pasta.set("0")

    def Enable_pizza(self):
        if (self.var4.get()==1):
            self.item4sp_entry.configure(state=NORMAL)
        elif self.var4.get()==0:
            self.item4sp_entry.configure(state=DISABLED)
            self.pizza.set("0")

    def Enable_dosa(self):
        if (self.var5.get()==1):
            self.item5sp_entry.configure(state=NORMAL)
        elif self.var5.get()==0:
            self.item5sp_entry.configure(state=DISABLED)
            self.dosa.set("0")

    def Enable_pavbhaji(self):
        if (self.var6.get()==1):
            self.item6sp_entry.configure(state=NORMAL)
        elif self.var6.get()==0:
            self.item6sp_entry.configure(state=DISABLED)
            self.pavbhaji.set("0")
    
    def Enable_pepsi(self):
        if (self.var7.get()==1):
            self.item7sp_entry.configure(state=NORMAL)
        elif self.var7.get()==0:
            self.item7sp_entry.configure(state=DISABLED)
            self.pepsi.set("0")
    
    def Enable_thumbsup(self):
        if (self.var8.get()==1):
            self.item8sp_entry.configure(state=NORMAL)
        elif self.var8.get()==0:
            self.item8sp_entry.configure(state=DISABLED)
            self.thumbsup.set("0")

    def Enable_coke(self):
        if (self.var9.get()==1):
            self.item9sp_entry.configure(state=NORMAL)
        elif self.var9.get()==0:
            self.item9sp_entry.configure(state=DISABLED)
            self.coke.set("0")
    
    def Enable_maaza(self):
        if (self.var10.get()==1):
            self.item10sp_entry.configure(state=NORMAL)
        elif self.var10.get()==0:
            self.item10sp_entry.configure(state=DISABLED)
            self.maaza.set("0")

    def Enable_mountaindew(self):
        if (self.var11.get()==1):
            self.item11sp_entry.configure(state=NORMAL)
        elif self.var11.get()==0:
            self.item11sp_entry.configure(state=DISABLED)
            self.mountaindew.set("0")

    def Enable_sprite(self):
        if (self.var12.get()==1):
            self.item12sp_entry.configure(state=NORMAL)
        elif self.var12.get()==0:
            self.item12sp_entry.configure(state=DISABLED)
            self.sprite.set("0")


    def total(self):

        if (self.c_name.get()=="" or self.c_phone.get()==""):
            messagebox.showerror("Error", "Fill the complete Customer Details!!")

        elif self.burger.get()==0 and self.noodles.get()==0 and self.pizza.get()==0 and self.dosa.get()==0 and self.pasta.get()==0 and self.pavbhaji.get()==0 and self.pepsi.get()==0 and self.coke.get()==0 and self.maaza.get()==0 and self.sprite.get()==0 and self.thumbsup.get()==0 and self.mountaindew.get()==0:
            messagebox.showerror('Error','Please select number of quantity')
        else:
            self.b=self.burger.get()
            self.n=self.noodles.get()
            self.pi=self.pizza.get()
            self.d=self.dosa.get()
            self.pa=self.pasta.get()
            self.pb=self.pavbhaji.get()
            self.pep=self.pepsi.get()   
            self.th=self.thumbsup.get()
            self.mo= self.mountaindew.get()
            self.sp=self.sprite.get()
            self.c=self.coke.get()
            self.m= self.maaza.get()

            t=float(self.b*35+self.n*90+self.pi*250+self.d*120+self.pa*150+self.pb*100+self.pep*45+self.th*38+self.mo*30+self.sp*45+self.c*48+self.m*35)
            self.Total.set(self.b+self.n+self.pi+self.d+self.pa+self.pb+self.pep+self.th+self.mo+self.sp+self.c+self.m)
            self.total_cost.set('Rs ' + str(round(t, 2)))

            self.cost_burger.set('Rs '+str(round(self.b * 35, 2)))
            self.cost_noodles.set('Rs '+str(round(self.n*90,2)))
            self.cost_pizza.set('Rs '+str(round(self.pi*250,2)))
            self.cost_dosa.set('Rs '+str(round(self.d*120,2)))
            self.cost_pasta.set('Rs '+str(round(self.pa*150, 2)))
            self.cost_pavbhaji.set('Rs '+str(round(self.pb*100,2)))
            self.cost_pepsi.set('Rs '+str(round(self.pep*45,2)))
            self.cost_coke.set('Rs '+str(round(self.c*48,2)))
            self.cost_thumbsup.set('Rs '+str(round(self.th*38, 2)))
            self.cost_mountaindew.set('Rs '+str(round(self.mo*30,2)))
            self.cost_sprite.set('Rs '+str(round(self.sp*45,2)))
            self.cost_maaza.set('Rs '+str(round(self.m*35,2)))
        
    def intro(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\tWELCOME TO SNACKOPEDIA\n\tPhone-No.739275410")
        self.textarea.insert(END,f"\n\nBill no. : {self.bill_no.get()}")
        self.textarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
        self.textarea.insert(END,f"\nPhone No. : {self.c_phone.get()}")
        self.textarea.insert(END,"\n====================================\n")
        self.textarea.insert(END,"\nProduct\t\tQty\tPrice\n")
        self.textarea.insert(END,"\n====================================\n")
    def bill(self):
        self.intro()
        if self.burger.get()!=0:
            self.textarea.insert(END,f"Burger\t\t {self.burger.get()}\t{self.cost_burger.get()}\n")
        if self.noodles.get()!=0:
            self.textarea.insert(END,f"Noodles\t\t {self.noodles.get()}\t{self.cost_noodles.get()}\n")
        if self.pizza.get()!=0:
            self.textarea.insert(END,f"Pizza\t\t {self.pizza.get()}\t{self.cost_pizza.get()}\n")
        if self.dosa.get()!=0:
            self.textarea.insert(END,f"Dosa\t\t {self.dosa.get()}\t{self.cost_dosa.get()}\n")
        if self.pasta.get()!=0:
            self.textarea.insert(END,f"Pasta\t\t {self.pasta.get()}\t{self.cost_pasta.get()}\n")
        if self.pavbhaji.get()!=0:
            self.textarea.insert(END,f"Pav Bhaji\t\t {self.pavbhaji.get()}\t{self.cost_pavbhaji.get()}\n")
        if self.pepsi.get()!=0:
            self.textarea.insert(END,f"Pepsi\t\t {self.pepsi.get()}\t{self.cost_pepsi.get()}\n")
        if self.thumbsup.get()!=0:
            self.textarea.insert(END,f"ThumbsUp\t\t {self.thumbsup.get()}\t{self.cost_thumbsup.get()}\n")
        if self.mountaindew.get()!=0:
            self.textarea.insert(END,f"MountainDew\t\t {self.mountaindew.get()}\t{self.cost_mountaindew.get()}\n")
        if self.sprite.get()!=0:
            self.textarea.insert(END,f"Sprite\t\t {self.sprite.get()}\t{self.cost_sprite.get()}\n")
        if self.coke.get()!=0:
            self.textarea.insert(END,f"Coke\t\t {self.coke.get()}\t{self.cost_coke.get()}\n")
        if self.maaza.get()!=0:
            self.textarea.insert(END,f"Maaza\t\t {self.maaza.get()}\t{self.cost_maaza.get()}\n")
        self.textarea.insert(END,f"------------------------------------\n\n")
    
        self.textarea.insert(END,f"Total Amount:\t\t {self.Total.get()}\t{self.total_cost.get()}\n")
        self.textarea.insert(END,f"------------------------------------\n")
        self.save_bill()
    
    def reset(self):
        op= messagebox.askyesno('RESET','Do you really want to reset?')
        if op>0:
            self.textarea.delete('1.0',END)
            self.c_name.set('')
            self.c_phone.set('')
            self.bill_no.set(' ')
            self.burger.set(0)
            self.noodles.set(0)
            self.pasta.set(0)
            self.pizza.set(0)
            self.pavbhaji.set(0)
            self.dosa.set(0)
            self.coke.set(0)
            self.sprite.set(0)
            self.mountaindew.set(0)
            self.maaza.set(0)
            self.thumbsup.set(0)
            self.pepsi.set(0)
            self.Total.set(0)
            self.cost_burger.set('')
            self.cost_noodles.set('')
            self.cost_pasta.set('')
            self.cost_pizza.set('')
            self.cost_dosa.set('')
            self.cost_pavbhaji.set('')
            self.cost_pepsi.set('')
            self.cost_coke.set('')
            self.cost_thumbsup.set('')
            self.cost_mountaindew.set('')
            self.cost_sprite.set('')
            self.cost_maaza.set('')
            self.total_cost.set('')

            x=random.randint(1000,9999)
            self.bill_no.set(str(x)) 
            self.intro()
            self.var1.set(0)
            self.item1sp_entry.configure(state=DISABLED)  
            self.var2.set(0)
            self.item2sp_entry.configure(state=DISABLED)   
            self.var3.set(0)
            self.item3sp_entry.configure(state=DISABLED)  
            self.var4.set(0)
            self.item4sp_entry.configure(state=DISABLED)  
            self.var5.set(0)
            self.item5sp_entry.configure(state=DISABLED)  
            self.var6.set(0)
            self.item6sp_entry.configure(state=DISABLED)  
            self.var7.set(0)
            self.item7sp_entry.configure(state=DISABLED)  
            self.var8.set(0)
            self.item8sp_entry.configure(state=DISABLED)  
            self.var9.set(0)
            self.item9sp_entry.configure(state=DISABLED)  
            self.var10.set(0)
            self.item10sp_entry.configure(state=DISABLED)  
            self.var11.set(0)
            self.item11sp_entry.configure(state=DISABLED)  
            self.var12.set(0)
            self.item12sp_entry.configure(state=DISABLED)  
            
    def print(self):
        q=self.textarea.get('1.0','end-1c')
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,'Print')

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} saved successfully")
        else:
            return  

            
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            q=i.split('.')[0]
            if q==self.bill_no.get():
                # print (q)

                f1=open(f"bills/{q}.txt","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill no.")

    def exit(self):
        if messagebox.askyesno('Exit','Do you really want to exit'):
            self.root.destroy()
root=Tk()
obj=Bill_App(root)
root.mainloop()