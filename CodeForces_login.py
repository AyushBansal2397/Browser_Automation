from selenium import webdriver
from tkinter import *

flag = 0
root = Tk()
root.title("CodeForces login")
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
	# global name_entry, pass_entry, root
	name = Label(root, text="Handle :")
	password = Label(root, text="Password :")
	button = Button(root, text="Submit")
	name.grid(row=0, column=0, pady=2, padx=2, sticky=E)
	password.grid(row=1, column=0, sticky=E)
	name_entry.grid(row=0, column=1)
	pass_entry.grid(row=1, column=1)
	button.grid(row=2, column=1, sticky=W)
	button.bind("<Button-1>", print_crap)
	root.mainloop()

# Login Part
def login(handle, password):
	root.destroy()
	driver = webdriver.Chrome()
	driver.get("http://codeforces.com/enter?back=%2F")
	email = driver.find_element_by_id("handleOrEmail").send_keys(handle)
	pwd = driver.find_element_by_id("password").send_keys(password)
	rem = driver.find_element_by_id("remember").click()
	log = driver.find_element_by_class_name("submit").submit()
	del email, pwd, rem, log
	while True:
		continue

if __name__ == '__main__':
	GUI()
