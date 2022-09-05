import datetime
import tkinter as tk
from PIL import Image, ImageTk


# defining the Person class
class Person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age
# defining function to get input from entry
def getInput(event):
    name = nameEntry.get()
    monkey = Person(name,datetime.date(int(yearEntry.get()),int(monthEntry.get()),int(dateEntry.get())))
    textArea = tk.Text(master=window, height=10,width=25)
    textArea.grid(column=1, row=6)
    answer = "Hey {monkey}!!!. You are {age} years old".format(monkey=name, age=monkey.age())
    textArea.insert(tk.END,answer)


window = tk.Tk()
window.geometry("380x320")
window.title("Age Calculator App")

#Adding an Image.
image = Image.open('index.jpeg')
image.thumbnail((300,300),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1,row=0)

# creating necessary labels
name = tk.Label(text="Name")
name.grid(column=0,row=1)
year = tk.Label(text="Year")
year.grid(column=0,row=2)
month = tk.Label(text="Month")
month.grid(column=0, row=3)
date = tk.Label(text="Day")
date.grid(column=0,row=4)

# creating entry_fields for each label
nameEntry = tk.Entry()
nameEntry.grid(column=1, row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1, row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1, row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1, row=4)

# creating submit button
submitButton = tk.Button(window, text="Submit", command=getInput, bg="green")
submitButton.grid(column=1, row=5)
submitButton.bind("<Button-1>", getInput)


window.mainloop()