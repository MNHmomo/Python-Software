from tkinter import *
root = Tk()
root.geometry("400x300")

def getvals():
    print("Accepted")

#Heading
Label(root, text="MACH Registration Form", font="Arial 15 bold").grid(row = 0, column = 3)

# Field Name
name = Label(root,text="Name")
username = Label(root,text="Username")
phone = Label(root,text="Phone")
payment = Label(root,text="Payment Method")

# Packing Fields
name.grid(row = 1, column = 2)
username.grid(row = 2, column = 2)
phone.grid(row = 3, column = 2)
payment.grid(row = 4, column = 2)

# Variable Storing Data
namevalue = StringVar
usernamevalue = StringVar
phonevalue = StringVar
paymentvalue = StringVar
checkvalue = IntVar

# Entry Fields
nameentry = Entry(root, textvariable =namevalue)
usernameentry = Entry(root, textvariable =usernamevalue)
phoneentry = Entry(root, textvariable =phonevalue)
paymententry = Entry(root, textvariable =paymentvalue)

# Packing Entry Fields
nameentry.grid(row = 1, column = 3)
usernameentry.grid(row = 2, column = 3)
phoneentry.grid(row = 3, column = 3)
paymententry.grid(row = 4, column = 3)

# Creating Checkbox
checkbtn = Checkbutton(text="Remember Me", variable = checkvalue)
checkbtn.grid(row = 6, column = 3)

# Sumbit Button
Button(text = "Submit", command = getvals).grid(row = 7, column = 3)

root.mainloop()