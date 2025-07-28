import tkinter
from tkinter import *
top=tkinter.Tk()
top.title("Calculator")
top.geometry("323x470")
top.resizable(0,0)
l1=[]
sum=0
num1=0
ab=0
ans=1
def a():
    txt1.insert(INSERT,"1")
    l1.append(1)
def b():
    txt1.insert(INSERT,"2")
    l1.append(2)
def c():
    txt1.insert(INSERT,"3")
    l1.append(3)
def d():
    txt1.insert(INSERT,"4")
    l1.append(4)
def e():
    txt1.insert(INSERT,"5")
    l1.append(5)
def f():
    txt1.insert(INSERT,"6")
    l1.append(6)
def g():
    txt1.insert(INSERT,"7")
    l1.append(7)
def h():
    txt1.insert(INSERT,"8")
    l1.append(8)
def i():
    txt1.insert(INSERT,"9")
    l1.append(9)
def j():
    txt1.insert(INSERT,"0")
    l1.append(0)
def k():
    txt1.insert(INSERT,".")
    l1.append(".")
def plus():
    global sum
    global num1
    global ab
    txt1.delete(1.0,2.0)
    str1="".join(map(str,l1))
    num1=float(str1)
    sum=num1
    num1=0
    l1.clear()
    ab=1
def minus():
    global sum
    global num1
    global ab
    txt1.delete(1.0,2.0)
    str1="".join(map(str,l1))
    num1=float(str1)
    sum=num1
    l1.clear()
    ab=2
def multiplication():
    global ans
    global num1
    global ab
    txt1.delete(1.0,2.0)
    str1="".join(map(str,l1))
    num1=float(str1)
    ans=num1
    num1=0
    l1.clear()
    ab=3
def division():
    global ans
    global num1
    global ab
    txt1.delete(1.0,2.0)
    str1="".join(map(str,l1))
    num1=float(str1)
    ans=num1
    l1.clear()
    ab=4
def plusminus():
    txt1.insert(INSERT,"-")
    l1.append("-")
def onebyx():
    txt1.delete(1.0,2.0)
    global sum
    global num1
    str1="".join(map(str,l1))
    num1=float(str1)
    sum=1/num1
    txt1.insert(INSERT,sum)
    l1.clear()
    l1.append(sum)
    sum=0
    num1=0
def square():
    txt1.delete(1.0,2.0)
    global sum
    global num1
    str1="".join(map(str,l1))
    num1=float(str1)
    num1=int(num1)
    sum=num1**2
    txt1.insert(INSERT,sum)
    l1.clear()
    l1.append(sum)
def sqrt():
    import math
    txt1.delete(1.0,2.0)
    global sum
    global num1
    str1="".join(map(str,l1))
    num1=float(str1)
    num1=int(num1)
    sum=math.sqrt(num1)
    txt1.insert(INSERT,sum)
    l1.clear()
    l1.append(sum)
def modulo():
    global sum
    global num1
    global ab
    txt1.delete(1.0,2.0)
    str1="".join(map(str,l1))
    num1=float(str1)
    sum=num1
    l1.clear()
    ab=5
def clear():
    txt1.delete(1.0,2.0)
    l1.clear()
    sum=0
    num1=0
    ab=0
    ans=1
def delete():
    global l1
    txt1.delete("end-2c")
    str1="".join(map(str,l1))
    l1=list(str1)
    del l1[-1]
def isequalto():
    global num1
    global sum
    global ans
    global ab
    if ab==1:
        txt1.delete(1.0,2.0)
        str1="".join(map(str,l1))
        num1=float(str1)
        sum=num1+sum
        txt1.insert(INSERT,sum)
        l1.clear()
        l1.append(sum)
        sum=0
        num1=0
    elif ab==2:
        txt1.delete(1.0,2.0)
        str1="".join(map(str,l1))
        num1=float(str1)
        sum=sum-num1
        txt1.insert(INSERT,sum)
        l1.clear()
        l1.append(sum)
        sum=0
        num1=0
    elif ab==3:
        txt1.delete(1.0,2.0)
        str1="".join(map(str,l1))
        num1=float(str1)
        ans=num1*ans
        txt1.insert(INSERT,ans)
        l1.clear()
        l1.append(ans)
        ans=1
        num1=0
    elif ab==4:
        txt1.delete(1.0,2.0)
        str1="".join(map(str,l1))
        num1=float(str1)
        ans=ans/num1
        txt1.insert(INSERT,ans)
        l1.clear()
        l1.append(ans)
        ans=1
        num1=0
    elif ab==5:
        txt1.delete(1.0,2.0)
        str1="".join(map(str,l1))
        num1=float(str1)
        sum=sum%num1
        txt1.insert(INSERT,sum)
        l1.clear()
        l1.append(sum)
        sum=0
        num1=0
lbl=Label(top,height="2",width="320")
lbl.pack()
txt1=Text(top,height="3",width="320",font=("Calibri",20))
txt1.pack()
txt1.place(x=0,y=30)
btnper=Button(top,text="%",height="2",width="13",command=modulo,bg="#D0D3D4")
btnper.pack()
btnper.place(x=3,y=165)
btnc=Button(top,text="C",height="2",width="13",command=clear,bg="#D0D3D4")
btnc.pack()
btnc.place(x=111,y=165)
btndel=Button(top,text="Del",height="2",width="13",command=delete,bg="#D0D3D4")
btndel.pack
btndel.place(x=219,y=165)
btndinom=Button(top,text="1/x",height="2",width="10",command=onebyx,bg="#D0D3D4")
btndinom.pack()
btndinom.place(x=3,y=215)
btnsqrt=Button(top,text="x^2",height="2",width="10",command=square,bg="#D0D3D4")
btnsqrt.pack()
btnsqrt.place(x=82,y=215)
btnroot=Button(top,text="√x",height="2",width="10",command=sqrt,bg="#D0D3D4")
btnroot.pack()
btnroot.place(x=161,y=215)
btndiv=Button(top,text="÷",height="2",width="10",command=division,bg="#D0D3D4")
btndiv.pack()
btndiv.place(x=240,y=215)
btn7=Button(top,text="7",height="2",width="10",command=g,bg="#FDFEFE")
btn7.pack()
btn7.place(x=3,y=265)
btn8=Button(top,text="8",height="2",width="10",command=h,bg="#FDFEFE")
btn8.pack()
btn8.place(x=82,y=265)
btn9=Button(top,text="9",height="2",width="10",command=i,bg="#FDFEFE")
btn9.pack()
btn9.place(x=161,y=265)
btnx=Button(top,text="x",height="2",width="10",command=multiplication,bg="#D0D3D4")
btnx.pack()
btnx.place(x=240,y=265)
btn4=Button(top,text="4",height="2",width="10",command=d,bg="#FDFEFE")
btn4.pack()
btn4.place(x=3,y=315)
btn5=Button(top,text="5",height="2",width="10",command=e,bg="#FDFEFE")
btn5.pack()
btn5.place(x=82,y=315)
btn6=Button(top,text="6",height="2",width="10",command=f,bg="#FDFEFE")
btn6.pack()
btn6.place(x=161,y=315)
btnms=Button(top,text="-",height="2",width="10",command=minus,bg="#D0D3D4")
btnms.pack()
btnms.place(x=240,y=315)
btn1=Button(top,text="1",height="2",width="10",command=a,bg="#FDFEFE")
btn1.pack()
btn1.place(x=3,y=365)
btn2=Button(top,text="2",height="2",width="10",command=b,bg="#FDFEFE")
btn2.pack()
btn2.place(x=82,y=365)
btn3=Button(top,text="3",height="2",width="10",command=c,bg="#FDFEFE")
btn3.pack()
btn3.place(x=161,y=365)
btnpls=Button(top,text="+",height="2",width="10",command=plus,bg="#D0D3D4")
btnpls.pack()
btnpls.place(x=240,y=365)
btnpm=Button(top,text="+/-",height="2",width="10",command=plusminus,bg="#FDFEFE")
btnpm.pack()
btnpm.place(x=3,y=415)
btnzero=Button(top,text="0",height="2",width="10",command=j,bg="#FDFEFE")
btnzero.pack()
btnzero.place(x=82,y=415)
btndot=Button(top,text=".",height="2",width="10",command=k,bg="#FDFEFE")
btndot.pack()
btndot.place(x=161,y=415)
btneq=Button(top,text="=",height="2",width="10",command=isequalto,bg="#4169E1")
btneq.pack()
btneq.place(x=240,y=415)
top.mainloop()