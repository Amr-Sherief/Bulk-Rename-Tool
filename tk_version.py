import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()                            # Defines the window where the program would be
root.title("Bulk Rename Tool")            # Defines the title of the window
root.attributes('-fullscreen', True)      # Opens the window in fullscreen

intro = tk.Label(root, text="This is a file renaming program", fg="Blue")       # Defines the use of the program
intro.pack()


def single2():

    rename = entry_s_1.get()      # the file new name

    my_label_s.destroy()
    entry_s_1.destroy()
    b_s_2.destroy()

    extension_list_s = file_dialog.rsplit(".", 1)         # Splits a list to get the file extension
    extension_s = "." + extension_list_s[1]               # gets the file extension
    old_path_s = extension_list_s[0] + extension_s        # gets the old path for the file
    folder_path_s = file_dialog.rsplit("/", 1)            # Splits a list to get the folder path
    folder_path_1_s = folder_path_s[0] + "/"              # gets the folder path
    new_path_s = folder_path_1_s + rename + extension_s   # gets the new path for the file with the new name
    os.rename(old_path_s, new_path_s)                     # renames the file

    change = folder_path_s[1] + " --> " + rename          # text with the changed that happened to the file's name

    change_label_s = tk.Label(root, text=change)          # a label with the change variable
    change_label_s.pack()

    done = tk.Label(root, text="Done")
    done.pack()

    exit_s = tk.Button(root, text="Exit", command=root.destroy)
    # a button to destroy the main window and exit the program
    exit_s.pack()


def single1():
    global file_dialog
    global my_label_s
    global entry_s_1
    global b_s_2

    why_1.destroy()

    file_dialog = tk.filedialog.askopenfilename(parent=root, filetypes=[("All Files", "*.*")])
    # defines a file dialog from which the client would choose the file to rename
    my_label_s = tk.Label(root, text="Insert the file new name")
    my_label_s.pack()
    entry_s_1 = tk.Entry(root, fg="white", bg="black")
    # An Entry with the new name for the file remark after being renamed
    entry_s_1.pack()
    b_s_2 = tk.Button(root, text="Submit", command=single2)   # a button to start the (single2) function
    b_s_2.pack()


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
    except:                               # Create an exception if the above variable was remark inserted as a string

        my_label_1.destroy()
        entry_2.destroy()
        b_3.destroy()

        error = tk.Label(root, text="Please Only insert a number")
        error.pack()
        click = tk.Button(root, text="Exit", command=root.destroy)
        # a button that destroys the main (root) window and exits the program
        click.pack()
        return                             # stops the function at this point

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
    file_menu_val = file_menu
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


def single():
    global why_1
    b__1.destroy()
    b__2.destroy()
    why_1 = tk.Button(root, text="Open Files", command=single1)  # a button to start the (button) function
    why_1.pack()


frame = tk.Frame(root)                 # a frame to put the first choices buttons ("b__1" and "b__2") in
frame.pack(side="top")                 # packs the frame at the top center of the (root) window

b__1 = tk.Button(frame, text="Rename one File", command=single)
# the choice to rename one file                 # a button to start the (single) function
b__1.pack(side="left")        # packs the button to the left of the frame

b__2 = tk.Button(frame, text="Rename multiple files", command=multiple)
# the choice to rename multiple files        # a button to start the (multiple) function
b__2.pack(side="left")        # packs the button to the left of the frame and to the right of the (b__1) button

root.mainloop()             # initiates the loop for the root window
# remark without the main loop the program won't run as it refreshes the window
