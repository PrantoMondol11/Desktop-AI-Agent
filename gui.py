from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.geometry("600x800")
root.resizable(False,False)
root.title("App")
root.config(bg="lightgray")
frame = LabelFrame(root,background="#82D8E9",height=400,relief="raised",width=500,borderwidth=7)
frame.pack(pady=10)
frame.pack_propagate(False)
text_label=Label(frame, 
                        text="Lili AI Agent", 
                        font=("Arial", 16, "bold italic"), 
                        fg="black",bg="#5FA8B6")
text_label.pack(pady=5)
image_path="pic.jpg"
original_image = Image.open(image_path)
max_size = (300, 300)
original_image.thumbnail(max_size)
tk_image = ImageTk.PhotoImage(original_image)
image_label = Label(frame, image=tk_image)
image_label.pack(padx=10)

def ask():
    print("ask.....")
def send():
    print("send")
def delete():
    print("delete")

text=Text(root,width=40,height=10,font =("Courier", 14))
text.pack(padx=10,pady=10)

entry=Entry(root,justify="center")
entry.place(x=100,y=650,width=350)

button1=Button(root,text="Ask",bg="blue",justify="center",padx=10,pady=10,command=ask)
button1.place(x=200,y=700)
button2=Button(root,text="Send",bg="blue",justify="center",padx=10,pady=10)
button2.place(x=300,y=700)
button3=Button(root,text="Delete",bg="blue",justify="center",padx=10,pady=10)
button3.place(x=400,y=700)
root.mainloop()