from tkinter import *

from GUI_Currency import calculate
root = Tk()
root.title("เครื่องคิดเลข")

content = ""
txt_input = StringVar(value="0")
#รับค่าผ่านปุม

def btn(number):
    global content 
    content = content+str(number)
    txt_input.set(content)
#ปุ่มเท่ากับ
def equal():
    global content
    eval(content) #ใช้ฟังชั่นของไพท่อน
    calculate = float(eval(content))
    txt_input.set(calculate)
    content = ""

def clear():
    global content
    content = ""
    txt_input.set("")
    display.insert(0,"0")

#จอแสดงผล 5x4 
display = Entry(font=('arial',30,'bold'),fg="white",bg="grey",textvariable=txt_input,justify="right")
display.grid(columnspan=4) #จัดตำแหน่งมี4 ช่อง

#row1
btn7 = Button(fg="black",font=('arial',30,'bold'),text="7",command=lambda:btn(7),padx=30,pady=15).grid(row=1,column=0)
btn8 = Button(fg="black",font=('arial',30,'bold'),text="8",command=lambda:btn(8),padx=30,pady=15).grid(row=1,column=1)
btn9 = Button(fg="black",font=('arial',30,'bold'),text="9",command=lambda:btn(9),padx=30,pady=15).grid(row=1,column=2)
#row1 ปุ่มเคลีย
btnClear = Button(fg="black",font=('arial',30,'bold'),text="C",command=clear,padx=30,pady=15).grid(row=1,column=3)
#row2
btn4 = Button(fg="black",font=('arial',30,'bold'),text="4",command=lambda:btn(4),padx=30,pady=15).grid(row=2,column=0)
btn5 = Button(fg="black",font=('arial',30,'bold'),text="5",command=lambda:btn(5),padx=30,pady=15).grid(row=2,column=1)
btn6 = Button(fg="black",font=('arial',30,'bold'),text="6",command=lambda:btn(6),padx=30,pady=15).grid(row=2,column=2)
#row2 ปุ่ม +
btnPlus = Button(fg="black",font=('arial',30,'bold'),text="+",command=lambda:btn("+"),padx=30,pady=15).grid(row=2,column=3)
#row3
btn1 = Button(fg="black",font=('arial',30,'bold'),text="1",command=lambda:btn(1),padx=30,pady=15).grid(row=3,column=0)
btn2 = Button(fg="black",font=('arial',30,'bold'),text="2",command=lambda:btn(2),padx=30,pady=15).grid(row=3,column=1)
btn3 = Button(fg="black",font=('arial',30,'bold'),text="3",command=lambda:btn(3),padx=30,pady=15).grid(row=3,column=2)
#row3 ปุ่ม -
btnMinus = Button(fg="black",font=('arial',30,'bold'),text="-",command=lambda:btn("-"),padx=35,pady=15).grid(row=3,column=3)
#row4 
btndot = Button(fg="black",font=('arial',30,'bold'),text=".",command=lambda:btn("."),padx=30,pady=15).grid(row=4,column=0)
btn0 = Button(fg="black",font=('arial',30,'bold'),text="0",command=lambda:btn(0),padx=30,pady=15).grid(row=4,column=1)
btnDiv = Button(fg="black",font=('arial',30,'bold'),text="/",command=lambda:btn("-"),padx=35,pady=15).grid(row=4,column=2)
btnX = Button(fg="black",font=('arial',30,'bold'),text="X",command=lambda:btn("x"),padx=30,pady=15).grid(row=4,column=3)

#row5
btnEqual = Button(fg="black",font=('arial',30,'bold'),text="=",command=equal,padx=30,pady=15).grid(row=5,column=1)
btnOpen = Button(fg="black",font=('arial',30,'bold'),text="(",command=lambda:btn("("),padx=30,pady=15).grid(row=5,column=2)
btnClose = Button(fg="black",font=('arial',30,'bold'),text=")",command=lambda:btn(")"),padx=30,pady=15).grid(row=5,column=3)

root.mainloop()