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
    files_number = files_num

    my_label_2.destroy()
    entry_3.destroy()
    b_4.destroy()

    for file in file_menu:
        extension_list = file.rsplit(".", 1)
        extension = "." + extension_list[1]
        old_path = extension_list[0] + extension
        folder_path = file.rsplit("/", 1)
        folder_path_1 = folder_path[0] + "/"
        new_path = folder_path_1 + files_name + files_split + str(files_number) + extension
        os.rename(old_path, new_path)
        files_number = int(files_number) + 1

    last_label = tk.Label(root, text="Done!")
    last_label.pack()

    last_button = tk.Button(root, text="Exit", command=root.destroy)
    last_button.pack()


def button3():
    global files_num
    global my_label_2
    global entry_3
    global b_4

    files_num = int(entry_2.get())

    my_label_1.destroy()
    entry_2.destroy()
    b_3.destroy()

    my_label_2 = tk.Label(root, text="Insert the character that separates the text and the number")
    my_label_2.pack()
    entry_3 = tk.Entry(root, fg="white", bg="black")
    entry_3.pack()
    b_4 = tk.Button(root, text="Submit", command=button4)
    b_4.pack()


def button2():
    global files_name
    global my_label_1
    global entry_2
    global b_3

    files_name = str(entry_1.get())

    my_label.destroy()
    entry_1.destroy()
    b_2.destroy()

    my_label_1 = tk.Label(root, text="Insert the first file's number")  # A button
    my_label_1.pack()
    entry_2 = tk.Entry(root, fg="white", bg="black")                   # An Entry with the number to start with
    entry_2.pack()
    b_3 = tk.Button(root, text="Submit", command=button3)             # A button that starts the next function
    b_3.pack()


def button():
    global file_menu
    global entry_1
    global my_label
    global entry_1
    global b_2

    why.destroy()

    file_menu = tk.filedialog.askopenfilenames(parent=root, filetypes=[("All Files", "*.*")])
    my_label = tk.Label(root, text="Insert the files core name (without numbers)")
    my_label.pack()
    entry_1 = tk.Entry(root, fg="white", bg="black")
    entry_1.pack()
    b_2 = tk.Button(root, text="Submit", command=button2)
    b_2.pack()


def multiple():
    global why
    b__1.destroy()
    b__2.destroy()
    why = tk.Button(root, text="Open Files", command=button)
    why.pack()


frame = tk.Frame(root)
frame.pack(side="top")

b__1 = tk.Button(frame, text="Rename one File")
b__1.pack(side="left")

b__2 = tk.Button(frame, text="Rename multiple files", command=multiple)
b__2.pack(side="left")

root.mainloop()

# todo add comments
# todo add a dialog box instead of inserting the path of the file
# todo add a github repository
# todo add try\except
# todo add a function to rename one file
