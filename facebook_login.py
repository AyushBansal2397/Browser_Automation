from selenium import webdriver
from tkinter import *

flag = 0
root = Tk()
root.title("Facebook login")
root.geometry("250x80+"+str(int(root.winfo_screenwidth()/2-125))+"+"+str(int(root.winfo_screenheight()/2-40)))
name_entry = Entry(root)
pass_entry = Entry(root)

def print_crap(event):
	global name_entry, pass_entry, flag
	if name_entry.get() != "" and pass_entry.get() != "":
		login(name_entry.get(), pass_entry.get())
	else:
		GUI()

#GUI Part
def GUI():
	name = Label(root, text="Email :")
	password = Label(root, text="Password :")
	button = Button(root, text="Submit")
	name.grid(row=0, column=0, pady=2, padx=2, sticky=E)
	password.grid(row=1, column=0, sticky=E)
	name_entry.grid(row=0, column=1)
	pass_entry.grid(row=1, column=1)
	button.grid(row=2, column=1, columnspan=2)
	button.bind("<Button-1>", print_crap)
	root.mainloop()

# Login Part
def login(username, pwd):
	root.destroy()
	driver = webdriver.Chrome()
	driver.get("https://www.facebook.com/")
	usr_box = driver.find_element_by_id("email").send_keys(username)
	pwd_box = driver.find_element_by_id("pass").send_keys(pwd)
	login = driver.find_element_by_id("u_0_2").submit()
	while True:
		continue

if __name__ == '__main__':
	GUI()
