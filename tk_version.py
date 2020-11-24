import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()                            # Defines the window where the program would be
root.title("Bulk Rename Tool")            # Defines the title of the window
root.attributes('-fullscreen', True)      # Opens the window in fullscreen

intro = tk.Label(root, text="This is a file renaming program", fg="Blue")       # Defines the use of the program
intro.pack()


def Error():
    button2()

def button4():
    global files_split

    files_split = entry_3.get()                     # reassigns the files splitting character
    files_number = files_num                        # reassign the files first number to index with the renamed files

    my_label_2.destroy()
    entry_3.destroy()
    b_4.destroy()

    for file in file_menu:
        extension_list = file.rsplit(".", 1)        # Splits the file path to get the file extension
        extension = "." + extension_list[1]         # Defines the extension of the file
        old_path = extension_list[0] + extension    # Defines the old path for the file remark before renaming
        folder_path = file.rsplit("/", 1)           # Splits th file path to get the folder
        folder_path_1 = folder_path[0] + "/"        # Defines the folder path
        new_path = folder_path_1 + files_name + files_split + str(files_number) + extension
        # defines the new path for the file with the new name
        os.rename(old_path, new_path)
        # Renames the file from the old path to the new path including the new name
        change = folder_path[1] + " --> " + files_name + files_split + str(files_number) + extension
        # a variable containing text which shows the change in the files names remark after being renamed
        change_label = tk.Label(root, text=change)  # a label which show the change variable
        change_label.pack()
        files_number = int(files_number) + 1
        # increments the variable every time the for loop ends to change the index number in every file

    last_label = tk.Label(root, text="Done!")
    last_label.pack()

    last_button = tk.Button(root, text="Exit", command=root.destroy)
    # A button which ends the program by closing the main window
    last_button.pack()


def button3():
    global files_num
    global my_label_2
    global entry_3
    global b_4


    try:
        files_num = int(entry_2.get())
    except:

        my_label_1.destroy()
        entry_2.destroy()
        b_3.destroy()

        error = tk.Label(root, text="Please Only insert a number")
        error.pack()
        click = tk.Button(root, text="Click Me!!", command=Error)
        click.pack()
        return

    # a variable containing the the number to begin with in indexing the files names

    my_label_1.destroy()
    entry_2.destroy()
    b_3.destroy()

    my_label_2 = tk.Label(root, text="Insert the character that separates the text and the number")
    my_label_2.pack()
    entry_3 = tk.Entry(root, fg="white", bg="black")
    # An entry with the file name and index number splitting character
    entry_3.pack()
    b_4 = tk.Button(root, text="Submit", command=button4)   # a button to start the (button4) function
    b_4.pack()


def button2():
    global files_name
    global my_label_1
    global entry_2
    global b_3


    files_name = str(entry_1.get())                   # a variable with the files core name

    my_label.destroy()
    entry_1.destroy()
    b_2.destroy()

    my_label_1 = tk.Label(root, text="Insert the first file's number")
    my_label_1.pack()
    entry_2 = tk.Entry(root, fg="white", bg="black")                   # An Entry with the number to start with
    entry_2.pack()
    b_3 = tk.Button(root, text="Submit", command=button3)             # A button to start the (button3) function
    b_3.pack()


def button():
    global file_menu
    global entry_1
    global my_label
    global entry_1
    global b_2

    why.destroy()

    file_menu = tk.filedialog.askopenfilenames(parent=root, filetypes=[("All Files", "*.*")])
    # defines a file dialog from which the client would choose the files to rename
    my_label = tk.Label(root, text="Insert the files core name (without numbers)")
    my_label.pack()
    entry_1 = tk.Entry(root, fg="white", bg="black")
    # An Entry with the core name for the files remark after being renamed
    entry_1.pack()
    b_2 = tk.Button(root, text="Submit", command=button2)   # a button to start the (button2) function
    b_2.pack()


def multiple():
    global why
    b__1.destroy()
    b__2.destroy()
    why = tk.Button(root, text="Open Files", command=button)        # a button to start the (button) function
    why.pack()


frame = tk.Frame(root)                 # a frame to put the first choices buttons ("b__1" and "b__2") in
frame.pack(side="top")                 # packs the frame at the top center of the (root) window

b__1 = tk.Button(frame, text="Rename one File")    # the choice to rename one file
b__1.pack(side="left")        # packs the button to the left of the frame

b__2 = tk.Button(frame, text="Rename multiple files", command=multiple)
# the choice to rename multiple files        # a button to start the (multiple) function
b__2.pack(side="left")        # packs the button to the left of the frame and to the right of the (b__1) button

root.mainloop()             # initiates the loop for the root window
# remark without the main loop the program won't run as it refreshes the window

# todo add a dialog box instead of inserting the path of the file
# todo add a github repository
# todo add try\except
# todo add a function to rename one file
