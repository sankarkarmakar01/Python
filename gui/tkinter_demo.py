from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


def handle_login():
    email = email_input.get()
    password = password_input.get()
    if email == 'sankar@gmail.com' and password == '1234':
        messagebox.showinfo('Yayy', 'Login Successful')
    else:
        messagebox.showerror('Error', 'Login Failed')


root = Tk()

root.title("Login Form")
root.iconbitmap('fevicon.ico')

root.geometry("350x500")
root.configure(background='#0096DC')

img = Image.open('logo.png')
resized_img = img.resize((70, 70))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root, image=img)
img_label.pack(pady=(10, 10))

text_lable = Label(root, text="White Devil", fg='white', bg='#0096DC')
text_lable.pack()
text_lable.config(font=('verdana', 24))

email_lable = Label(root, text="Enter Email", fg='white', bg='#0096DC')
email_lable.pack(pady=(20, 5))
email_lable.config(font=('verdana', 12))

email_input = Entry(root, width=50)
email_input.pack(ipady=6, pady=(1, 15))

password_lable = Label(root, text="Enter Pssword", fg='white', bg='#0096DC')
password_lable.pack(pady=(20, 5))
password_lable.config(font=('verdana', 12))

password_input = Entry(root, width=50)
password_input.pack(ipady=6, pady=(1, 15))

login_button = Button(root, text="Login Here", bg='white', fg='black', width=30, height=2, command=handle_login)
login_button.pack(pady=(10, 20))
login_button.config(font=('verdana', 10))

root.mainloop()  # hold the window in the screen

# root.minsize(400,400)
# root.maxsize(800,800)
