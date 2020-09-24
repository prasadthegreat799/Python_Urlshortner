import pyperclip
import pyshorteners
from tkinter import *

root=Tk()
root.geometry("300x300")
root.title("Url Shortner")

url=StringVar()
url_address=StringVar()

def urlshortner():
    urladdress=url.get()
    url_short=pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    short_url=url_address.get()
    pyperclip.copy(short_url)

Label(root,text="My Url Shortner",font='poppins').pack(pady=10)

Label(root,text="Enter Your Url:").pack()
Entry(root,textvariable=url).pack(pady=5)

Button(root,text="Generate Short Url",command=urlshortner).pack(pady=7)

Entry(root,textvariable=url_address).pack(pady=5)
Button(root,text="Copy Url",command=copyurl).pack(pady=7)


root.mainloop()
