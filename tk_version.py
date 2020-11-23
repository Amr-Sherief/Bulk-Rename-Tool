import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.title("Bulk Rename Tool")
root.attributes('-fullscreen', True)

intro = tk.Label(root, text="This is a file renaming program", fg="Blue")
intro.pack()


def button4():
    global files_split
    files_split = entry_3.get()
    count = 0

    for file in file_menu:
        extension = file.rsplit(".", 1)
        print(extension)
        count = count + 1


def button3():
    global files_num
    global entry_3
    files_num = int(entry_2.get())
    my_label_2 = tk.Label(root, text="Insert the character that separates the text and the number")
    my_label_2.pack()
    entry_3 = tk.Entry(root, fg="white", bg="black")
    entry_3.pack()
    b_4 = tk.Button(root, text="Submit", command=button4)
    b_4.pack()


def button2():
    global files_name
    global entry_2
    files_name = entry_1.get()
    my_label_1 = tk.Label(root, text="Insert the first files number")
    my_label_1.pack()
    entry_2 = tk.Entry(root, fg="white", bg="black")
    entry_2.pack()
    b_3 = tk.Button(root, text="Submit", command=button3)
    b_3.pack()


def button():
    global file_menu
    global entry_1
    file_menu = tk.filedialog.askopenfilenames(parent=root, filetypes=[("All Files", "*.*")])
    my_label = tk.Label(root, text="Insert the files core name (without numbers)")
    my_label.pack()
    entry_1 = tk.Entry(root, fg="white", bg="black")
    entry_1.pack()
    b_2 = tk.Button(root, text="Submit", command=button2)
    b_2.pack()

        #extension = "." + str(extension_list[len(extension_list) - 1])
        #my_label_3 = tk.Label(root, text="Please insert the new name for the file with the " + extension)
        #my_label_3.pack()

    #my_label = tk.Label(root, text="Please insert the full path of the file")
    #my_label.pack()
    #old_path = tk.Entry(root, bg="black", fg="white", width=80)   # todo make this a dialog box
    #old_path.pack()



b = tk.Button(root, text="Open Files", command=button)
b.pack()


root.mainloop()

# todo add comments
# todo add a dialog box instead of inserting the path of the file
# todo add a github repository
# todo add try\except