from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.geometry("600x700")
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
image_label.pack()
root.mainloop()