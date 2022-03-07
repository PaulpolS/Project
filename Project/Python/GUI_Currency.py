#โปรแกรมแปลงสกุลเงิน

# 1 THB = 0.026 EUR
# 1 THB = 3.486 JPY
# 1 THB = 0.031 USD
# 1 THB = 0.023 GBP

from tkinter import *
from tkinter import ttk
from unittest import result
root = Tk()
root.title("โปรแกรมแปลงสกุลเงิน")

money = IntVar() #รับตัวเลขจำนวนเต็ม
Label(text="จำนวนเงิน",padx=10,font=30).grid(row=0,sticky=W)
et1 = Entry(font=30,width=30,textvariable=money) #กล่องรับข้อความ
et1.grid(row=0,column=1)


choice = StringVar(value="โปรดเลือกสกุลเงิน") #ตัว combo box ที่เอาไว้เป็นกล่องกดเลือกลงมาได้
Label(text="เลือกสกุลเงิน",padx=10,font=30).grid(row=1,sticky=W)
combo =ttk.Combobox(width=30,font=30,textvariable=choice)
combo["values"]=("EUR","JPY","USD","GBP")  # ตัวเลือกใน ComboBox
combo.grid(row=1,column=1)

def calculate():
    amount = money.get() #รับค่าในกล่อง money
    currency = choice.get() #รับค่าสกุลเงิน
    if currency == "EUR":
        et2.delete(0,END) #ก่อนจะเอาค่าไปแสดงใน et2 ต้องทำการลบเคลียค่าก่อน
        amount = amount * 0.026
        result = (amount,"EUR") 
        et2.insert(0,result) #เอาค่าที่ได้ไปแสดงใน et2
    
    elif currency == "JPY":
         et2.delete(0,END)
         amount = amount * 3.486
         result = (amount,"JPY")
         et2.insert(0,result)
    
    elif currency == "USD":
         et2.delete(0,END)
         amount = amount * 0.031
         result = (amount,"USD")
         et2.insert(0,result)
    
    elif currency == "GBP":
         et2.delete(0,END)
         amount = amount * 0.023
         result = (amount,"GBP")
         et2.insert(0,result)

def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)        

#output กล่องโชว์ผลการคำนวน
Label(text="ผลการคำนวน",padx=10,font=30).grid(row=2,sticky=W)
et2 = Entry(font=30,width=30) #กล่องรับข้อความ
et2.grid(row=2,column=1)

#ปุ่มต่างๆ
Button(text="คำนวณ",font=30,width=15,command=calculate).grid(row=3,column=1,sticky=W) #Sticky W=ซ้าย E=ขวา
Button(text="ล้าง",font=30,width=15,command=deleteText).grid(row=3,column=1,sticky=E)


root.mainloop()