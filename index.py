import requests
from bs4 import BeautifulSoup
import re
import smtplib
import time
import sys
import schedule
from datetime import datetime
from Tkinter import *
import tkMessageBox
import csv

#Url='https://www.amazon.in/Samsung-Galaxy-Ocean-Blue-32GB/dp/B07HGH8JWQ/ref=sr_1_1_sspa?keywords=mobiles&qid=1569055700&sr=8-1-spons&psc=1&shpLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFFVFpLUlhURlg1RUUmZW5jcnlwdGVkSWQ9QTA5NTExMzgyQjhSTEFDNThEWjE4JmVuY3J5cHRlZEFkSWQ9QTA5NTI3NTYxU1RMVTAwNEE2M083JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='



headers ={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

#checking price
def check_price():
	
	page =requests.get(s,headers=headers)

	soup=BeautifulSoup(page.content,'html.parser')
	global t
	global trr
	global stock
	global sentence
	t = (soup.find(id="productTitle").get_text()).strip()
	trr = soup.find(id="bylineInfo").get_text()
	stock = (soup.find(id="availability").get_text()).strip()
	features =(soup.find(id="feature-bullets").get_text()).strip()
	print(t)
	print("Manufactured by = "+trr)
	print(stock[0:8])
	global q
        q=stock[0:8]
        #print(q)
	sentence = re.sub(r"\s+", "",features, flags=re.UNICODE)
	#print(sentence)
        print(features)
       
	js_test = soup.find('span', id ='priceblock_ourprice') 
	if js_test is None: 
    		js_test = soup.find('span', id ='priceblock_dealprice')         
	str = "     " 

	for line in js_test.stripped_strings : 
    		str = line 
# convert to integer 
        global my
        global converted
	converted = int(float(re.sub(r"[^\d.]", "",str)))
	myorder = "Product price is Rs {}"
	my=myorder.format(converted)
	print(myorder.format(converted))
       
def lab():
        
        Label7 = Label(top,font=('Helvetica',11, 'bold'),wraplength=500)
        Label7.place(x=35,y=280)
        Label7.configure(text='Product Name '+t)
        Label7.configure(background="#b7e5ed")
        
        
        Label8 = Label(top,font=('Helvetica',12, 'bold'))
        Label8.place(x=35,y=330)
        Label8.configure(text="Manufactured by = "+trr)
        Label8.configure(background="#b7e5ed")
        
        
        Label9 = Label(top,font=('Helvetica',12, 'bold'))
        Label9.place(x=35,y=360)
        Label9.configure(text="Product Is "+stock)
        Label9.configure(background="#b7e5ed")
        
        Label10 = Label(top,font=('Helvetica',13, 'bold'))
        Label10.place(x=35,y=390)
        Label10.configure(text=my)
        Label10.configure(background="#b7e5ed")
        
        m=str(datetime.date(datetime.now()))
        print(m)
        Label16 = Label(top,font=('Helvetica',13, 'bold'))
        Label16.place(x=35,y=460)
        Label16.configure(text='Date:'+m)
        Label16.configure(background="#b7e5ed")
        
def ch():

	if (converted<price) :
                print('inside sending email')
		send_mail(email)
		Label11 = Label(top,font=('Helvetica',13, 'bold'))
                Label11.place(x=35,y=420)
                Label11.configure(text='Email sent')
                Label11.configure(background="#b7e5ed") 
        else:
                
                schedule.every(2).seconds.do(check_price)
                print('email not sent')
	        while 1:
	                
	                schedule.run_pending()
	               	time.sleep(1)      	
	                ch()     	
	       
#send mail 
def send_mail(email):
     
 	        server=smtplib.SMTP('smtp.gmail.com',587)
                server.ehlo()
                server.starttls()
	        server.ehlo()
                
                server.login('peter.parker98652@gmail.com','spiderman@00')
                sub='''Price Fell Down! 
           Current Price {} 
           check the Amazon link {} '''

                h=sub.format(converted,s)
                msg=h
                server.sendmail('peter.parker98652@gmail.com',email,msg)
                
                
                
	        #print(datetime.today())        
	        print('Email sent')
                server.quit()
	        #sys.exit()


top=Tk();

top.geometry('800x500')
top.title("PROJECT")
top.configure(background="#b7e5ed")
top.resizable(0,0)
#clear the data
def clearBox():
        Text1.delete('0',END)
        Text2.delete('0',END)
        Text3.delete('0',END)
#only number
def only_numbers(char):
        return char.isdigit()
validation = top.register(only_numbers)



def p():
	if(Text2.get()==""):
                tkMessageBox.showinfo("Warning","Please Enter Valid Url")
        else:
		global s
		s=Text2.get()
		#print(s)
		check_price()
		lab()


def j():
	if(Text3.get()=="" and Text1.get()==""):
        	tkMessageBox.showinfo("Warning","Enter Valid Gmail-Id and Price")
        else:
		global price
	        price=Text3.get()
                price = int(price)
                print(price)
		global email
		email = Text1.get()
		ch()


Label1 = Label(top)
Label1.place(x=500, y=75)
_img0 = PhotoImage(file=r"/home/moro21/Downloads/hello.png")    
Label1.configure(image=_img0)
Label1.configure(background="#b7e5ed")		

Label3 = Label(top,font=('Helvetica', 40, 'bold'),fg="black")
Label3.place(relx=0.0,rely=0.0,height=41,width=1200)
Label3.configure(background="orange")
Label3.configure(text='''Price Tracker''')
Label3.pack(fill=X)

Label4 = Label(top,font=('Helvetica', 11, 'bold'))
Label4.place(x=20,y=120)
Label4.configure(text='''Enter gmail:''')
Label4.configure(background="#b7e5ed")
Text1 = Entry(top)
Text1.place(x=120,y=120,width=250)
Text1.configure(background="white")
Text1.configure(font="TkTextFont")
Text1.configure(selectbackground="#c4c4c4")

Label5 = Label(top,font=('Helvetica', 10, 'bold'))
Label5.place(x=20,y=80)
Label5.configure(text='URL:')
Label5.configure(background="#b7e5ed")
#Text2 = Entry(top,textvar="url")
Text2=Entry(top)
Text2.place(x=70,y=80,width=300)

Label6 = Label(top,font=('Helvetica', 11, 'bold'))
Label6.place(x=20,y=160)
Label6.configure(text='''Enter price:''')
Label6.configure(background="#b7e5ed")
Text3 = Entry(top,validate="key",validatecommand=(validation, '%S'))
Text3.place(x=120,y=160,width=250)
Text3.configure(background="white")
Text3.configure(font="TkTextFont")
Text3.configure(selectbackground="#c4c4c4")

Button1 = Button(top,command=p,bd=2)
Button1.place(x=400,y=80,height=25)
Button1.configure(text='''TRACK''')  	


Button2 = Button(top,bd=2,command=j)
Button2.place(x=200,y=210)
Button2.configure(text='''SHOW''')

Button3 = Button(top,command=clearBox,bd=2)
Button3.place(x=300,y=210)
Button3.configure(text='''RESET''')


	
mainloop()



