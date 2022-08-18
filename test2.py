import string
import random
import pyautogui
from tkinter import messagebox

while True:
    strength_of_password = pyautogui.prompt("\nHow strong do you want your password to be? (digits/simple/mediocre/hard/extreme)", "Question...",)
    while True:
        length_of_password = int(pyautogui.prompt("How long do you want the password to be? \n(number of characters)", "Question..."))
        if length_of_password < 4:
            messagebox.showerror("Attention!","The password must be greater than or equal to 4 characters... Try Again!")
        else:
            break      
    if strength_of_password == 'digits':
        combined = string.digits
        break
    elif strength_of_password == 'simple':
        combined = string.ascii_lowercase
        break
    elif strength_of_password == 'mediocre':
        combined = string.ascii_lowercase + string.digits
        break
    elif strength_of_password == 'hard':
        combined = string.ascii_uppercase + string.ascii_lowercase + string.digits
        break
    elif strength_of_password == 'extreme':
        combined = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
        break
    else:
        messagebox.showerror("Attention!", "Please enter a valid choice...")

password = "".join(random.sample(combined, length_of_password))
messagebox.showinfo("Information", "Your password is: " + password + "\nWrite it down somewhere so you don't forget.")