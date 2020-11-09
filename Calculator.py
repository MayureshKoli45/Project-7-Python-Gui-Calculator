import tkinter as tk
from PIL import Image, ImageTk


class Calculator:
    # Geometry, Title and icon constructor
    def __init__(self, master):
        self.master = master
        master.title("Calculator By Mayuresh Koli")
        master.geometry("325x590")
        master.maxsize(325, 590)
        master.minsize(325, 590)
        master.wm_iconbitmap("1.ico")

    # Setting up a Frame
    def Frame_widget(self):
        self.f1 = tk.Frame(bg="grey")
        self.f1.pack(side="left", fill="both")

    # Adding necessary images in our calculator by using PIL module
    def Image_widget(self):
        image = Image.open("wood button.jpg")
        photo = ImageTk.PhotoImage(image)
        self.imagelabel = tk.Label(self.f1, image=photo, pady=1000)
        self.imagelabel.image = photo
        self.imagelabel.pack(fill="both")

    def Image_widget_2(self):
        image = Image.open("wood button.jpg")
        photo = ImageTk.PhotoImage(image)
        self.imagelabel_2 = tk.Label(self.f1, image=photo)
        self.imagelabel_2.image = photo
        self.imagelabel_2.pack(fill="both")

    # Adding display
    def Entry_widget(self):
        global entryvalue
        self.entry = tk.Entry(
            self.imagelabel, textvariable=entryvalue, font="Ariel 40 bold", borderwidth=10)
        self.entry.pack(anchor="n", fill="both")
        self.entry.focus_set()

    # Declaration of click events
    def click(self, event):
        global entryvalue
        self.text = event.widget.cget("text")
        if self.text == "=":
            if entryvalue.get().isdigit():
                value = int(entryvalue.get())
            else:
                try:
                    value = eval(self.entry.get())
                except:
                    value = "Error"

            entryvalue.set(value)
            self.entry.update()

        elif self.text == "C":
            entryvalue.set("")
            self.entry.update()

        else:
            entryvalue.set(entryvalue.get() + str(self.text))
            self.entry.update()

    # Adding buttons to our calculator
    def Button_widget(self):
        for i in range(7, 10):
            buttonlayer = tk.Button(
                self.imagelabel_2, text=i, font="Ariel 15 bold", padx=20, pady=20)
            buttonlayer.grid(row=0, column=i-7, pady=10, padx=5)
            buttonlayer.bind("<Button-1>", self.click)

        for i in range(4, 7):
            buttonlayer = tk.Button(
                self.imagelabel_2, text=i, font="Ariel 15 bold", padx=20, pady=20)
            buttonlayer.grid(row=1, column=i-4, pady=10, padx=5)
            buttonlayer.bind("<Button-1>", self.click)

        for i in range(1, 4):
            buttonlayer = tk.Button(
                self.imagelabel_2, text=i, font="Ariel 15 bold", padx=20, pady=20)
            buttonlayer.grid(row=2, column=i-1, pady=10, padx=5)
            buttonlayer.bind("<Button-1>", self.click)

        list_1 = [".", "0", "="]
        for i in range(len(list_1)):
            buttonlayer = tk.Button(
                self.imagelabel_2, text=list_1[i], font="Ariel 15 bold", padx=20, pady=20)
            buttonlayer.grid(row=3, column=i, pady=10, padx=5)
            buttonlayer.bind("<Button-1>", self.click)

        list_2 = ["/", "*", "-", "+"]
        for i in range(len(list_2)):
            buttonlayer = tk.Button(
                self.imagelabel_2, text=list_2[i], font="Ariel 15 bold", padx=20, pady=20)
            buttonlayer.grid(row=i, column=3, pady=10, padx=5)
            buttonlayer.bind("<Button-1>", self.click)

        list_3 = ["C", "00"]
        for i in range(len(list_3)):
            buttonlayer = tk.Button(
                self.imagelabel_2, text=list_3[i], font="Ariel 15 bold", padx=20, pady=20)
            buttonlayer.grid(row=4, column=i+1, pady=10, padx=5)
            buttonlayer.bind("<Button-1>", self.click)


if __name__ == "__main__":
    # Calling all classes and functions
    root = tk.Tk()
    app = Calculator(root)
    entryvalue = tk.StringVar()
    entryvalue.set("")
    app.Frame_widget()
    app.Image_widget()
    app.Entry_widget()
    app.Image_widget_2()
    app.Button_widget()
    root.mainloop()
