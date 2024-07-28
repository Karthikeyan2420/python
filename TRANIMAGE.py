import tkinter as tk

root = tk.Tk()


# Create a label with an image with transparency
image = tk.PhotoImage(file="TRAN.jpg")  # Make sure to have a transparent PNG image
transparent_image_label = tk.Label(root, image=image,text="natpu forever")
transparent_image_label.pack()

root.mainloop()
