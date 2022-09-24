#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(host="localhost",port="3306",user="root", password="root", database="student database")


def insert(name,aadhar card number,parents name,ph number, Class, section):
    res = con.cursor()
    sql = "insert into users (name,aadhar card number,parents name,ph number, class and section) values (%s,%s,%s,%s,%s,%s)"
    user = (name,aadhar card number,parents name,ph number, Class , section)
    res.execute(sql, user)
    con.commit()
    print("Data Insert Success")


def update(name,aadhar card number,parents name,ph number, Class , section,id):
    res = con.cursor()
    sql = "update users set name=%s,aadhar card number=%s,parents number=%s,ph number=%s,class=%s,section=%s where id=%s"
    user = (name,aadhar card number,parents name,ph number, Class , section,id)
    res.execute(sql, user)
    con.commit()
    print("Data Update Success")



def select():
    res = con.cursor()
    sql = "SELECT ID,NAME,AADHAR CARD NUMBER,PARENTS NAME,PH NUMBER, CLASS , SECTION from users"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result, headers=["ID", "NAME", "AADHAR CARD NUMBER", "PARENTS NAME" , "PH NUMBER" , "CLASS" ,"SECTION"]))


def delete(id):
    res = con.cursor()
    sql = "delete from users where id=%s"
    user = (id,)
    res.execute(sql, user)
    con.commit()
    print("Data Delete Success")



while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        name = input("Enter Name : ")
        aadhar card number = input("Enter Aadhar Card Number : ")
        parents name = input("Enter Parents Name : ")
        ph number = input("Enter Ph Number : ")
        class = input(" Enter Class : ")
        section = input(" Enter Section : ")
        insert (name,aadhar card number,parents name,ph number, class , section)
        
    elif choice == 2:
        id = input("Enter The Id : ")
        name = input("Enter Name : ")
        aadhar card number = input("Enter Aadhar Card Number : ") 
        parents name = input("Enter Parents Name : ")
        ph number = input("Enter Ph Number : ")
        class = input(" Enter Class : ")
        section = input(" Enter Section : ")
        update (name,aadhar card number,parents name,ph number, class , section,id)
        
    elif choice == 3:
        select()
    elif choice == 4:
        id = input("Enter The Id to Delete : ")
        delete(id)
    elif choice == 5:
        quit()
    else:
        print("Invalid Selection . Please Try Again !")


# In[2]:


from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(host="localhost",port="3306",user="root", password="root", database="half yearly datasheet")

class student:
    marks = []
    def getdata(self,gid,math,science,social,language):
        student.gid = gid
        
        

    def displayData(self):
        print('gid is : " ,' student id)
        print('marks are: ",' student mark)
    
gid = int(input('enter student gid : "'))

s1 = student()
s1.getdata(gid,math,science,social,language)
s1.displayData()


# In[ ]:


from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(host="localhost",port="3306",user="root", password="root", database=" annual datasheet")

class student:
    marks = []
    def getdata(self,gid,math,science,social,language):
        student.gid = gid
        
        

    def displayData(self):
        print('gid is : " ,' student id)
        print('marks are: ",' student mark)
    
gid = int(input('enter student gid : "'))

s1 = student()
s1.getdata(gid,math,science,social,language)
s1.displayData()


# In[ ]:


from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(host="localhost",port="3306",user="root", password="root", database=" quarterly datasheet")

class student:
    marks = []
    def getdata(self,gid,math,science,social,language):
        student.gid = gid
        
        

    def displayData(self):
        print('gid is : " ,' student id)
        print('marks are: ",' student mark)
    
gid = int(input('enter student gid : "'))

s1 = student()
s1.getdata(gid,math,science,social,language)
s1.displayData()


# In[4]:


import mysql.connector
import tkinter as tk
from tkinter import ttk

r = tk.Tk()
r.title("student details")
r.geometry("600x300")
con = mysql.connector.connect(host="localhost",port="3306",user="root", password="root", database=" student details")

conn = connect.cursor()

conn.execute("SELECT * FROM data")

tree=ttk.Treeview(r)

tree["columns"]=("G_ID","NAME","AADHAR CARD NUMBER","PARENTS NAME","PH NUMBER", "CLASS" , "SECTION")

tree.column("G_ID", width=50 , minwidth =50 ,anchor=tk.CENTER)
tree.column("NAME", width=100 , minwidth =100 ,anchor=tk.CENTER)
tree.column("AADHAR CARD NUMBER", width=50 , minwidth =50 ,anchor=tk.CENTER)
tree.column("PARENTS NAME", width=150 , minwidth =150 ,anchor=tk.CENTER)
tree.column("PH NUMBER", width=150 , minwidth =150 ,anchor=tk.CENTER)
tree.column("CLASS", width=50 , minwidth =50 ,anchor=tk.CENTER)
tree.column("SECTION", width=50 , minwidth =50 ,anchor=tk.CENTER)

tree.heading("G_ID", text"G.Id",anchor=tk.CENTER)
tree.heading("NAME", text"Student name",anchor=tk.CENTER)
tree.heading("AADHAR CARD NUMBER", text"Student name",anchor=tk.CENTER)
tree.heading("PARENTS NAME", text"Parent name",anchor=tk.CENTER)
tree.heading("PH NUMBER", text"Phone number",anchor=tk.CENTER)
tree.heading("CLASS", text"Class",anchor=tk.CENTER)
tree.heading("SECTION", text"Section",anchor=tk.CENTER)

i=0
for ro in conn:
    tree.insert('', i , text="" , values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6]))
    i = i+1
    
tree.pack()

r.mainloop()


# In[ ]:




