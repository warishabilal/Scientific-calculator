from tkinter import*
import math as m
window=Tk()
window.geometry("383x570+470+20")
window.title("advanced cal")
window.config(bg="gray11")
window.resizable(0,0)
window.overrideredirect(1)

def close():
    window.destroy()

def clear():
    entry.delete(0,"end")

def back():
    last_number=len(entry.get())-1
    entry.delete(last_number)

def press(input):
    length=len(entry.get())
    entry.insert(length,input)

def add(a,b):
    return int(a) + int(b)

def subtract(a,b):
    return int(a) - int(b)

def divide (a,b):
    return int(a) / int(b)

def multiply (a,b):
    return int(a) * int(b)

def expression_break(sign,expression):
    values = expression.split(sign,1)
    return values

def scientific(expression):
    data= expression_break ("(",expression)
    if data[0]=="tan":
        result=m.tan(int(data[1]))

    elif data[0]=="cos":
        result=m.cos(int(data[1]))

    elif data[0]=="sin":
        result=m.sin(int(data[1]))

    elif data[0]=="sqrt":
        result=m.sqrt(int(data[1]))

    elif data[0]=="log":
        result=m.log10(int(data[1]))
    
    elif data[0]=="ln":
        result=m.log(int(data[1]))

    elif data[0]=="deg":
        result=m.degrees(int(data[1]))

    elif data[0]=="rad":
        result=m.radians(int(data[1]))

    elif data[0]=="fac":
        result=m.factorial(int(data[1]))
    return result

def equal():
    expression = entry.get()
    clear()
    try:
        if expression.find("(") > 0:
            result= scientific (expression)
        elif expression.find("pow") > 0:
            data=expression_break("pow",expression)
            result= m.pow(int(data[0]), int(data[1]))

        elif expression.find("rem") > 0:
            data=expression_break("rem",expression)
            result= m.remainder(int(data[0]), int(data[1]))

        elif "*" in expression :
            data=expression_break("*",expression)
            result= multiply(data[0],data[1])

        elif "/" in expression:
            data=expression_break("/",expression)
            result=divide (data[0],data[1])

        elif expression.find("+") > 0:
            first= expression.find("+")
            second=expression.find("+",(first+1),(first+5))
            if first>second:
                data=expression_break("+",expression)
                result= add(data[0],data[1])
            else:
                result= add(expression[0:second],expression[second+1:])
        elif expression.rindex("-") >0:
            sign=expression.rindex("-")
            result=subtract(expression[0:sign],expression[sign+1:])

        entry.insert(0,result)
    except:
        entry.insert(0,"error")

entry_string=StringVar()
entry=Entry(window,textvariable= entry_string,foreground="white",background="gray20",border=0,
            font=("Bahnschrift SemiBold",26))
entry.grid(columnspan=4,ipady=15)
font_value=("calibari",18)
btn_tan=Button(window,text="tan",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press("tan("))
btn_tan.grid(row=1,column=0,sticky=E+W,ipady=5)
btn_cos=Button(window,text="cos",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press("cos("))
btn_cos.grid(row=1,column=1,sticky=E+W,ipady=5)
btn_sin=Button(window,text="sin",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press("sin("))
btn_sin.grid(row=1,column=2,sticky=E+W,ipady=5)
btn_sqrt=Button(window,text="sqrt",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press("sqrt("))
btn_sqrt.grid(row=1,column=3,sticky=E+W,ipady=5)
btn_log=Button(window,text="log",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press("log("))
btn_log.grid(row=2,column=0,sticky=E+W,ipady=5)
btn_ln=Button(window,text="ln",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press("ln("))
btn_ln.grid(row=2,column=1,sticky=E+W,ipady=5)
btn_deg=Button(window,text="deg",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press("deg("))
btn_deg.grid(row=2,column=2,sticky=E+W,ipady=5)
btn_rad=Button(window,text="rad",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press("rad("))
btn_rad.grid(row=2,column=3,sticky=E+W,ipady=5)
btn_fac=Button(window,text="fac",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press("fac("))
btn_fac.grid(row=3,column=0,sticky=E+W,ipady=5)
btn_pow=Button(window,text="pow",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press("pow"))
btn_pow.grid(row=3,column=1,sticky=E+W,ipady=5)
btn_remainder=Button(window,text="rem",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press("rem"))
btn_remainder.grid(row=3,column=2,sticky=E+W,ipady=5)
btn_pi=Button(window,text="pi",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press(3.141592))
btn_pi.grid(row=3,column=3,sticky=E+W,ipady=5)
btn_clear=Button(window,text="C",background="gray5",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=clear)
btn_clear.grid(row=4,columnspan=2,column=0,sticky=E+W,ipady=5)
btn_backspace=Button(window,text="B",background="gray5",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=back)
btn_backspace.grid(row=4,columnspan=2,column=2,sticky=E+W,ipady=5)
btn_7=Button(window,text="7",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press(7))
btn_7.grid(row=5,column=0,sticky=E+W,ipady=5)
btn_8=Button(window,text="8",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press(8))
btn_8.grid(row=5,column=1,sticky=E+W,ipady=5)
btn_9=Button(window,text="9",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press(9))
btn_9.grid(row=5,column=2,sticky=E+W,ipady=5)
btn_divide=Button(window,text="/",background="gray5",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press("/"))
btn_divide.grid(row=5,column=3,sticky=E+W,ipady=5)
btn_4=Button(window,text="4",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press(4))
btn_4.grid(row=6,column=0,sticky=E+W,ipady=5)
btn_5=Button(window,text="5",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press(5))
btn_5.grid(row=6,column=1,sticky=E+W,ipady=5)
btn_6=Button(window,text="6",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press(6))
btn_6.grid(row=6,column=2,sticky=E+W,ipady=5)
btn_multiply=Button(window,text="*",background="gray5",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press("*"))
btn_multiply.grid(row=6,column=3,sticky=E+W,ipady=5)
btn_1=Button(window,text="1",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press(1))
btn_1.grid(row=7,column=0,sticky=E+W,ipady=5)
btn_2=Button(window,text="2",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press(2))
btn_2.grid(row=7,column=1,sticky=E+W,ipady=5)
btn_3=Button(window,text="3",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press(3))
btn_3.grid(row=7,column=2,sticky=E+W,ipady=5)
btn_subtract=Button(window,text="-",background="gray5",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press("-"))
btn_subtract.grid(row=7,column=3,sticky=E+W,ipady=5)
btn_dot=Button(window,text=".",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press("."))
btn_dot.grid(row=8,column=0,sticky=E+W,ipady=5)
btn_0=Button(window,text="0",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press(0))
btn_0.grid(row=8,column=1,sticky=E+W,ipady=5)
btn_e=Button(window,text="e",background="gray11",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press(2.71828))
btn_e.grid(row=8,column=2,sticky=E+W,ipady=5)
btn_add=Button(window,text="+",background="gray5",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=lambda:press("+"))
btn_add.grid(row=8,column=3,sticky=E+W,ipady=5)
btn_equal=Button(window,text="=",background="darkorange1",foreground="white",font=font_value,borderwidth=1,
               relief=SOLID,command= equal)
btn_equal.grid(row=9,column=0,columnspan=3,sticky=E+W,ipady=5)
btn_close=Button(window,text="close",background="gray5",foreground="darkorange1",font=font_value,borderwidth=1,
               relief=SOLID,command=close)
btn_close.grid(row=9,column=3,sticky=E+W,ipady=5)
mainloop()
